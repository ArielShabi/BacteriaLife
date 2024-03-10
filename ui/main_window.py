from PyQt5.QtWidgets import QMainWindow

from logic.game_runner import ON_TURN_FINISHED, GameRunner
from ui.board_ui import BoardUi


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        game = GameRunner()
        game.create_board()
        self.game = game
        self.board_ui = BoardUi(self.game.board)
        game.add_listener(ON_TURN_FINISHED, self.board_ui.update_board)
        self.initUI()
        game.start()

    def initUI(self):
        self.setWindowTitle("Smooth Button Movement")
        self.setCentralWidget(self.board_ui)
