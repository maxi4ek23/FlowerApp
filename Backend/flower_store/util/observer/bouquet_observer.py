from typing import Dict, List


class BouquetObserver:
    def __init__(self, observer_id):
        self.observer_id = observer_id

    def update(self, bouquet):
        print("Bouquet updated")


class BouquetSubject:
    def __init__(self):
        self._observers: List[BouquetObserver] = []

    def add_observer(self, observer: BouquetObserver):
        self._observers.append(observer)

    def remove_observer(self, observer_id):
        for observer in self._observers:
            if observer.observer_id == observer_id:
                self._observers.remove(observer)
                break
    def find_observer(self, observer_id):
        for observer in self._observers:
            if observer.observer_id == observer_id:
                return observer
        return None
    def notify_observers(self, bouquet, action="updated"):
        for observer in self._observers:
            observer.update(bouquet, action)
