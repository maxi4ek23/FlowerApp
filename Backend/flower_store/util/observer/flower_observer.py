from typing import Dict, List


class FlowerObserver:
    def __init__(self, observer_id):
        self.observer_id = observer_id

    def update(self, flower):
        print("Flower updated")


class FlowerSubject:
    def __init__(self):
        self._observers: List[FlowerObserver] = []

    def add_observer(self, observer: FlowerObserver):
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


    def notify_observers(self, flower):
        for observer in self._observers:
            observer.update(flower)
