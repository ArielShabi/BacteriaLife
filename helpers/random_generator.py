import random

from project_types import Location, Vector

VECTOR_SIZE = 2


def generate_random_location(width: int, height: int) -> Location:
    return (random.randint(0, width - 1), random.randint(0, height - 1))


def generate_random_vector(amplitude: int) -> Vector:
    return tuple([random.randint(-amplitude, amplitude) for _ in range(VECTOR_SIZE)])
