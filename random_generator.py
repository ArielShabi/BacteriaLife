import random

from project_types import Vector

VECTOR_SIZE = 2


def generate_random_vector(amplitude: int) -> Vector:
    return [random.randint(-amplitude, amplitude) for _ in range(VECTOR_SIZE)]
