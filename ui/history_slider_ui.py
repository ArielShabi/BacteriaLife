from PyQt5.QtWidgets import QWidget, QSlider, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt

from logic.event_emitter import EventEmitter
from logic.game_runner import GameRunner
from logic.history_saver import ON_TURN_SAVED, HistorySaver
from ui.utils import apply_style_sheet_file

CSS_FILE = "history_slider.css"

LABEL_WIDTH = 150

ON_HISTORY_SLIDER_CHANGE = "on_history_slider_change"
ON_HISTORY_SLIDER_RELEASED = "on_history_slider_released"


class HistorySliderUI(QWidget):
    def __init__(self, history_saver: HistorySaver, game: GameRunner):
        super().__init__()

        self.history_saver = history_saver
        self.game = game
        self.turn = 0
        self.initUI()

        self.history_saver.add_listener(
            ON_TURN_SAVED, self.__on_turn_saved)

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

        self.setLayout(layout)
        apply_style_sheet_file(self, CSS_FILE)

    def __on_turn_saved(self, _):
        total_turns = len(self.history_saver.turns)
        self.slider_label.setText(f"{total_turns}/{total_turns}")
        self.slider.setRange(1, total_turns)
        self.slider.setValue(total_turns)

    def __on_slider_pressed(self):
        self.__pause_value_before_slider_pressed = self.game.is_running
        self.game.toggle_play_pause(False)

    def __on_slider_change(self, value: int):
        self.slider_label.setText(f"{value}/{self.slider.maximum()}")
        self.game.start_run_from_history(value - 1)

    def __on_slider_released(self):
        self.game.toggle_play_pause(self.__pause_value_before_slider_pressed)
