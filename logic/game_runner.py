import uuid
from helpers.timer import Timer
from logic.event_emitter import EventEmitter
from logic.turn_runner import TurnRunner
from models.bacteria import Bacteria, BacteriaProperties
from models.board import Board
from random_generator import generate_random_location

BOARD_WIDTH = 100
BOARD_HEIGHT = 100

ON_TURN_FINISHED = "on_turn_finished"
TIMER_INTERVAL = 1000


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
        for i in range(50):
            self.board.add_bacteria(
                Bacteria(uuid.uuid4(), "test_name", 4, 4, BacteriaProperties(4)), generate_random_location(BOARD_WIDTH, BOARD_HEIGHT))

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
