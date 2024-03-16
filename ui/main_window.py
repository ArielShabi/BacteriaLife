from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QStyle, QApplication
from PyQt5.QtCore import Qt, QSize

from logic.game_runner import ON_TURN_FINISHED, GameRunner
from logic.history_saver import HistorySaver
from ui.board_ui import BoardUi
from ui.history_slider_ui import HistorySliderUI
from ui.toolbar_ui import ON_PLAY_PAUSE, ON_SETTINGS_CHANGE, ON_SPEED_CHANGE, ToolbarUI
from ui.utils import apply_style_sheet_file

CSS_FILE = "main_window.css"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.game = GameRunner()
        self.game.create_board()
        self.board_ui = BoardUi(self.game.board)
        self.toolbar = ToolbarUI(self.game.settings)
        self.history_saver = HistorySaver()
        self.initUI()

        self.connect_events()

        self.board_ui.update_board(self.game.board)

    def initUI(self):
        self.setWindowTitle("Bacteria Game")
        self.setGeometry(
            QStyle.alignedRect(
                Qt.LeftToRight,
                Qt.AlignCenter,
                QSize(1200, 900),
                QApplication.desktop().availableGeometry()
            )
        )
        apply_style_sheet_file(self, CSS_FILE)
        
        history_slider = HistorySliderUI()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        layout.addWidget(self.toolbar)
        layout.addWidget(self.board_ui)
        layout.addWidget(history_slider)
        

    def connect_events(self):
        self.game.add_listener(ON_TURN_FINISHED, self.board_ui.update_board)
        self.game.add_listener(ON_TURN_FINISHED, self.history_saver.save_turn)
        self.toolbar.add_listener(
            ON_PLAY_PAUSE, self.game.toggle_play_pause)
        self.toolbar.add_listener(ON_SPEED_CHANGE, self.game.change_speed)
        self.toolbar.add_listener(
            ON_SETTINGS_CHANGE, self.game.on_settings_change)
