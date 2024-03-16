from typing import Union
from models.bacteria import Bacteria
from models.bacteria_properties import BacteriaProperties
from models.board_data import BoardData
from models.food import Food
from models.models_types import BoardObject
from project_types import Location


class Board(BoardData):
    def get_cell_content(self, location: Location) -> BoardObject:
        if (self.__is_out_of_bounds(location)):
            return None
        bacteria_content = next((bacteria for bacteria, bacteria_location
                                in self.bacterias if location == bacteria_location), None)

        if (bacteria_content):
            return bacteria_content.properties

        food_content = next(
            (food for food, loc in self.foods if loc == location), None)

        if (food_content):
            return food_content

        return None

    def add_bacteria(self, bacteria: Bacteria, start_location: Location) -> bool:
        if (self.is_occupied(start_location)) or (self.__is_out_of_bounds(start_location)):
            return False

        self.bacterias.append((bacteria, start_location))
        return True

    def remove_bacteria(self, bacteria_id) -> bool:
        self.bacterias = [(b, locations)
                          for b, locations in self.bacterias if b.id != bacteria_id]
        return True

    def load_board_data(self, board_data: BoardData) -> None:
        self.width = board_data.width
        self.height = board_data.height
        self.bacterias = board_data.bacterias
        self.foods = board_data.foods

    def add_food(self, food, location: Location) -> bool:
        if self.__is_out_of_bounds(location) or self.is_occupied([location]):
            return False
        self.foods.append((food, location))
        return True

    def remove_food(self, location: Location) -> Union[Food, None]:
        food = next((f for f, loc in self.foods if loc == location), None)
        self.foods = [(f, loc) for f, loc in self.foods if loc != location]

        return food

    def update_bacteria(self, bacteria_id: str, bacteria: Bacteria, new_location: Location) -> bool:
        if self.__is_out_of_bounds(new_location) or self.is_occupied(new_location, bacteria):
            return False
        self.remove_bacteria(bacteria_id)
        self.bacterias.append((bacteria, new_location))
        return True

    def is_occupied(self, locations: Location, bacteria: Bacteria = None) -> bool:
        occupied_by_bacteria = any([locations == occupied_location
                                    for bacteria, occupied_location in self.bacterias
                                    if bacteria != bacteria
                                    ])

        occupied_by_food = any(
            [locations == food_loc for _, food_loc in self.foods])

        return occupied_by_food or occupied_by_bacteria

    def __is_out_of_bounds(self, location: Location) -> bool:
        return location[0] < 0 or location[0] >= self.width or location[1] < 0 or location[1] >= self.height

    def is_food(self, location: Location) -> bool:
        return location in [loc for _, loc in self.foods]
