import random

from project_types import Location, Vector
from utils import set_vector_length

VECTOR_SIZE = 2


def generate_random_location(width: int, height: int) -> Location:
    """
    Generate a random location within the given width and height.

    Args:
        width (int): The width of the area.
        height (int): The height of the area.

    Returns:
        Location: A tuple representing the random location (x, y).
    """
    return (random.randint(0, height - 1), random.randint(0, width - 1))


def generate_random_vector(amplitude: int) -> Vector:
    """
    Generate a random vector with the given amplitude.

    Args:
        amplitude (int): The amplitude of the vector.

    Returns:
        Vector: A tuple representing the random vector (x, y).
    """
    direction = (random.randint(-1, 1), random.randint(-1, 1))
    return set_vector_length(direction, amplitude)


def random_event_occurred(change_rate: float) -> bool:
    """
    Check if a random event occurred based on the given change rate.

    Args:
        change_rate (float): The probability of a random event occurring.

    Returns:
        bool: True if a random event occurred, False otherwise.
    """
    return random.random() < change_rate


def alter_value(value: int, change_value: int, min_value: int, max_value: int) -> int:
    """
    Alter a value by adding a random change value within the specified range.

    Args:
        value (int): The original value.
        change_value (int): The maximum absolute change value.
        min_value (int): The minimum value the altered value can have.
        max_value (int): The maximum value the altered value can have.

    Returns:
        int: The altered value.
    """
    while True:
        new_value = value + random.randint(-change_value, change_value)
        if new_value >= min_value and new_value <= max_value and new_value != value:
            return new_value
