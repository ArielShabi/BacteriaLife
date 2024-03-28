from typing import Callable, Optional
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSpinBox, QDialog, QLabel, QHBoxLayout
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QMovie

from const import BUTTON_SIZE
from logic.auto_simulation_runner import AutoSimulationRunner
from logic.game_runner import GameRunner
from logic.history_saver import HistorySaver
from models.board import Board

DEFAULT_MAX = 3000
LOADING_GIF = "assets/Hourglass.gif"


class JumpToTurnButton(QWidget):
    """
    A custom widget representing a button that allows the user to jump to a specific turn in a game simulation.

    Args:
        get_min_value (Callable[[], int]): A function that returns the minimum value for the turn.
        game (GameRunner): An instance of the GameRunner class.
        history_saver (HistorySaver): An instance of the HistorySaver class.

    Attributes:
        get_min_value (Callable[[], int]): A function that returns the minimum value for the turn.
        game (GameRunner): An instance of the GameRunner class.
        history_saver (HistorySaver): An instance of the HistorySaver class.
        worker (Optional[AutoSimulationRunner]): An optional instance of the AutoSimulationRunner class.
        button (QPushButton): The button widget.
        popover_dialog (QDialog): The dialog widget for the popover.
        input_label (QLabel): The label widget for displaying instructions.
        spin_box (QSpinBox): The spin box widget for selecting the turn.
        loading_label (QLabel): The label widget for displaying a loading animation.

    Signals:
        simulation_finished (board: Board): A signal emitted when the simulation is finished.

    """

    def __init__(self, get_min_value: Callable[[], int], game: GameRunner, history_saver: HistorySaver):
        """
        Initializes the JumpToTurnButton widget.

        Args:
            get_min_value (Callable[[], int]): A function that returns the minimum value for the turn.
            game (GameRunner): An instance of the GameRunner class.
            history_saver (HistorySaver): An instance of the HistorySaver class.

        """
        super().__init__()

        layout = QVBoxLayout(self)

        self.get_min_value = get_min_value
        self.game = game
        self.history_saver = history_saver
        self.worker: Optional[AutoSimulationRunner] = None

        self.button = QPushButton()
        self.button.setIcon(QIcon("assets/hourglass.svg"))
        self.button.setFixedSize(QSize(BUTTON_SIZE, BUTTON_SIZE))

        layout.addWidget(self.button)

        self.__init_popover()

        self.button.clicked.connect(self.open_popover)

    def __init_popover(self) -> None:
        """
        Initializes the popover dialog.

        """
        self.__pause_value_before_slider_pressed = False

        self.popover_dialog: QDialog = QDialog(self)
        self.popover_dialog.setWindowTitle("Go to Turn")

        layout = QVBoxLayout(self.popover_dialog)

        self.input_label: QLabel = QLabel("Here you can go to any turn in the Future!\n" +
                                          "The program will simulate the turns until the turn you want to go to.")
        self.input_label.setWordWrap(True)
        self.input_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.input_label)

        self.spin_box: QSpinBox = QSpinBox()

        self.loading_label: QLabel = QLabel(self)
        self.loading_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.loading_label)
        layout.addWidget(self.spin_box)

        self.loading_label.hide()

        buttons_layout = QHBoxLayout()
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.accept_input)
        buttons_layout.addWidget(ok_button)

        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.cancel_input)
        buttons_layout.addWidget(cancel_button)

        self.popover_dialog.finished.connect(self.__on_window_closed)

        layout.addLayout(buttons_layout)

    def open_popover(self) -> None:
        """
        Opens the popover dialog.

        """
        self.__pause_value_before_slider_pressed = self.game.is_running
        self.game.toggle_play_pause(False)

        self.spin_box.setMinimum(self.get_min_value()+1)
        self.spin_box.setMaximum(DEFAULT_MAX)

        self.popover_dialog.exec_()

    def accept_input(self) -> None:
        """
        Accepts the user input and starts the simulation.

        """
        self.run_simulation()

    def cancel_input(self) -> None:
        """
        Cancels the user input and terminates the simulation if running.

        """
        self.popover_dialog.reject()

        if self.worker:
            self.worker.terminate()

    def show_loading_gif(self) -> None:
        """
        Shows the loading GIF animation and hides other widgets.

        """
        self.loading_label.setMovie(QMovie(LOADING_GIF))
        movie = self.loading_label.movie()

        if movie is None:
            return

        movie.start()

        self.input_label.hide()
        self.spin_box.hide()

        self.loading_label.show()

    def run_simulation(self) -> None:
        """
        Runs the simulation until the selected turn.

        """
        until_turn = self.spin_box.value()
        start = self.get_min_value()

        self.show_loading_gif()

        self.worker = AutoSimulationRunner(
            self.game, self.history_saver, start, until_turn)
        self.worker.finished.connect(self.simulation_finished)
        self.worker.start()

    def simulation_finished(self, board: Board) -> None:
        """
        Updates the game board with the simulation result and accepts the popover dialog.

        Args:
            board (Board): The updated game board.

        """
        self.game.update_board(board)
        if self.popover_dialog:
            self.popover_dialog.accept()

    def __on_window_closed(self, result: int) -> None:
        """
        Restores the play/pause state of the game and cleans up after the popover dialog is closed.

        Args:
            result (int): The result code of the dialog.

        """
        self.game.toggle_play_pause(self.__pause_value_before_slider_pressed)
        self.worker = None
        self.loading_label.hide()
        self.input_label.show()
        self.spin_box.show()
