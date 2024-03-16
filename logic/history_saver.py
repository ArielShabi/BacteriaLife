from models.board_data import BoardData


class HistorySaver():
    def __init__(self):
        self.turns: list[BoardData] = []

    def save_turn(self, board: BoardData):
        self.turns.append(board)

    def get_turn(self, turn: int) -> BoardData:
        return self.turns[turn]
