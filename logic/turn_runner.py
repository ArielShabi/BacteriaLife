import random
from helpers.random_generator import generate_random_location
from models.food import Food
import utils
from models.bacteria import Bacteria
from models.board import Board
from models.models_types import BoardObject
from project_types import Location


class TurnRunner:
    def __init__(self, food_per_turn) -> None:
        self.food_per_turn = food_per_turn
        self.x = False

    def run_turn(self, board: Board) -> Board:
        for bacteria, bacteria_locations in board.bacterias:
            bacteria_area_of_sense = self.__get_bacteria_area_of_sense(
                bacteria, bacteria_locations, board)
            direction = bacteria.play_turn(bacteria_area_of_sense)
            new_location = utils.sum_locations(
                bacteria_locations[0], direction)

            if (board.is_food(new_location)):
                food = board.remove_food(new_location)
                bacteria.energy += food.energy

            board.update_bacteria(bacteria.id, bacteria, new_location)

        self.__generate_food(board)
        return board

    def __generate_food(self, board: Board):
        board.foods = []

        food_placed = self.food_per_turn

        while (food_placed > 0):
            location = generate_random_location(board.width, board.height)

            if (not board.is_occupied(location)):
                board.add_food(Food("apple", 10), location)
                food_placed -= 1

    def __get_bacteria_area_of_sense(self, bacteria: Bacteria, bacteria_locations: list[Location], board: Board) -> list[list[BoardObject]]:
        start_location = utils.increase_location(
            bacteria_locations[0], -bacteria.properties.sense)

        max_location = (board.width-1, board.height-1)
        min_location = (0, 0)

        start_location = utils.clamp_location(
            start_location, min_location, max_location)

        end_location = utils.increase_location(
            bacteria_locations[-1], bacteria.properties.sense)

        end_location = utils.clamp_location(
            end_location, min_location, max_location)

        area_of_sense = [[
            board.get_cell_content((x, y))
            for y in range(start_location[1], end_location[1])
        ]
            for x in range(start_location[0], end_location[0])]

        return area_of_sense
