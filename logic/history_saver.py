import copy
from models.board import Board
from models.board_data import BoardData


class HistorySaver():
    def __init__(self):
        super().__init__()
        self.turns: list[BoardData] = []

    def save_turn(self, board: Board):
        self.turns.append(self.__get_board_data(board))

    def get_turn(self, turn: int) -> BoardData:
        return self.turns[turn]

    def __get_board_data(self, board: Board) -> BoardData:
        return BoardData(
            board.width,
            board.height,
            copy.deepcopy(board.bacterias),
            copy.deepcopy(board.foods),
            copy.deepcopy(board.magic_door)
        )