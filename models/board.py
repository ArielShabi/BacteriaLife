from typing import Union
from .bacteria import Bacteria
from .board_data import BoardData
from .food import Food
from .models_types import BoardObject
from project_types import Location


class Board(BoardData):
    def __init__(self,
                 width: int,
                 height: int,
                 bacterias: list[tuple[Bacteria, Location]] = [],
                 foods: list[tuple[Food, Location]] = []) -> None:
        super().__init__(width, height, bacterias, foods)

        self.cells: list[list[BoardObject]] = []

        self.__init_cells()

    def get_cell_content(self, location: Location) -> BoardObject:
        if (self.__is_out_of_bounds(location)):
            return None

        return self.cells[location[1]][location[0]]

    def add_bacteria(self, bacteria: Bacteria, start_location: Location) -> bool:
        if (self.is_occupied(start_location)):
            return False

        self.bacterias.append((bacteria, start_location))
        self.cells[start_location[1]][start_location[0]] = bacteria.properties
        return True

    def remove_bacteria(self, bacteria_id: str) -> bool:
        found_index, location = next(((index, loc) for index, (bacteria, loc) in enumerate(
            self.bacterias) if bacteria.id == bacteria_id), (None, None))

        if found_index is None or location is None:
            return False

        del self.bacterias[found_index]

        self.cells[location[1]][location[0]] = None
        return True

    def resize(self, new_width: int, new_height: int) -> None:
        width_diff = new_width - self.width
        height_diff = new_height - self.height

        self.width = new_width
        self.height = new_height

        if width_diff > 0:
            for row in self.cells:
                row.extend([None for _ in range(width_diff)])

        elif width_diff < 0:
            for row in self.cells:
                row = row[:new_width]

        if height_diff > 0:
            self.cells.extend([[None for _ in range(new_width)]
                              for _ in range(height_diff)])
        elif height_diff < 0:
            self.cells = self.cells[:new_height]

        if width_diff < 0 or height_diff < 0:
            self.bacterias = [(bacteria, location) for bacteria,
                              location in self.bacterias if location[0] < new_width and location[1] < new_height]
            self.foods = [(food, location) for food, location in self.foods if location[0]
                          < new_width and location[1] < new_height]

    def load_board_data(self, board_data: BoardData) -> None:
        self.width = board_data.width
        self.height = board_data.height
        self.bacterias = board_data.bacterias
        self.foods = board_data.foods

        self.__init_cells()

    def add_food(self, food: Food, location: Location) -> bool:
        if self.is_occupied(location):
            return False
        self.foods.append((food, location))
        self.cells[location[1]][location[0]] = food
        return True

    def remove_food(self, location: Location) -> Union[Food, None]:
        (food, index) = next(((f, index) for index, (f, loc)
                              in enumerate(self.foods) if loc == location), (None, None))

        if food is None or index is None:
            return None

        del self.foods[index]
        self.cells[location[1]][location[0]] = None

        return food

    def update_bacteria(self, bacteria_id: str, bacteria: Bacteria, new_location: Location) -> bool:
        if self.is_occupied(new_location):
            return False

        self.remove_bacteria(bacteria_id)
        self.add_bacteria(bacteria, new_location)

        return True

    def is_occupied(self, location: Location) -> bool:
        return self.__is_out_of_bounds(location) or self.get_cell_content(location) is not None

    def __is_out_of_bounds(self, location: Location) -> bool:
        return location[0] < 0 or location[0] >= self.width or location[1] < 0 or location[1] >= self.height

    def __init_cells(self) -> None:
        self.cells = [
            [None for _ in range(self.width)] for _ in range(self.height)
        ]

        for self.bacteria, location in self.bacterias:
            self.cells[location[1]][location[0]] = self.bacteria.properties
        for food, location in self.foods:
            self.cells[location[1]][location[0]] = food
