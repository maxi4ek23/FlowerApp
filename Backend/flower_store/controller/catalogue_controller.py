from http import HTTPStatus
from flask import abort
from flower_store.model.catalogue import Catalogue, CatalogueObserverImpl
from flower_store.util.builder.catalogue_builder import CatalogueBuilder
from flower_store.util.observer.catalogue_observer import CatalogueSubject
from flower_store import db


class CatalogueController:
    def __init__(self):
        self.subject = CatalogueSubject()

    def create_catalogue(self, data):
        try:
            catalogue_builder = CatalogueBuilder()
            catalogue = catalogue_builder \
                .set_name(data.get('name')) \
                .set_bouquets([]) \
                .build()

            db.session.add(catalogue)
            db.session.commit()
            new_observer = CatalogueObserverImpl(catalogue.id)
            self.subject.add_observer(new_observer)
            self.subject.notify_observers(catalogue)
            return catalogue
        except Exception as e:
            db.session.rollback()
            raise e

    def get_catalogue(self, id):
        catalogue = Catalogue.query.get(id)
        if catalogue is None:
            abort(HTTPStatus.NOT_FOUND)
        return catalogue

    def get_all_catalogues(self):
        return Catalogue.query.all()

    def update_catalogue(self, id, data):
        catalogue = self.get_catalogue(id)
        if catalogue is None:
            abort(HTTPStatus.NOT_FOUND)

        try:
            catalogue.name = data.get('name', catalogue.id)
            db.session.commit()
            observer = self.subject.find_observer(catalogue.id)
            if observer is None:
                observer = CatalogueObserverImpl(catalogue.id)
                self.subject.add_observer(observer)
            self.subject.notify_observers(catalogue)
            return catalogue
        except Exception as e:
            db.session.rollback()
            raise e

    def delete_catalogue(self, id):
        catalogue = self.get_catalogue(id)
        if catalogue is None:
            abort(HTTPStatus.NOT_FOUND)

        try:
            db.session.delete(catalogue)
            db.session.commit()
            self.subject.notify_observers(catalogue)
            self.subject.remove_observer(catalogue.id)
        except Exception as e:
            db.session.rollback()
            raise e
