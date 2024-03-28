from typing import Union
from .bacteria import Bacteria
from .board_data import BoardData
from .food import Food
from .models_types import BoardObject
from project_types import Location


class Board(BoardData):
    """
    Represents a game board for the Bacteria Simulation.

    Args:
        width (int): The width of the board.
        height (int): The height of the board.
        bacterias (list[tuple[Bacteria, Location]], optional): The initial list of bacterias and their locations on the board. Defaults to an empty list.
        foods (list[tuple[Food, Location]], optional): The initial list of foods and their locations on the board. Defaults to an empty list.
    """

    def __init__(self,
                 width: int,
                 height: int,
                 bacterias: list[tuple[Bacteria, Location]] = [],
                 foods: list[tuple[Food, Location]] = []) -> None:
        super().__init__(width, height, bacterias, foods)

        self.cells: list[list[BoardObject]] = []

        self.__init_cells()

    def get_cell_content(self, location: Location) -> BoardObject:
        """
        Get the content of a cell at the specified location.

        Args:
            location (Location): The location of the cell.

        Returns:
            BoardObject: The content of the cell.
        """
        if (self.__is_out_of_bounds(location)):
            return None

        return self.cells[location[1]][location[0]]

    def add_bacteria(self, bacteria: Bacteria, start_location: Location) -> bool:
        """
        Add a bacteria to the board at the specified location.

        Args:
            bacteria (Bacteria): The bacteria to add.
            start_location (Location): The location to add the bacteria.

        Returns:
            bool: True if the bacteria was successfully added, False otherwise.
        """
        if (self.is_occupied(start_location)):
            return False

        self.bacterias.append((bacteria, start_location))
        self.cells[start_location[1]][start_location[0]] = bacteria.properties
        return True

    def remove_bacteria(self, bacteria_id: str) -> bool:
        """
        Remove a bacteria from the board based on its ID.

        Args:
            bacteria_id (str): The ID of the bacteria to remove.

        Returns:
            bool: True if the bacteria was successfully removed, False otherwise.
        """
        found_index, location = next(((index, loc) for index, (bacteria, loc) in enumerate(
            self.bacterias) if bacteria.id == bacteria_id), (None, None))

        if found_index is None or location is None:
            return False

        del self.bacterias[found_index]

        self.cells[location[1]][location[0]] = None
        return True

    def resize(self, new_width: int, new_height: int) -> None:
        """
        Resize the board to the specified width and height.

        Args:
            new_width (int): The new width of the board.
            new_height (int): The new height of the board.
        """
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
        """
        Load board data from a BoardData object.

        Args:
            board_data (BoardData): The BoardData object to load data from.
        """
        self.width = board_data.width
        self.height = board_data.height
        self.bacterias = board_data.bacterias
        self.foods = board_data.foods

        self.__init_cells()

    def add_food(self, food: Food, location: Location) -> bool:
        """
        Add a food to the board at the specified location.

        Args:
            food (Food): The food to add.
            location (Location): The location to add the food.

        Returns:
            bool: True if the food was successfully added, False otherwise.
        """
        if self.is_occupied(location):
            return False
        self.foods.append((food, location))
        self.cells[location[1]][location[0]] = food
        return True

    def remove_food(self, location: Location) -> Union[Food, None]:
        """
        Remove a food from the board at the specified location.

        Args:
            location (Location): The location of the food to remove.

        Returns:
            Union[Food, None]: The removed food if successful, None otherwise.
        """
        (food, index) = next(((f, index) for index, (f, loc)
                              in enumerate(self.foods) if loc == location), (None, None))

        if food is None or index is None:
            return None

        del self.foods[index]
        self.cells[location[1]][location[0]] = None

        return food

    def update_bacteria(self, bacteria_id: str, bacteria: Bacteria, new_location: Location) -> bool:
        """
        Update the location of a bacteria on the board.

        Args:
            bacteria_id (str): The ID of the bacteria to update.
            bacteria (Bacteria): The updated bacteria object.
            new_location (Location): The new location of the bacteria.

        Returns:
            bool: True if the bacteria was successfully updated, False otherwise.
        """
        if self.is_occupied(new_location):
            return False

        self.remove_bacteria(bacteria_id)
        self.add_bacteria(bacteria, new_location)

        return True

    def is_occupied(self, location: Location) -> bool:
        """
        Check if a cell at the specified location is occupied.

        Args:
            location (Location): The location to check.

        Returns:
            bool: True if the cell is occupied, False otherwise.
        """
        return self.__is_out_of_bounds(location) or self.get_cell_content(location) is not None

    def clear_board(self) -> None:
        """
        Clear the board by removing all bacterias and foods.
        """
        self.bacterias = []
        self.foods = []
        self.__init_cells()

    def __is_out_of_bounds(self, location: Location) -> bool:
        """
        Check if a location is out of bounds of the board.

        Args:
            location (Location): The location to check.

        Returns:
            bool: True if the location is out of bounds, False otherwise.
        """
        return location[0] < 0 or location[0] >= self.width or location[1] < 0 or location[1] >= self.height

    def __init_cells(self) -> None:
        """
        Initialize the cells of the board with None values.
        """
        self.cells = [
            [None for _ in range(self.width)] for _ in range(self.height)
        ]

        for self.bacteria, location in self.bacterias:
            self.cells[location[1]][location[0]] = self.bacteria.properties
        for food, location in self.foods:
            self.cells[location[1]][location[0]] = food
