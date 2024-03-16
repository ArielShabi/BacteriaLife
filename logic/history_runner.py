from typing import Union
from logic.history_saver import HistorySaver
from models.board import Board
from models.board_data import BoardData


class HistoryRunner:
    def __init__(self, history: HistorySaver):
        self.history = history
        self.turn = 1

    def get_turn(self, board: Board, increment_turn_counter=True) -> Union[Board, None]:
        if self.turn >= len(self.history.turns):
            return None
        past_board_data = self.history.get_turn(self.turn)
        board.load_board_data(past_board_data)
        if increment_turn_counter:
            self.turn += 1

        return board
