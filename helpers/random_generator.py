import random

from project_types import Location, Vector
from utils import set_vector_length

VECTOR_SIZE = 2


def generate_random_location(width: int, height: int) -> Location:
    return (random.randint(0, width - 1), random.randint(0, height - 1))


def generate_random_vector(amplitude: int) -> Vector:
    direction = tuple([random.randint(-1, 1) for _ in range(VECTOR_SIZE)])
    return set_vector_length(direction, amplitude)
