import random
import uuid
from helpers.random_generator import generate_random_location
from logic.bacteria_strategies.random_strategy import random_strategy
from logic.bacteria_strategies.seek_food_strategy import seek_food_strategy
from models.bacteria import Bacteria
from models.bacteria_properties import BacteriaProperties
from project_types import Location


def get_random_bacterias(board_width, board_height, amount=10) -> list[tuple[Bacteria, Location]]:
    return [(Bacteria(uuid.uuid4(),
                      BacteriaProperties(
        "test_name", 4, 4, random.randint(
            1, 10), 30),
        seek_food_strategy
    ),
        generate_random_location(board_width, board_height))
        for _ in range(amount)]
