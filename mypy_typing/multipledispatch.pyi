
from typing import Any, Callable, TypeVar, Tuple

T = TypeVar('T')


class Dispatcher:
    def add(self, *types: Tuple[type]) -> Callable[[Callable[[Any], Any]], Callable[[Any], Any]]:
        ...


def dispatch(*types: type) -> Callable[[Callable[[Any], Any]], Callable[[Any], Any]]:
    ...
