from typing import Callable
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QStyle, QApplication
from PyQt5.QtCore import Qt, QSize

from helpers.color import get_bacteria_color
from logic.bacteria_creator import get_random_bacteria
from logic.game_runner import ON_TURN_FINISHED, GameRunner
from logic.history_saver import HistorySaver
from models.board_data import BoardData
from ui.board_ui import BoardUi
from ui.history_slider_ui import HistorySliderUI
from ui.toolbar_ui import ToolbarUI
from ui.utils import apply_style_sheet_file, createColoredIcon

CSS_FILE = "main_window.css"


class SimulationPage(QWidget):
    def __init__(self, change_page: Callable, history_saver: HistorySaver, game: GameRunner):
        super().__init__()
        self.history_saver = history_saver
        self.game = game
        self.game.create_board()
        self.board_ui = BoardUi(self.game.board)
        self.toolbar = ToolbarUI(self.game)
        self.history_slider = HistorySliderUI(
            self.history_saver, self.game, self.board_ui.update_board)

        self.initUI()

        self.connect_events()

        self.toolbar.graph_button.clicked.connect(change_page)

        self.board_ui.update_board(self.game.board)

    def initUI(self):
        self.setWindowTitle("Bacteria Game")
        self.__set_icon()

        self.setGeometry(
            QStyle.alignedRect(
                Qt.LeftToRight,
                Qt.AlignCenter,
                QSize(1200, 900),
                QApplication.desktop().availableGeometry()
            )
        )
        apply_style_sheet_file(self, CSS_FILE)

        layout = QVBoxLayout(self)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.board_ui)
        layout.addWidget(self.history_slider)
        self.setLayout(layout)

    def connect_events(self):
        def on_turn_finished(board: BoardData):
            self.board_ui.update_board(board)

            if not self.game.running_from_history:
                self.history_saver.save_turn(board)

        self.game.add_listener(ON_TURN_FINISHED, on_turn_finished)

    def __set_icon(self):
        random_bacteria = get_random_bacteria()
        color = get_bacteria_color(random_bacteria.properties)
        self.setWindowIcon(createColoredIcon("assets/bacteria.svg", color))
