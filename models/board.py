from models.bacteria import Bacteria
from models.bacteria_properties import BacteriaProperties
from models.food import Food
from models.models_types import BoardObject
from project_types import Location


class Board:
    def __init__(self, width: int, height: int):
        self.width: int = width
        self.height: int = height
        self.bacterias: list[tuple[Bacteria, list[Location]]] = []
        self.foods: list[tuple[Food, Location]] = []

    def get_cell_content(self, location: Location) -> BoardObject:
        if (self.is_out_of_bounds(location)):
            return None
        bacteria_content = [bacteria for bacteria,
                            locations in self.bacterias if location in locations]

        if (bacteria_content):
            return bacteria_content[0].properties

        food_content = [food for food, loc in self.foods if loc == location]

        if (food_content):
            return food_content[0]

        return None

    def add_bacteria(self, bacteria: Bacteria, start_location: Location) -> bool:
        bacteria_locations = self.__get_bacteria_location(
            start_location, bacteria.properties)

        if (self.__is_occupied(bacteria_locations)) or (self.__is_any_out_of_bounds(bacteria_locations)):
            return False

        self.bacterias.append((bacteria, bacteria_locations))
        return True

    def remove_bacteria(self, bacteria_id) -> bool:
        self.bacterias = [(b, locations)
                          for b, locations in self.bacterias if b.id != bacteria_id]
        return True

    def add_food(self, food, location: Location) -> bool:
        if self.is_out_of_bounds(location) or self.__is_occupied([location]):
            return False
        self.foods.append((food, location))
        return True

    def remove_food(self, location: Location) -> bool:
        food_amount = len(self.foods)
        self.foods = [(f, loc) for f, loc in self.foods if loc != location]

        if len(self.foods) == food_amount:
            return False

        return True

    def update_bacteria(self, bacteria_id: str, bacteria: Bacteria, new_location: Location) -> bool:
        bacteria_locations: list[Location] = self.__get_bacteria_location(
            new_location, bacteria.properties)

        if self.__is_any_out_of_bounds(bacteria_locations) or self.__is_occupied(bacteria_locations, bacteria):
            return False
        self.remove_bacteria(bacteria_id)
        self.bacterias.append((bacteria, bacteria_locations))
        return True

    def is_out_of_bounds(self, location: Location) -> bool:
        return location[0] < 0 or location[0] >= self.width or location[1] < 0 or location[1] >= self.height

    def __get_bacteria_location(self, start_location: Location, bacteria: BacteriaProperties) -> list[Location]:
        return [(x, y) for x in range(start_location[0], start_location[0] + bacteria.width)
                for y in range(start_location[1], start_location[1] + bacteria.height)]

    def __is_any_out_of_bounds(self, location: list[Location]) -> bool:
        return any([self.is_out_of_bounds(loc) for loc in location])

    def __is_occupied(self, locations: list[Location], bacteria: Bacteria = None) -> bool:
        other_bacterias = [
            bacterias for bacterias in self.bacterias if bacterias[0] != bacteria]
        food = [food_loc for _, food_loc in self.foods if food_loc in locations]
        return food or any([bacteria_location in occupied_location
                            for _, occupied_location in other_bacterias
                            for bacteria_location in locations
                            ])
