from typing import Any, Callable
from collections import defaultdict


class EventEmitter:
    """
    A class that represents an event emitter.

    Attributes:
        listeners (dict[str, list[Callable[[Any], Any]]]): A dictionary that maps event names to a list of listeners.

    Methods:
        add_listener(event_name: str, listener: Callable[[Any], Any]) -> None:
            Adds a listener function to the specified event.

        remove_listener(event_name: str, listener: Callable[[Any], Any]) -> None:
            Removes a listener function from the specified event.

        fire_event(event_name: str, data: Any = None) -> None:
            Fires an event by calling all the listener functions associated with the event.
    """

    def __init__(self) -> None:
        """
        Initializes an instance of the EventEmitter class.
        """
        self.listeners: dict[str, list[Callable[[Any], Any]]] = defaultdict(list)

    def add_listener(self, event_name: str, listener: Callable[[Any], Any]) -> None:
        """
        Adds a listener function to the specified event.

        Args:
            event_name (str): The name of the event.
            listener (Callable[[Any], Any]): The listener function to be added.

        Returns:
            None
        """
        self.listeners[event_name].append(listener)

    def remove_listener(self, event_name: str, listener: Callable[[Any], Any]) -> None:
        """
        Removes a listener function from the specified event.

        Args:
            event_name (str): The name of the event.
            listener (Callable[[Any], Any]): The listener function to be removed.

        Returns:
            None
        """
        self.listeners[event_name].remove(listener)

    def fire_event(self, event_name: str, data: Any = None) -> None:
        """
        Fires an event by calling all the listener functions associated with the event.

        Args:
            event_name (str): The name of the event.
            data (Any, optional): The data to be passed to the listener functions. Defaults to None.

        Returns:
            None
        """
        for listener in self.listeners[event_name]:
            listener(data)
