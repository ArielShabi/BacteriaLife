import random
from helpers.timer import Timer
from logic.bacteria_creator import get_random_bacterias
from logic.bacteria_strategies.random_strategy import random_strategy
from logic.event_emitter import EventEmitter
from logic.turn_runner import TurnRunner
from models.board import Board
from models.food import Food

BOARD_WIDTH = 100
BOARD_HEIGHT = 100

ON_TURN_FINISHED = "on_turn_finished"
TIMER_INTERVAL = 100


class GameRunner(EventEmitter):
    def __init__(self, time_per_turn=1):
        super().__init__()
        self.turn_runner = TurnRunner()
        self.time_per_turn = time_per_turn
        self.board = None
        self.timer: Timer = Timer(TIMER_INTERVAL)
        self.timer.timeout.connect(self.run_turn)

    def create_board(self):
        self.board = Board(BOARD_WIDTH, BOARD_HEIGHT)
        bacterias = get_random_bacterias(BOARD_WIDTH, BOARD_HEIGHT, 50)

        # for _ in range(8):
        #     self.board.add_food(Food("apple"), (random.randint(
        #         0, BOARD_WIDTH), random.randint(0, BOARD_HEIGHT)))

        self.board.add_food(Food("apple"), (BOARD_WIDTH-2, BOARD_HEIGHT-2))

        for bacteria, location in bacterias:
            self.board.add_bacteria(
                bacteria,
                location)

    def start(self):
        if not (self.timer and self.timer.is_alive()):
            self.fire_event(ON_TURN_FINISHED, self.board)
            self.timer.start()

    def pause(self):
        if (self.timer and self.timer.is_alive()):
            self.timer.stop()

    def run_turn(self):
        updated_board = self.turn_runner.run_turn(self.board)
        self.board = updated_board
        self.fire_event(ON_TURN_FINISHED, updated_board)