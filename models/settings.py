

from const import DEFAULT_FOOD_PER_TURN, DEFAULT_MUTATION_RATE


class Settings:
    def __init__(self, food_per_turn: int = DEFAULT_FOOD_PER_TURN, mutation_rate: float = DEFAULT_MUTATION_RATE):
        self.food_per_turn = food_per_turn
        self.mutation_rate = mutation_rate
