from typing import Dict, List
from flask_socketio import SocketIO, emit
from flower_store import socketio

class BouquetObserver:
    def __init__(self, observer_id, sid):
        self.observer_id = observer_id
        self.sid = sid


    def update(self, bouquet, action="updated"):
        message = f"Bouquet {action}: {bouquet}"
        socketio.emit('bouquet_update', message, room=self.sid)
    # def update(self, bouquet):
    #     print("Bouquet updated")


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
