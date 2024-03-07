from models.bacteria import Bacteria
from models.models_types import Board_Object
from project_types import Location


class Board:
    def __init__(self, width: int, height: int):
        self.width: int = width
        self.height: int = height
        self.bacterias: list[tuple[Bacteria, list[Location]]] = []

    def get_cell_content(self, location: Location) -> Board_Object:
        if (self.is_out_of_bounds(location)):
            return None
        return [bacteria for bacteria, locations in self.bacterias if location in locations]

    def add_bacteria(self, bacteria, start_location: Location) -> bool:
        bacteria_locations = [(x, y) for x in range(start_location[0], start_location[0] + bacteria.width)
                              for y in range(start_location[1], start_location[1] + bacteria.height)]

        if (any([bacteria_location in occupied_location
                 for occupied_location in self.bacterias
                 for bacteria_location in bacteria_locations
                 ])):
            return False

        self.bacterias.append((bacteria, bacteria_locations))
        return True

    def remove_bacteria(self, bacteria_id) -> bool:
        self.bacterias = [b for b in self.bacterias if b.id != bacteria_id]
        return True

    def update_bacteria(self, bacteria_id: str, bacteria: Bacteria, new_location: Location) -> bool:
        self.remove_bacteria(bacteria_id)
        return self.add_bacteria(bacteria, new_location)

    def is_out_of_bounds(self, location: Location) -> bool:
        return location[0] < 0 or location[0] >= self.width or location[1] < 0 or location[1] >= self.height
