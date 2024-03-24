from typing import Any, Callable
from collections import defaultdict


class EventEmitter:
    def __init__(self) -> None:
        self.listeners: dict[str,
                             list[Callable[[Any], Any]]] = defaultdict(list)

    def add_listener(self, event_name: str, listener: Callable[[Any], Any]):
        self.listeners[event_name].append(listener)

    def remove_listener(self, event_name: str, listener: Callable[[Any], Any]):
        self.listeners[event_name].remove(listener)

    def fire_event(self, event_name: str, data: Any = None):
        for listener in self.listeners[event_name]:
            listener(data)
