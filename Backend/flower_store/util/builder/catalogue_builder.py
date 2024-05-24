from flower_store.model.catalogue import Catalogue

class CatalogueBuilder:
    def __init__(self):
        self._name = ""
        self._bouquets = []

    def set_name(self, name):
        self._name = name
        return self

    def set_bouquets(self, bouquets):
        self._bouquets = bouquets
        return self

    def build(self):
        return Catalogue(
            bouquets=self._bouquets, name=self._name
        )
