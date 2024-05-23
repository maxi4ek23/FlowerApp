from typing import Dict, List


class CatalogueObserver:
    def __init__(self, observer_id):
        self.observer_id = observer_id

    def update(self, catalogue):
        print("Catalogue updated")


class CatalogueSubject:
    def __init__(self):
        self._observers: List[CatalogueObserver] = []

    def add_observer(self, observer: CatalogueObserver):
        self._observers.append(observer)

    def find_observer(self, observer_id):
        for observer in self._observers:
            if observer.observer_id == observer_id:
                return observer
        return None

    def remove_observer(self, observer_id):
        for observer in self._observers:
            if observer.observer_id == observer_id:
                self._observers.remove(observer)
                break

    def notify_observers(self, catalogue):
        for observer in self._observers:
            observer.update(catalogue)
