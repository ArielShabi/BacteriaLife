import copy
from logic.event_emitter import EventEmitter
from models.board import Board
from models.board_data import BoardData

ON_TURN_SAVED = "on_turn_saved"


class HistorySaver(EventEmitter):
    def __init__(self):
        super().__init__()
        self.turns: list[BoardData] = []

    def save_turn(self, board: Board):
        self.turns.append(self.__get_board_data(board))
        self.fire_event(ON_TURN_SAVED, board)

    def get_turn(self, turn: int) -> BoardData:
        return self.turns[turn]

    def __get_board_data(self, board: Board) -> BoardData:
        return BoardData(
            board.width,
            board.height,
            copy.deepcopy(board.bacterias),
            copy.deepcopy(board.foods)
        )
