from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

from logic.game_runner import ON_TURN_FINISHED, GameRunner
from ui.board_ui import BoardUi
from ui.toolbar_ui import ToolbarUI
from ui.utils import apply_style_sheet_file

CSS_FILE = "main_window.css"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        game = GameRunner()
        game.create_board()
        self.game = game
        self.board_ui = BoardUi(self.game.board)
        game.add_listener(ON_TURN_FINISHED, self.board_ui.update_board)
        self.initUI()
        self.board_ui.update_board(self.game.board)
        # game.start()

    def initUI(self):
        self.setWindowTitle("Bacteria Game")
        apply_style_sheet_file(self, CSS_FILE)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        toolbar = ToolbarUI()

        layout.addWidget(toolbar)
        layout.addWidget(self.board_ui, alignment=Qt.AlignCenter)
