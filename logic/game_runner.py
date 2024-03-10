from logic.turn_runner import TurnRunner
from models.bacteria import Bacteria, BacteriaProperties
from models.board import Board
from random_generator import generate_random_location

BOARD_WIDTH = 500
BOARD_HEIGHT = 500

class GameRunner:
    def __init__(self):
        self.turn_runner = TurnRunner()

    def create_board(self):
        self.board = Board(BOARD_WIDTH, BOARD_HEIGHT)
        for i in range(10):
            self.board.add_bacteria(
                Bacteria("test", "test_name", 2, 2, BacteriaProperties()), generate_random_location(BOARD_WIDTH, BOARD_HEIGHT))
