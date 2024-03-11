from helpers.random_generator import generate_random_vector
from models.bacteria_properties import BacteriaProperties
from models.models_types import BoardObject
from project_types import Vector


def random_strategy(area_of_sense: list[list[BoardObject]], bacteria: BacteriaProperties) -> Vector:
    return generate_random_vector(bacteria.speed)
