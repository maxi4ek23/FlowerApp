from http import HTTPStatus
from flask import abort
from flower_store.model.packing import Packing, PackingObserverImpl
from flower_store import db

from flower_store.util.observer.packing_observer import PackingSubject


class PackingController:
    def __init__(self):
        self.subject = PackingSubject()
    def create_packing(self, data):
        try:
            packing = Packing(
                name=data.get('name'),
                price=data.get('price')
            )
            db.session.add(packing)
            db.session.commit()
            new_observer = PackingObserverImpl(packing.id)
            self.subject.add_observer(new_observer)
            self.subject.notify_observers(packing)
            return packing
        except Exception as e:
            db.session.rollback()
            raise e

    def get_packing(self, id):
        packing = Packing.query.get(id)
        if packing is None:
            abort(HTTPStatus.NOT_FOUND)
        return packing

    def get_all_packings(self):
        return Packing.query.all()

    def update_packing(self, id, data):
        packing = self.get_packing(id)
        if packing is None:
            abort(HTTPStatus.NOT_FOUND)

        try:
            packing.name = data.get('name', packing.name)
            packing.price = data.get('price', packing.price)
            db.session.commit()
            observer = self.subject.find_observer(packing.id)
            if observer is None:
                observer = PackingObserverImpl(packing.id)
                self.subject.add_observer(observer)
            self.subject.notify_observers(packing)
            return packing
        except Exception as e:
            db.session.rollback()
            raise e

    def delete_packing(self, id):
        packing = self.get_packing(id)
        if packing is None:
            abort(HTTPStatus.NOT_FOUND)

        try:
            db.session.delete(packing)
            db.session.commit()
            self.subject.notify_observers(packing)
            self.subject.remove_observer(packing.id)
        except Exception as e:
            db.session.rollback()
            raise e
