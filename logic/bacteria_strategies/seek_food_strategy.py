from helpers.random_generator import generate_random_vector
from models.bacteria_properties import BacteriaProperties
from models.food import Food
from models.models_types import BoardObject
from project_types import Vector
from utils import get_direction_vector, get_distance, set_vector_length


def seek_food_strategy(area_of_sense: list[list[BoardObject]], bacteria: BacteriaProperties) -> Vector:
    food = [(x, y) for x in range(len(area_of_sense)) for y in range(len(area_of_sense[0]))
            if isinstance(area_of_sense[x][y], Food)
            ]

    if (food == []):
        return generate_random_vector(bacteria.speed)

    bacteria_location = (len(area_of_sense) // 2, len(area_of_sense[0]) // 2)

    vector = get_direction_vector(bacteria_location, food[0])

    distance = get_distance(bacteria_location, food[0])

    return set_vector_length(vector, min(bacteria.speed, distance))
