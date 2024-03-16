from typing import Callable
from collections import defaultdict


class EventEmitter:
    def __init__(self):
        self.listeners: dict[str, list[Callable]] = defaultdict(list)

    def add_listener(self, event_name: str, listener: Callable):
        self.listeners[event_name].append(listener)

    def remove_listener(self, event_name: str, listener: Callable):
        self.listeners[event_name].remove(listener)

    def fire_event(self, event_name: str, data: any = None):
        for listener in self.listeners[event_name]:
            listener(data)
