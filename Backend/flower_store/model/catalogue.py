from typing import Dict, List
from flower_store import db
from flower_store.model.i_dto import IDto
from flower_store.util.observer.catalogue_observer import CatalogueObserver


class Catalogue(db.Model, IDto):
    __tablename__ = "catalogue"
    __table_args__ = {'extend_existing': True}
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(100), nullable=False)

    def __init__(self, bouquets: List, name: str):
        self.name = name
        self.bouquets = bouquets

    def notify(self):
        self._notify_observers()

    def put_into_dto(self) -> Dict[str, object]:
        return {
            "name": self.name,
            "bouquets": [bouquet.put_into_dto() for bouquet in self.bouquets]
        }

    def put_into_dto_excluding_bouquets(self) -> Dict[str, object]:
        return {
            "name": self.name
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> object:
        from Backend.flower_store.model.bouquet import Bouquet
        catalogue = Catalogue()
        catalogue.bouquets = [Bouquet.create_from_dto(bouquet_dto) for bouquet_dto in dto_dict.get("bouquets", [])]
        return catalogue


class CatalogueObserverImpl(CatalogueObserver):
    def __init__(self, observer_id):
        self.observer_id = observer_id

    def update(self, flower):
        print(f"Flower updated: {flower.name}, {flower.color}, {flower.price}")
