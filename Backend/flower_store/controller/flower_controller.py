from http import HTTPStatus
from flask import abort
from flower_store.model.flower import Flower, FlowerObserverImpl
from flower_store.util.builder.flower_builder import FlowerBuilder
from flower_store.util.observer.flower_observer import FlowerSubject
from flower_store import db


class FlowerController:
    def __init__(self):
        self.subject = FlowerSubject()

    def create_flower(self, name, color, price):
        try:
            flower_builder = FlowerBuilder()
            flower = flower_builder \
                .set_name(name) \
                .set_color(color) \
                .set_price(price) \
                .build()

            db.session.add(flower)
            db.session.commit()
            new_observer = FlowerObserverImpl(flower.id)
            self.subject.add_observer(new_observer)
            self.subject.notify_observers(flower)
            return flower
        except Exception as e:
            db.session.rollback()
            raise e

    def get_flower(self, id):
        flower = Flower.query.get(id)
        if flower is None:
            abort(HTTPStatus.NOT_FOUND)
        return flower

    def get_all_flowers(self):
        return Flower.query.all()

    def update_flower(self, id, data):
        flower = self.get_flower(id)
        if flower is None:
            abort(HTTPStatus.NOT_FOUND)

        try:
            flower.name = data.get('name', flower.name)
            flower.color = data.get('color', flower.color)
            flower.price = data.get('price', flower.price)
            db.session.commit()

            observer = self.subject.find_observer(flower.id)
            if observer is None:
                observer = FlowerObserverImpl(flower.id)
                self.subject.add_observer(observer)
            self.subject.notify_observers(flower)

            return flower
        except Exception as e:
            db.session.rollback()
            raise e

    def delete_flower(self, id):
        flower = self.get_flower(id)
        if flower is None:
            abort(HTTPStatus.NOT_FOUND)

        try:
            db.session.delete(flower)
            db.session.commit()

            self.subject.notify_observers(flower)
            self.subject.remove_observer(flower.id)
        except Exception as e:
            db.session.rollback()
            raise e
