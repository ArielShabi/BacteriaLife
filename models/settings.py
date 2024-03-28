

from typing import Optional
from const import (DEFAULT_FOOD_PER_TURN, DEFAULT_MUTATION_RATE,
                   START_BOARD_HEIGHT, START_BOARD_WIDTH)
from project_types import Location


class Settings:
    """Represents the settings for the Bacteria Simulation.

    Args:
        board_size (tuple[int, int], optional): The size of the game board. Defaults to (START_BOARD_WIDTH, START_BOARD_HEIGHT).
        food_per_turn (float, optional): The amount of food generated per turn. Defaults to DEFAULT_FOOD_PER_TURN.
        mutation_rate (float, optional): The mutation rate for bacteria. Defaults to DEFAULT_MUTATION_RATE.
        magic_door (Optional[tuple[Location, Location]], optional): The locations of the magic door. Defaults to None.
    """

    def __init__(self,
                 board_size: tuple[int, int] = (
                     START_BOARD_WIDTH, START_BOARD_HEIGHT),
                 food_per_turn: float = DEFAULT_FOOD_PER_TURN,
                 mutation_rate: float = DEFAULT_MUTATION_RATE,
                 magic_door: Optional[tuple[Location, Location]] = None
                 ):
        """Initializes a new instance of the Settings class.

        Args:
            board_size (tuple[int, int], optional): The size of the game board. Defaults to (START_BOARD_WIDTH, START_BOARD_HEIGHT).
            food_per_turn (float, optional): The amount of food generated per turn. Defaults to DEFAULT_FOOD_PER_TURN.
            mutation_rate (float, optional): The mutation rate for bacteria. Defaults to DEFAULT_MUTATION_RATE.
            magic_door (Optional[tuple[Location, Location]], optional): The locations of the magic door. Defaults to None.
        """
        self.board_size = board_size
        self.food_per_turn = food_per_turn
        self.mutation_rate = mutation_rate
        self.magic_door = magic_door
