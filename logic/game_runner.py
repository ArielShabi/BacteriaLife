import random
from const import START_TIME_PER_TURN
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


class GameRunner(EventEmitter):
    def __init__(self, time_per_turn=1):
        super().__init__()
        self.turn_runner = TurnRunner(5)
        self.time_per_turn = time_per_turn
        self.board = None
        self.timer: Timer = Timer(START_TIME_PER_TURN)
        self.is_running = False
        self.timer.timeout.connect(self.run_turn)

    def create_board(self):
        self.board = Board(BOARD_WIDTH, BOARD_HEIGHT)
        bacterias = get_random_bacterias(BOARD_WIDTH, BOARD_HEIGHT, 30)

        for bacteria, location in bacterias:
            self.board.add_bacteria(
                bacteria,
                location)

    def toggle_play_pause(self, start: bool = True):
        if start:
            self.__start()
        else:
            self.__pause()
        self.is_running = start

    def change_speed(self, speed: int):
        self.time_per_turn = round(START_TIME_PER_TURN / speed)
        self.timer.interval = round(START_TIME_PER_TURN / speed)

        if (self.is_running):
            self.timer.stop()
            self.timer.start()

    def run_turn(self):
        updated_board = self.turn_runner.run_turn(self.board)
        self.board = updated_board
        self.fire_event(ON_TURN_FINISHED, updated_board)

    def __start(self):
        if not (self.is_running):
            self.fire_event(ON_TURN_FINISHED, self.board)
            self.timer.start()

    def __pause(self):
        if (self.is_running):
            self.timer.stop()
