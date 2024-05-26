from typing import Dict, List
from flower_store import db
from flower_store.model.i_dto import IDto
from flower_store.util.observer.flower_observer import FlowerObserver


class Flower(db.Model, IDto):
    __tablename__ = "flower"
    __table_args__ = {'extend_existing': True}
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(100), nullable=False)
    color: str = db.Column(db.String(50), nullable=False)
    price: int = db.Column(db.Integer, nullable=False)
    bouquet_id: int = db.Column(db.Integer, db.ForeignKey('bouquet.id'), nullable=False)

    def __init__(self, name: str, color: str, price: int):
        self.name = name
        self.color = color
        self.price = price

    def put_into_dto(self) -> Dict[str, object]:
        return {
            "name": self.name,
            "color": self.color,
            "price": self.price
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> object:
        return Flower(
            name=dto_dict.get("name"),
            color=dto_dict.get("color"),
            price=dto_dict.get("price")
        )


class FlowerObserverImpl(FlowerObserver):
    def __init__(self, observer_id):
        self.observer_id = observer_id

    def update(self, flower, action):
        if action == "deleted":
            print(f"Flower deleted: {flower.name}, {flower.color}, {flower.price}")
        elif action == "created":
            print(f"Flower created: {flower.name}, {flower.color}, {flower.price}")
        else:
            print(f"Flower updated: {flower.name}, {flower.color}, {flower.price}")
        # print(f"Flower updated: {flower.name}, {flower.color}, {flower.price}")
