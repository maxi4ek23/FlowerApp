from typing import Dict, List
from flask_socketio import SocketIO, emit
from flower_store import socketio


class PackingObserver:
    def __init__(self, observer_id):
        self.observer_id = observer_id

    def update(self, packing, action="updated"):
        message = f"Packing {action}: {packing}"
        socketio.emit('packing_update', message, room=self.sid)


class PackingSubject:
    def __init__(self):
        self._observers: List[PackingObserver] = []

    def add_observer(self, observer: PackingObserver):
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
    def notify_observers(self, packing, action="updated"):
        for observer in self._observers:
            observer.update(packing, action)
