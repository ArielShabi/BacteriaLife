from PyQt5.QtWidgets import QWidget, QSlider, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt

from logic.game_runner import ON_TURN_FINISHED, GameRunner
from logic.history_saver import HistorySaver
from ui.utils import apply_style_sheet_file

CSS_FILES = [
    "filled_slider.css",
    "history_slider.css"
]

LABEL_WIDTH = 150


class HistorySliderUI(QWidget):
    def __init__(self, history_saver: HistorySaver, game: GameRunner, update_board: callable):
        super().__init__()

        self.history_saver = history_saver
        self.game = game
        self.update_board = update_board
        self.initUI()

        self.game.add_listener(ON_TURN_FINISHED, self.__on_turn_finished)

    def initUI(self):
        layout = QHBoxLayout(self)
        self.slider = QSlider(Qt.Horizontal)

        self.slider.setRange(1, 1)
        self.slider.setValue(1)

        self.slider.sliderPressed.connect(self.__on_slider_pressed)
        self.slider.sliderMoved.connect(self.__on_slider_change)
        self.slider.sliderReleased.connect(self.__on_slider_released)

        self.slider_label = QLabel("0/0")
        self.slider_label.setFixedWidth(LABEL_WIDTH)
        self.slider_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.slider)
        layout.addWidget(self.slider_label)

        self.slider.enterEvent = lambda _: self.slider.setStyleSheet(
            self.slider.styleSheet() +
            "QSlider::handle:horizontal {background-color: #0078D7;border-color: #0078D7;}"
        )

        self.slider.leaveEvent = lambda _: self.slider.setStyleSheet(
            self.slider.styleSheet().replace(
                "QSlider::handle:horizontal {background-color: #0078D7;border-color: #0078D7;}", "")
        )

        self.setLayout(layout)
        apply_style_sheet_file(self, CSS_FILES)

    def __on_turn_finished(self, _):
        total_turns = self.game.live_turn_number
        current_turn = self.game.history_runner.turn if self.game.running_from_history else total_turns
        self.slider_label.setText(f"{current_turn}/{total_turns}")
        self.slider.setRange(0, total_turns)
        self.slider.setValue(current_turn)

    def __on_slider_pressed(self):
        self.__pause_value_before_slider_pressed = self.game.is_running
        self.game.toggle_play_pause(False)

    def __on_slider_change(self, value: int):
        self.slider_label.setText(f"{value}/{self.slider.maximum()}")
        self.update_board(self.game.board)

    def __on_slider_released(self):
        self.game.start_run_from_history(self.slider.value())
        self.game.toggle_play_pause(self.__pause_value_before_slider_pressed)
