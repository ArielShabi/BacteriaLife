import random

from project_types import Location, Vector
from utils import set_vector_length

VECTOR_SIZE = 2


def generate_random_location(width: int, height: int) -> Location:
    return (random.randint(0, height - 1), random.randint(0, width - 1))


def generate_random_vector(amplitude: int) -> Vector:
    direction = (random.randint(-1, 1), random.randint(-1, 1))
    return set_vector_length(direction, amplitude)


def random_event_occurred(change_rate: float) -> bool:
    return random.random() < change_rate


def alter_value(value: int, change_value: int, min_value: int, max_value: int) -> int:
    while True:
        new_value = value + random.randint(-change_value, change_value)
        if new_value >= min_value and new_value <= max_value and new_value != value:
            return new_value
