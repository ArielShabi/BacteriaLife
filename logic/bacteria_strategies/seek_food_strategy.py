from helpers.random_generator import generate_random_vector
from models.bacteria_properties import BacteriaProperties
from models.food import Food
from models.models_types import BoardObject
from project_types import Vector
from utils import get_direction_vector, get_distance, set_vector_length


def seek_food_strategy(area_of_sense: list[list[BoardObject]], bacteria: BacteriaProperties) -> Vector:
    food_locations = [(x, y) for x in range(len(area_of_sense)) for y in range(len(area_of_sense[0]))
                      if isinstance(area_of_sense[x][y], Food)
                      ]

    if (food_locations == []):
        return generate_random_vector(bacteria.speed)

    bacteria_location = next(((x, y)
                             for x in range(len(area_of_sense)) for y in range(len(area_of_sense[0]))
                             if (__check_bacteria(area_of_sense[x][y], bacteria))), None)

    if (bacteria_location is None):
        # This should never happen
        return generate_random_vector(bacteria.speed)

    closest_food = min(food_locations, key=lambda food_location: get_distance(
        bacteria_location, food_location))

    direction_vector = get_direction_vector(bacteria_location, closest_food)

    distance = get_distance(bacteria_location, closest_food)

    vector_length = min(bacteria.speed, distance)

    while (True):
        where_to_go = set_vector_length(direction_vector, vector_length)

        desired_cell = area_of_sense[where_to_go[0]+bacteria_location[0]
                                     ][where_to_go[1]+bacteria_location[1]]

        if ((not isinstance(desired_cell, BacteriaProperties)
                or desired_cell.name == bacteria.name)):
            break

        vector_length -= 1

    return where_to_go


def __check_bacteria(board_object: BoardObject, bacteria: BacteriaProperties) -> bool:
    if (isinstance(board_object, BacteriaProperties)):
        if board_object.name == bacteria.name:
            return True
    return False
