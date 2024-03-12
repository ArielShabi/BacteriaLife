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

    bacteria_location = next((x, y)
                             for x in range(len(area_of_sense)) for y in range(len(area_of_sense[0]))
                             if isinstance(area_of_sense[x][y], BacteriaProperties) and area_of_sense[x][y].name == bacteria.name
                             )

    if (bacteria_location == None):
        # This should never happen
        return generate_random_vector(bacteria.speed)

    direction_vector = get_direction_vector(bacteria_location, food[0])

    distance = get_distance(bacteria_location, food[0])

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
