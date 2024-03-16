from models.bacteria import Bacteria
from models.food import Food
from project_types import Location


class BoardData:
    def __init__(self,
                 width: int,
                 height: int,
                 bacterias: list[tuple[Bacteria, Location]] = [],
                 foods: list[tuple[Food, Location]] = []
                 ):
        self.width = width
        self.height = height
        self.bacterias = bacterias
        self.foods = foods
