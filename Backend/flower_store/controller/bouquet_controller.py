from http import HTTPStatus
from flask import abort

from flower_store.model.catalogue import Catalogue
from flower_store.model.bouquet import Bouquet, BouquetObserverImpl
from flower_store.util.builder.bouquet_builder import BouquetBuilder
from flower_store.util.builder.packing_builder import PackingBuilder
from flower_store.util.observer.bouquet_observer import BouquetSubject
from flower_store import db


class BouquetController:
    def __init__(self):
        self.subject = BouquetSubject()

    def create_bouquet(self, eventType, price, flowers, packing, catalogue):
        try:
            packing_builder = PackingBuilder()
            packing = packing_builder.set_name(packing.get('name')).set_price(
                packing.get('price')).build()
            catalogue = Catalogue.query.filter_by(name=catalogue.get('name')).first()
            bouquet_builder = BouquetBuilder()
            bouquet = bouquet_builder \
                .set_eventType(eventType) \
                .set_price(price) \
                .set_packing(packing) \
                .set_flowers(flowers) \
                .set_catalogue(catalogue) \
                .build()

            db.session.add(bouquet)
            db.session.commit()
            new_observer = BouquetObserverImpl(bouquet.id)
            self.subject.add_observer(new_observer)
            self.subject.notify_observers(bouquet, action='created')
            return bouquet
        except Exception as e:
            db.session.rollback()
            raise e

    def get_bouquet(self, id):
        bouquet = Bouquet.query.get(id)
        if bouquet is None:
            abort(HTTPStatus.NOT_FOUND)
        return bouquet
    
    def get_by_event(self, eventType):
        bouquet = Bouquet.query.filter_by(eventType=eventType)
        if bouquet is None:
            abort(HTTPStatus.NOT_FOUND)
        list(map(lambda x: x.put_into_dto(), bouquet))

    def get_all_bouquets(self):
        return Bouquet.query.all()

    def update_bouquet(self, bouquet_id, eventType, price, flowers, packing, catalogueName):
        bouquet = self.get_bouquet(bouquet_id)
        if bouquet is None:
            abort(HTTPStatus.NOT_FOUND)

        try:
            packing_builder = PackingBuilder()
            packing = packing_builder.set_name(packing.get('name')).set_price(
                packing.get('price')).build()
            catalogue = Catalogue.query.filter_by(name=catalogueName).first()
            bouquet.catalogue = catalogue
            bouquet.eventType = eventType
            bouquet.price = price
            bouquet.flowers = flowers
            bouquet.packing = packing
            db.session.commit()
            observer = self.subject.find_observer(bouquet.id)
            if observer is None:
                observer = BouquetObserverImpl(bouquet.id)
                self.subject.add_observer(observer)
            self.subject.notify_observers(bouquet)
            return bouquet
        except Exception as e:
            db.session.rollback()
            raise e

    def delete_bouquet(self, id):
        bouquet = self.get_bouquet(id)
        if bouquet is None:
            abort(HTTPStatus.NOT_FOUND)

        try:

            db.session.delete(bouquet)
            db.session.commit()
            self.subject.notify_observers(bouquet, action='deleted')
            self.subject.remove_observer(bouquet.id)
        except Exception as e:
            db.session.rollback()
            raise e
