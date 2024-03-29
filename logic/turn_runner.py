import copy
import math
import uuid
from const import ENERGY_FOR_FOOD, MAX_BACTERIA_SENSE, MAX_BACTERIA_SPEED, START_BOARD_SIZE, START_ENERGY, MUTATION_CHANGE
from helpers.random_generator import alter_value, generate_random_location, random_event_occurred
from models.bacteria_properties import BacteriaProperties
from models.food import Food
from models.settings import Settings
import utils
from models.bacteria import Bacteria
from models.board import Board
from models.models_types import BoardObject
from project_types import Location


class TurnRunner:
    """
    The TurnRunner class is responsible for running a single turn of the bacteria simulation.

    Args:
        settings (Settings): The settings object containing the simulation parameters.

    Attributes:
        settings (Settings): The settings object containing the simulation parameters.
    """

    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    def run_turn(self, board: Board, turn_number: int) -> Board:
        """
        Runs a single turn of the bacteria simulation.

        Args:
            board (Board): The current state of the game board.
            turn_number (int): The current turn number.

        Returns:
            Board: The updated game board after the turn.
        """
        self.__generate_food(board, turn_number)
        self.__play_bacterias(board)
        self.__duplicate_bacterias(board)
        self.__natural_selection(board)

        return board

    def __play_bacterias(self, board: Board) -> None:
        """
        Plays the turn for each bacteria on the board.

        Args:
            board (Board): The current state of the game board.
        """
        sorted_by_speed = sorted(
            board.bacterias, key=lambda bacteria_and_location: bacteria_and_location[0].properties.speed, reverse=True)

        for bacteria, bacteria_location in sorted_by_speed:
            bacteria_area_of_sense = self.__get_bacteria_area_of_sense(
                bacteria, bacteria_location, board)
            direction = bacteria.play_turn(bacteria_area_of_sense)
            new_location = utils.sum_locations(
                bacteria_location, direction)

            new_location = self.__check_magic_portal(
                board, bacteria_location, new_location)

            new_location_content = board.get_cell_content(new_location)

            if (isinstance(new_location_content, Food)):
                food = board.remove_food(new_location)
                if (food is None):
                    continue
                bacteria.energy += food.energy

            bacteria.energy -= bacteria.energy_per_turn()

            if not isinstance(new_location_content, BacteriaProperties):
                board.update_bacteria(bacteria.id, bacteria, new_location)

    def __generate_food(self, board: Board, turn_number: int) -> None:
        """
        Generates food on the board based on the current turn number and settings.

        Args:
            board (Board): The current state of the game board.
            turn_number (int): The current turn number.
        """
        food_per_turn = self.settings.food_per_turn

        if food_per_turn < 1 and turn_number % int(1/(food_per_turn)) != 0:
            return

        food_placed = math.ceil(food_per_turn)

        board_size = board.width * board.height

        board_size_ratio = board_size / START_BOARD_SIZE

        food_placed = round(food_placed * board_size_ratio)

        while (food_placed > 0):
            location = generate_random_location(board.width, board.height)

            if (not board.is_occupied(location)):
                board.add_food(Food(ENERGY_FOR_FOOD), location)
                food_placed -= 1

    def __duplicate_bacterias(self,  board: Board) -> None:
        """
        Duplicates bacteria on the board if they have enough energy.

        Args:
            board (Board): The current state of the game board.
        """
        for bacteria, _ in board.bacterias:
            if bacteria.energy < START_ENERGY * 2:
                continue

            child_bacteria = copy.deepcopy(bacteria)
            child_bacteria.energy = START_ENERGY
            child_bacteria.id = str(uuid.uuid4())
            child_bacteria.properties.name = f"""{
                bacteria.properties.name} c """
            bacteria.energy -= START_ENERGY
            while True:
                location = generate_random_location(board.width, board.height)
                if not board.is_occupied(location):
                    break
            self.__mutate_bacteria(child_bacteria)
            board.add_bacteria(child_bacteria, location)

    def __get_bacteria_area_of_sense(self, bacteria: Bacteria, bacteria_location: Location, board: Board) -> list[list[BoardObject]]:
        """
        Gets the area of sense for a bacteria on the board.

        Args:
            bacteria (Bacteria): The bacteria object.
            bacteria_location (Location): The current location of the bacteria.
            board (Board): The current state of the game board.

        Returns:
            list[list[BoardObject]]: The 2D list representing the area of sense for the bacteria.
        """
        start_location = utils.increase_location(
            bacteria_location, -bacteria.properties.sense)

        max_location = (board.width-1, board.height-1)
        min_location = (0, 0)

        start_location = utils.clamp_location(
            start_location, min_location, max_location)

        end_location = utils.increase_location(
            bacteria_location, bacteria.properties.sense)

        end_location = utils.clamp_location(
            end_location, min_location, max_location)

        area_of_sense = [[
            board.get_cell_content((x, y))
            for y in range(start_location[1], end_location[1]+1)
        ]
            for x in range(start_location[0], end_location[0]+1)]

        return area_of_sense

    def __mutate_bacteria(self, bacteria: Bacteria) -> None:
        """
        Mutates the properties of a bacteria based on the mutation rate.

        Args:
            bacteria (Bacteria): The bacteria object.
        """
        mutation_rate = self.settings.mutation_rate

        if random_event_occurred(mutation_rate):
            bacteria.properties.speed = alter_value(
                bacteria.properties.speed, MUTATION_CHANGE, 1, MAX_BACTERIA_SPEED)
            bacteria.properties.sense = alter_value(
                bacteria.properties.sense, MUTATION_CHANGE, 1, MAX_BACTERIA_SENSE)

    def __natural_selection(self, board: Board) -> None:
        """
        Performs natural selection by removing bacteria with zero or negative energy from the board.

        Args:
            board (Board): The current state of the game board.
        """
        for bacteria, _ in board.bacterias:
            if bacteria.energy <= 0:
                board.remove_bacteria(bacteria.id)

    def __check_magic_portal(self, board: Board, bacteria_location: Location, new_location: Location) -> Location:
        """
        Checks if the bacteria's movement crosses the magic portal and updates the new location accordingly.

        Args:
            board (Board): The current state of the game board.
            bacteria_location (Location): The current location of the bacteria.
            new_location (Location): The new location of the bacteria.

        Returns:
            Location: The updated new location of the bacteria.
        """
        if board.magic_door and utils.is_point_on_line(bacteria_location, new_location, board.magic_door[0]):
            return board.magic_door[1]
        return new_location
