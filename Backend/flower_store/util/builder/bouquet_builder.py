from typing import List

from flower_store.model.catalogue import Catalogue
from flower_store.model.bouquet import Bouquet
from flower_store.model.flower import Flower
from flower_store.model.packing import Packing


class BouquetBuilder:
    def __init__(self):
        self._eventType = None
        self._price = None
        self._packing = None
        self._flowers = []
        self._catalogue=None

    def set_eventType(self, eventType: str) -> "BouquetBuilder":
        self._eventType = eventType
        return self

    def set_price(self, price: int) -> "BouquetBuilder":
        self._price = price
        return self

    def set_packing(self, packing: Packing) -> "BouquetBuilder":
        self._packing = packing
        return self

    def set_flowers(self, flowers: List[Flower]) -> "BouquetBuilder":
        self._flowers = flowers
        return self

    def set_catalogue(self, catalogue: Catalogue) -> "BouquetBuilder":
        self._catalogue = catalogue
        return self

    def build(self) -> "Bouquet":
        if None in [self._eventType, self._price, self._packing]:
            raise ValueError("EventType, price, and packing must be set")

        bouquet = Bouquet(eventType=self._eventType, price=self._price, packing=self._packing, catalogue=self._catalogue,
                          flowers=[])

        for flower in self._flowers:
            bouquet.flowers.append(flower)

        return bouquet
