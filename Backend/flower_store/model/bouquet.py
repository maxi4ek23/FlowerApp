from typing import Dict, List
from flower_store import db

from flower_store.model.catalogue import Catalogue
from flower_store.model.flower import Flower
from flower_store.model.i_dto import IDto
from flower_store.model.packing import Packing
from flower_store.util.observer.bouquet_observer import BouquetObserver


class Bouquet(db.Model, IDto):
    __tablename__ = "bouquet"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    eventType: str = db.Column(db.String(100), nullable=False)
    price: int = db.Column(db.Integer, nullable=False)
    packing_id: int = db.Column(db.Integer, db.ForeignKey('packing.id'), nullable=False)
    packing = db.relationship('Packing')
    catalogue_id = db.Column(db.Integer, db.ForeignKey('catalogue.id'))
    catalogue = db.relationship('Catalogue', backref='bouquets')
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=True)
    flowers = db.relationship('Flower', backref='bouquet', lazy=True)

    def __init__(self, eventType: str, price: int, packing: Packing, catalogue: Catalogue, flowers: List[Flower]):
        self.eventType = eventType
        self.price = price
        self.packing = packing
        self.catalogue = catalogue
        self.flowers = flowers

    def calculatePrice(self) -> int:
        flowers_price = sum(flower.price for flower in self.flowers)
        packing_price = self.packing.price
        return flowers_price + packing_price

    def put_into_dto(self) -> Dict[str, object]:
        return {
            "id": self.id,
            "eventType": self.eventType,
            "price": self.price,
            "packing": self.packing.put_into_dto() if self.packing else {},
            "catalogue": self.catalogue.put_into_dto_excluding_bouquets() if self.catalogue else {},
            "flowers": [flower.put_into_dto() for flower in self.flowers]
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> object:
        bouquet = Bouquet(
            eventType=dto_dict.get("eventType"),
            price=dto_dict.get("price"),
            packing=Packing.create_from_dto(dto_dict.get("packing"))
        )
        bouquet.flowers = [Flower.create_from_dto(flower_dto) for flower_dto in dto_dict.get("flowers", [])]
        return bouquet


class BouquetObserverImpl(BouquetObserver):
    def __init__(self, observer_id):
        self.observer_id = observer_id

    def update(self, bouquet, action):
        if action == "deleted":
            print(f"Bouquet deleted: {bouquet.name}, {bouquet.color}, {bouquet.price}")
        elif action == "created":
            print(f"Bouquet created: {bouquet.name}, {bouquet.color}, {bouquet.price}")
        else:
            print(f"Bouquet updated: {bouquet.name}, {bouquet.color}, {bouquet.price}")
        # print(f"Flower updated: {bouquet.eventType}, {bouquet.price}")
