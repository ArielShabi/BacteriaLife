import copy
from models.board import Board
from models.board_data import BoardData


class HistorySaver():
    """
    A class that represents a history saver for a board game.

    Args:
        None

    Attributes:
        turns (list[BoardData]): A list to store the history of board data.

    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the HistorySaver class.

        Args:
            None

        Returns:
            None

        """
        super().__init__()
        self.turns: list[BoardData] = []

    def save_turn(self, board: BoardData) -> None:
        """
        Saves the current turn's board data to the history.

        Args:
            board (BoardData): The board data to be saved.

        Returns:
            None

        """
        self.turns.append(self.__get_board_data(board))

    def get_turn(self, turn: int) -> BoardData:
        """
        Retrieves the board data for a specific turn.

        Args:
            turn (int): The turn number.

        Returns:
            BoardData: The board data for the specified turn.

        """
        return self.turns[turn]
    
    def clear_history(self) -> None:
        """
        Clears the history of board data.

        Args:
            None

        Returns:
            None

        """
        self.turns = []

    def __get_board_data(self, board: BoardData) -> BoardData:
        """
        Creates a deep copy of the board data.

        Args:
            board (BoardData): The board data to be copied.

        Returns:
            BoardData: A deep copy of the board data.

        """
        return BoardData(
            board.width,
            board.height,
            copy.deepcopy(board.bacterias),
            copy.deepcopy(board.foods),
            copy.deepcopy(board.magic_door)
        )
