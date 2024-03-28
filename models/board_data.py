from typing import Optional
from .bacteria import Bacteria
from .food import Food
from project_types import Location


class BoardData:
    """
    Represents the data of the game board.

    Args:
        width (int): The width of the game board.
        height (int): The height of the game board.
        bacterias (list[tuple[Bacteria, Location]], optional): The list of bacterias and their locations on the board. Defaults to an empty list.
        foods (list[tuple[Food, Location]], optional): The list of foods and their locations on the board. Defaults to an empty list.
        magic_door (Optional[tuple[Location, Location]], optional): The location of the magic door on the board. Defaults to None.
    """

    def __init__(self,
                 width: int,
                 height: int,
                 bacterias: list[tuple[Bacteria, Location]] = [],
                 foods: list[tuple[Food, Location]] = [],
                 magic_door: Optional[tuple[Location, Location]] = None):
        self.width = width
        self.height = height
        self.bacterias = bacterias
        self.foods = foods
        self.magic_door = magic_door
