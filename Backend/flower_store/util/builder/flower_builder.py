from flower_store.model.flower import Flower


class FlowerBuilder:
    def __init__(self):
        self._name = None
        self._color = None
        self._price = None

    def set_name(self, name):
        self._name = name
        return self

    def set_color(self, color):
        self._color = color
        return self

    def set_price(self, price):
        self._price = price
        return self

    def build(self):
        return Flower(
            name=self._name,
            color=self._color,
            price=self._price
        )
