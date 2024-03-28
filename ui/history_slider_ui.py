from typing import Callable
from PyQt5.QtWidgets import QWidget, QSlider, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt
from logic.game_runner import ON_TURN_FINISHED, GameRunner
from logic.history_saver import HistorySaver
from models.board_data import BoardData
from ui.jump_to_turn_button import JumpToTurnButton
from ui.ui_utils import apply_style_sheet_file

CSS_FILES = [
    "filled_slider.css",
    "history_slider.css"
]

LABEL_WIDTH = 150


class HistorySliderUI(QWidget):
    """
    This class represents the UI component for the history slider.

    Args:
        history_saver (HistorySaver): The history saver object.
        game (GameRunner): The game runner object.
        update_board (Callable[[BoardData], None]): The callback function to update the board.

    Attributes:
        history_saver (HistorySaver): The history saver object.
        game (GameRunner): The game runner object.
        update_board (Callable[[BoardData], None]): The callback function to update the board.
        slider (QSlider): The slider widget.
        slider_label (QLabel): The label widget to display the current turn.
        goto_button (JumpToTurnButton): The button to jump to a specific turn.

    Signals:
        None

    """

    def __init__(self, history_saver: HistorySaver, game: GameRunner, update_board: Callable[[BoardData], None]):
        super().__init__()

        self.history_saver = history_saver
        self.game = game
        self.update_board = update_board
        self.initUI()

        self.game.add_listener(ON_TURN_FINISHED, self.__on_turn_finished)

    def initUI(self) -> None:
        """
        Initialize the UI components and layout.

        Returns:
            None

        """
        layout = QHBoxLayout(self)
        self.slider = QSlider(Qt.Orientation.Horizontal)

        self.slider.setRange(0, 0)
        self.slider.setValue(0)

        self.slider.sliderPressed.connect(self.__on_slider_pressed)
        self.slider.sliderMoved.connect(self.__on_slider_change)
        self.slider.sliderReleased.connect(self.__on_slider_released)

        self.slider_label = QLabel("0/0")
        self.slider_label.setFixedWidth(LABEL_WIDTH)
        self.slider_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.goto_button = JumpToTurnButton(
            self.slider.maximum, self.game, self.history_saver)

        layout.addWidget(self.slider)
        layout.addWidget(self.slider_label)
        layout.addWidget(self.goto_button)

        self.slider.enterEvent = lambda _: self.slider.setStyleSheet(  # type: ignore
            self.slider.styleSheet() +
            "QSlider::handle:horizontal {background-color: #0078D7;border-color: #0078D7;}"
        )

        self.slider.leaveEvent = lambda _: self.slider.setStyleSheet(  # type: ignore
            self.slider.styleSheet().replace(
                "QSlider::handle:horizontal {background-color: #0078D7;border-color: #0078D7;}", "")
        )

        self.setLayout(layout)
        apply_style_sheet_file(self, CSS_FILES)

    def __on_turn_finished(self, _: BoardData) -> None:
        """
        Callback function when a turn is finished.

        Args:
            _: The board data (not used).

        Returns:
            None

        """
        total_turns = self.game.live_turn_number
        current_turn = self.game.history_runner.turn if self.game.running_from_history else total_turns
        self.slider_label.setText(f"{current_turn}/{total_turns}")
        self.slider.setRange(0, total_turns)
        self.slider.setValue(current_turn)

    def __on_slider_pressed(self) -> None:
        """
        Callback function when the slider is pressed.

        Args:
            None

        Returns:
            None

        """
        self.__pause_value_before_slider_pressed = self.game.is_running
        self.game.toggle_play_pause(False)

    def __on_slider_change(self, value: int) -> None:
        """
        Callback function when the slider value is changed.

        Args:
            value (int): The new value of the slider.

        Returns:
            None

        """
        self.slider_label.setText(f"{value}/{self.slider.maximum()}")
        board = self.history_saver.get_turn(self.slider.value())
        self.update_board(board)

    def __on_slider_released(self) -> None:
        """
        Callback function when the slider is released.

        Args:
            None

        Returns:
            None

        """
        self.game.start_run_from_history(self.slider.value())
        self.game.toggle_play_pause(self.__pause_value_before_slider_pressed)

    def __enter_event(self) -> None:
        """
        Callback function when the mouse enters the slider.

        Args:
            None

        Returns:
            None

        """
        self.slider.setStyleSheet(
            self.slider.styleSheet() +
            "QSlider::handle:horizontal {background-color: #0078D7;border-color: #0078D7;}"
        )
