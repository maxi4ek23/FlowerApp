from typing import Dict
from flower_store import db
from flower_store.model.i_dto import IDto
from flower_store.util.observer.packing_observer import PackingObserver


class Packing(db.Model, IDto):
    __tablename__ = "packing"
    __table_args__ = {'extend_existing': True}
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(100), nullable=False)
    price: int = db.Column(db.Integer, nullable=False)

    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def put_into_dto(self) -> Dict[str, object]:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> object:
        return Packing(
            name=dto_dict.get("name"),
            price=dto_dict.get("price")
        )


class PackingObserverImpl(PackingObserver):
    def __init__(self, observer_id):
        self.observer_id = observer_id

    def update(self, packing):
        print(f"Flower updated: {packing.name}, {packing.price}")
