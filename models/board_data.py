from .bacteria import Bacteria
from .food import Food
from project_types import Location


class BoardData:
    def __init__(self,
                 width: int,
                 height: int,
                 bacterias: list[tuple[Bacteria, Location]] = [],
                 foods: list[tuple[Food, Location]] = [],
                 magic_door: Location = None):
        self.width = width
        self.height = height
        self.bacterias = bacterias
        self.foods = foods
        self.magic_door = magic_door
