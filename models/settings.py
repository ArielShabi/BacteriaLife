

from const import DEFAULT_FOOD_PER_TURN


class Settings:
    def __init__(self, food_per_turn: int = DEFAULT_FOOD_PER_TURN):
        self.food_per_turn = food_per_turn
