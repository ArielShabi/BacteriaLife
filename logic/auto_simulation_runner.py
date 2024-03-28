from datetime import datetime
from PyQt5.QtCore import QThread, pyqtSignal
from logic.game_runner import GameRunner
from logic.history_saver import HistorySaver
from models.board import Board


class AutoSimulationRunner(QThread):
    """
    A class representing an automatic simulation runner.

    Args:
        game (GameRunner): The game runner object.
        history_saver (HistorySaver): The history saver object.
        start_amount (int): The starting turn number.
        until_turn (int): The ending turn number.

    Attributes:
        game (GameRunner): The game runner object.
        history_saver (HistorySaver): The history saver object.
        start_amount (int): The starting turn number.
        until_turn (int): The ending turn number.
        board (Board): The game board.

    Signals:
        finished (Board): A signal emitted when the simulation is finished.

    """

    def __init__(self, game: GameRunner, history_saver: HistorySaver, start_amount: int, until_turn: int):
        super().__init__()
        self.game = game
        self.history_saver = history_saver
        self.start_amount = start_amount
        self.until_turn = until_turn
        self.board = self.game.board

    finished = pyqtSignal(Board)

    def run(self) -> None:
        """
        Runs the automatic simulation.

        Returns:
            None

        """
        start = datetime.now()
        board = self.game.board
        for turn_number in range(self.start_amount, self.until_turn+1):
            board = self.game.turn_runner.run_turn(
                board, turn_number)

            if (len(board.bacterias) == 0):
                break

            self.history_saver.save_turn(board)

        self.game.live_turn_number = turn_number
        self.game.running_from_history = False

        print(f"Simulation finished in {datetime.now() - start}")

        self.finished.emit(board)
