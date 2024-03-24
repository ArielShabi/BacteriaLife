

from typing import Optional
from const import DEFAULT_FOOD_PER_TURN, DEFAULT_MUTATION_RATE, START_BOARD_HEIGHT, START_BOARD_WIDTH
from project_types import Location


class Settings:
    def __init__(self,
                 board_size: tuple[int, int] = (
                     START_BOARD_WIDTH, START_BOARD_HEIGHT),
                 food_per_turn: int = DEFAULT_FOOD_PER_TURN,
                 mutation_rate: float = DEFAULT_MUTATION_RATE,
                 magic_door: Optional[tuple[Location, Location]] = None
                 ):
        self.board_size = board_size
        self.food_per_turn = food_per_turn
        self.mutation_rate = mutation_rate
        self.magic_door = magic_door
