from models.bacteria import Bacteria
from models.food import Food
from project_types import Location


class BoardData:
    def __init__(self, width: int, height: int):
        self.width: int = width
        self.height: int = height
        self.bacterias: list[tuple[Bacteria, Location]] = []
        self.foods: list[tuple[Food, Location]] = []
