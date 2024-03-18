import copy
import math
import uuid
from const import ENERGY_FOR_FOOD, START_ENERGY
from helpers.random_generator import generate_random_location
from models.food import Food
import utils
from models.bacteria import Bacteria
from models.board import Board
from models.models_types import BoardObject
from project_types import Location


class TurnRunner:
    def __init__(self, food_per_turn: int) -> None:
        self.food_per_turn = food_per_turn

    def run_turn(self, board: Board, turn_number: int) -> Board:
        self.__generate_food(board, turn_number)
        self.__play_bacterias(board)
        self.__duplicate_bacterias(board)
        self.__natural_selection(board)

        return board

    def __play_bacterias(self, board: Board):
        sorted_by_speed = sorted(
            board.bacterias, key=lambda bacteria_and_location: bacteria_and_location[0].properties.speed, reverse=True)

        for bacteria, bacteria_location in sorted_by_speed:
            bacteria_area_of_sense = self.__get_bacteria_area_of_sense(
                bacteria, bacteria_location, board)
            direction = bacteria.play_turn(bacteria_area_of_sense)
            new_location = utils.sum_locations(
                bacteria_location, direction)

            new_location_content = board.get_cell_content(new_location)

            if (isinstance(new_location_content, Food)):
                food = board.remove_food(new_location)
                bacteria.energy += food.energy

            bacteria.energy -= bacteria.energy_per_turn()

            if new_location_content is None:
                board.update_bacteria(bacteria.id, bacteria, new_location)

    def __generate_food(self, board: Board, turn_number: int):
        # if food_per_turn is a fraction, we will generate food every 1/food_per_turn turns
        if self.food_per_turn < 1 and turn_number % int(1/(self.food_per_turn)) != 0:
            return

        food_placed = math.ceil(self.food_per_turn)

        while (food_placed > 0):
            location = generate_random_location(board.width, board.height)

            if (not board.is_occupied(location)):
                board.add_food(Food("apple", ENERGY_FOR_FOOD), location)
                food_placed -= 1

    def __duplicate_bacterias(self,  board: Board):
        for bacteria, _ in board.bacterias:
            if bacteria.energy < START_ENERGY * 2:
                continue

            child_bacteria = copy.deepcopy(bacteria)
            child_bacteria.energy = START_ENERGY
            child_bacteria.id = uuid.uuid4()
            child_bacteria.properties.name = f"{
                bacteria.properties.name} c "
            bacteria.energy -= START_ENERGY
            while True:
                location = generate_random_location(board.width, board.height)
                if not board.is_occupied(location):
                    break
            board.add_bacteria(child_bacteria, location)

    def __get_bacteria_area_of_sense(self, bacteria: Bacteria, bacteria_location: Location, board: Board) -> list[list[BoardObject]]:
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

    def __natural_selection(self, board: Board):
        for bacteria, _ in board.bacterias:
            if bacteria.energy <= 0:
                board.remove_bacteria(bacteria.id)
