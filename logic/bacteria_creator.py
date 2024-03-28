import random
import uuid
from const import MAX_BACTERIA_SENSE, MAX_BACTERIA_SPEED, START_ENERGY
from helpers.random_generator import generate_random_location
from logic.bacteria_strategies.seek_food_strategy import seek_food_strategy
from models.bacteria import Bacteria
from models.bacteria_properties import BacteriaProperties
from project_types import Location


def get_random_bacterias(board_width: int, board_height: int, amount: int = 10) -> list[tuple[Bacteria, Location]]:
    """
    Generate a list of random bacterias with their corresponding locations.

    Args:
        board_width (int): The width of the game board.
        board_height (int): The height of the game board.
        amount (int, optional): The number of bacterias to generate. Defaults to 10.

    Returns:
        list[tuple[Bacteria, Location]]: A list of tuples containing a random bacteria and its location.
    """
    return [(get_random_bacteria(),
             generate_random_location(board_width, board_height)
             )
            for _ in range(amount)]


def get_random_bacteria() -> Bacteria:
    """
    Generate a random bacteria.

    Returns:
        Bacteria: A randomly generated bacteria object.
    """
    return Bacteria(str(uuid.uuid4()), START_ENERGY,
                    BacteriaProperties(
        f"name_{uuid.uuid4()}", random.randint(
            1, MAX_BACTERIA_SPEED), random.randint(
            1, MAX_BACTERIA_SENSE)),
        seek_food_strategy
    )
