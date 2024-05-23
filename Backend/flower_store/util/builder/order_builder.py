from typing import List

from flower_store.model.bouquet import Bouquet
from flower_store.model.order import Order


class OrderBuilder:
    def __init__(self):
        self._price = None
        self._deliveryType = None
        self._clientId = None
        self._bouquets = []

    def set_price(self, price: int):
        self._price = price
        return self

    def set_deliveryType(self, deliveryType: str):
        self._deliveryType = deliveryType
        return self

    def set_clientId(self, clientId: int):
        self._clientId = clientId
        return self

    def add_bouquet(self, bouquet: Bouquet):
        self._bouquets.append(bouquet)
        return self

    def build(self):
        if self._price is None or self._deliveryType is None or self._clientId is None:
            raise ValueError("Price, DeliveryType, and ClientId must be set")
        return Order(
            price=self._price,
            deliveryType=self._deliveryType,
            clientId=self._clientId,
            bouquets=self._bouquets
        )

    def prepareOrder(self, price: int, delivery_type: str, client_id: int, bouquets: List[Bouquet]) -> Order:
        order = Order(
            price=price,
            deliveryType=delivery_type,
            clientId=client_id
        )

        if bouquets:
            for bouquet in bouquets:
                order.addItemToOrder(bouquet)

        return order
