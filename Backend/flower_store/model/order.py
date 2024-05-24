from typing import Dict, List, Optional
from flower_store import db

from flower_store.model.bouquet import Bouquet
from flower_store.model.i_dto import IDto
from flower_store.util.observer.order_observer import OrderObserver


class Order(db.Model, IDto):
    __tablename__ = "order"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.Integer, nullable=False)
    deliveryType = db.Column(db.String(100), nullable=False)
    clientId = db.Column(db.Integer, nullable=False)
    bouquets = db.relationship('Bouquet', backref='order', lazy=True)

    def __init__(self, price: int, deliveryType: str, clientId: int, bouquets: List[Bouquet] = None):
        self.price = price
        self.deliveryType = deliveryType
        self.clientId = clientId
        self.bouquets = bouquets or []

    def getFullPrice(self) -> int:
        bouquets_sum = sum(bouquet.price for bouquet in self.bouquets)
        packing_sum = sum(bouquet.packing for bouquet in self.bouquets)
        return bouquets_sum + packing_sum

    def addItemToOrder(self, bouquet: Bouquet):
        self.bouquets.append(bouquet)

    def put_into_dto(self) -> Dict[str, object]:
        return {
            "id": self.id,
            "price": self.price,
            "deliveryType": self.deliveryType,
            "clientId": self.clientId,
            "bouquets": [bouquet.put_into_dto() for bouquet in self.bouquets]
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Optional[object]]) -> "Order":
        # Explicitly cast to the appropriate types
        price = int(dto_dict.get("price"))
        delivery_type = str(dto_dict.get("deliveryType"))
        client_id = int(dto_dict.get("clientId"))
        bouquets = [Bouquet.create_from_dto(bouquet_dto) for bouquet_dto in dto_dict.get("bouquets", []) if
                    bouquet_dto is not None]

        # Check if required fields are not None
        if None in [price, delivery_type, client_id]:
            raise ValueError("Required fields (price, deliveryType, clientId) cannot be None")

        order = Order(
            price=price,
            deliveryType=delivery_type,
            clientId=client_id,
            bouquets=bouquets
        )
        return order


class OrderObserverImpl(OrderObserver):
    def __init__(self, observer_id):
        self.observer_id = observer_id

    def update(self, order):
        print(f"Order updated: {order.price}, {order.id}")
