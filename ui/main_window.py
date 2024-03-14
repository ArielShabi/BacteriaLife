from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

from logic.game_runner import ON_TURN_FINISHED, GameRunner
from ui.board_ui import BoardUi
from ui.toolbar_ui import ON_PLAY_PAUSE, ON_SPEED_CHANGE, ToolbarUI
from ui.utils import apply_style_sheet_file

CSS_FILE = "main_window.css"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.game = GameRunner()
        self.game.create_board()
        self.board_ui = BoardUi(self.game.board)
        self.toolbar = ToolbarUI()
        self.initUI()

        self.connect_events()

        self.board_ui.update_board(self.game.board)

    def initUI(self):
        self.setWindowTitle("Bacteria Game")
        apply_style_sheet_file(self, CSS_FILE)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        layout.addWidget(self.toolbar)
        layout.addWidget(self.board_ui, alignment=Qt.AlignCenter)

    def connect_events(self):
        self.game.add_listener(ON_TURN_FINISHED, self.board_ui.update_board)
        self.toolbar.add_listener(
            ON_PLAY_PAUSE, self.game.toggle_play_pause)
        self.toolbar.add_listener(ON_SPEED_CHANGE, self.game.change_speed)

        # self.toolbar_ui.add_listener(ON_SPEED_CHANGE, self.game.change_speed)
        # self.game.add_listener(ON_TURN_FINISHED, self.board_ui.update_board)
        # self.game.add_listener(ON_TURN_FINISHED, self.toolbar_ui.update_turn)
        # self.game.add_listener(ON_TURN_FINISHED, self.toolbar_ui.update_score)
        # self.game.add_listener(ON_TURN_FINISHED, self.toolbar_ui.update_speed)
