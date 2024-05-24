from typing import Dict, List


class OrderObserver:
    def __init__(self, observer_id):
        self.observer_id = observer_id

    def update(self, order):
        print("Order updated")


class OrderSubject:
    def __init__(self):
        self._observers: List[OrderObserver] = []

    def add_observer(self, observer: OrderObserver):
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

    def notify_observers(self, order):
        for observer in self._observers:
            observer.update(order)
