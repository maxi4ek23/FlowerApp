from typing import Optional

from flower_store.model.packing import Packing


class PackingBuilder:
    def __init__(self):
        self._name: Optional[str] = None
        self._price: Optional[int] = None

    def set_name(self, name: str):
        self._name = name
        return self

    def set_price(self, price: int):
        self._price = price
        return self

    def build(self) -> "Packing":
        if self._name is None or self._price is None:
            raise ValueError("Name and price must be set")
        return Packing(name=self._name, price=self._price)
