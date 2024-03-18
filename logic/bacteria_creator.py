import random
import uuid
from const import MAX_BACTERIA_SENSE, MAX_BACTERIA_SPEED, START_ENERGY
from helpers.random_generator import generate_random_location
from logic.bacteria_strategies.random_strategy import random_strategy
from logic.bacteria_strategies.seek_food_strategy import seek_food_strategy
from models.bacteria import Bacteria
from models.bacteria_properties import BacteriaProperties
from project_types import Location


def get_random_bacterias(board_width, board_height, amount=10) -> list[tuple[Bacteria, Location]]:
    return [(Bacteria(uuid.uuid4(), START_ENERGY,
                      BacteriaProperties(
        f"name_{uuid.uuid4()}", random.randint(
            1, MAX_BACTERIA_SPEED), random.randint(
            1, MAX_BACTERIA_SENSE)),
        seek_food_strategy
    ),
        generate_random_location(board_width, board_height)
    )
        for _ in range(amount)]
