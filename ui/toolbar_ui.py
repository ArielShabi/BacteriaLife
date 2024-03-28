from typing import Callable
from PyQt5.QtWidgets import QPushButton, QWidget, QHBoxLayout, QSlider, QDialog, QSizePolicy, QSpacerItem
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import QSize, Qt

from const import BUTTON_SIZE, DEFAULT_FOOD_PER_TURN, DEFAULT_MUTATION_RATE
from logic.game_runner import ON_PAUSE_PLAY_TOGGLE, GameRunner
from logic.history_saver import HistorySaver
from models.board_data import BoardData
from ui.components.slider_with_icon import SliderWithButton
from ui.components.uneven_step_slider import UnevenStepSlider
from ui.settings_modal import SettingsModal
from ui.ui_utils import apply_style_sheet_file

CSS_FILES = [
    "filled_slider.css",
    "toolbar.css",
]

SLIDER_SIZE = 200
MAX_SPEED_SLIDER_VALUE = 30
RESTART_BUTTON_SIZE = BUTTON_SIZE - 8

FOOD_PER_TURN_STEPS = [1/3, 1/2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


class ToolbarUI(QWidget):
    """
    Represents the toolbar user interface for the BacteriaSim application.

    The ToolbarUI class provides a graphical user interface for controlling the simulation.
    It includes buttons for starting/pausing the simulation, changing settings, and displaying graphs.

    Args:
        game (GameRunner): The game runner object that manages the simulation.
        update_board (Callable[[BoardData], None]): A callback function for updating the game board.
        history_saver (HistorySaver): The history saver object for saving simulation history.

    Attributes:
        play_icon (QIcon): The icon for the play button.
        pause_icon (QIcon): The icon for the pause button.
        settings (Settings): The current game settings.
        game (GameRunner): The game runner object that manages the simulation.
        update_board (Callable[[BoardData], None]): A callback function for updating the game board.
        history_saver (HistorySaver): The history saver object for saving simulation history.
        play_pause_button (QPushButton): The button for starting/pausing the simulation.
        restart_button (QPushButton): The button for restarting the simulation.
        speed_slider (QSlider): The slider for adjusting the simulation speed.
        mutation_slider (QSlider): The slider for adjusting the mutation rate.
        food_slider (UnevenStepSlider): The slider for adjusting the food per turn.
        settings_button (QPushButton): The button for changing settings.
        graph_button (QPushButton): The button for displaying graphs.
    """

    def __init__(self, game: GameRunner, update_board: Callable[[BoardData], None], history_saver: HistorySaver) -> None:
        super().__init__()
        self.play_icon = QIcon("assets/play.svg")
        self.pause_icon = QIcon("assets/pause.svg")
        self.settings = game.settings
        self.game = game
        self.update_board = update_board
        self.history_saver = history_saver

        self.initUI()

        self.game.add_listener(ON_PAUSE_PLAY_TOGGLE,
                               self.__on_play_pause_changed)

    def toggle_play_pause(self, is_checked: bool) -> None:
        """
        Toggles the play/pause state of the simulation.

        Args:
            is_checked (bool): The new play/pause state.

        Returns:
            None
        """
        self.game.toggle_play_pause(is_checked)

    def settings_button_clicked(self) -> None:
        """
        Handles the click event of the settings button.

        Opens the settings modal dialog and updates the game settings accordingly.

        Returns:
            None
        """
        settingsModal = SettingsModal(self.settings)
        is_running = self.play_pause_button.isChecked()

        if is_running:
            self.toggle_play_pause(False)

        results = settingsModal.exec_()

        if results == QDialog.Accepted:
            self.settings = settingsModal.settings
            self.game.change_settings(self.settings)
            self.update_board(self.game.board)

        if is_running:
            self.toggle_play_pause(True)

    def initUI(self) -> None:
        """
        Initializes the user interface for the toolbar.

        This method sets up the layout and adds various buttons and sliders to the toolbar.
        It also connects the appropriate signals to their respective slots.

        Returns:
            None
        """
        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        play_pause_button = QPushButton()
        play_pause_button.setIcon(self.play_icon)
        play_pause_button.setCheckable(True)

        play_pause_button.clicked.connect(self.toggle_play_pause)
        play_pause_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        play_pause_button.setFixedSize(QSize(BUTTON_SIZE, BUTTON_SIZE))
        self.play_pause_button = play_pause_button

        restart_button = QPushButton()
        restart_button.setIcon(QIcon("assets/restart.svg"))
        restart_button.setIconSize(
            QSize(RESTART_BUTTON_SIZE, RESTART_BUTTON_SIZE))
        restart_button.setFixedSize(QSize(BUTTON_SIZE, BUTTON_SIZE))
        restart_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        restart_button.clicked.connect(self.__restart_button_clicked)
        self.restart_button = restart_button

        speed_slider = QSlider(Qt.Orientation.Horizontal)
        speed_slider.setObjectName("speed_slider")

        speed_slider.setRange(1, MAX_SPEED_SLIDER_VALUE)
        speed_slider.setValue(1)
        speed_slider.setFixedWidth(SLIDER_SIZE)
        speed_slider.valueChanged.connect(self.game.change_speed)

        self.speed_slider = speed_slider

        speed_slider_container = SliderWithButton(
            speed_slider, QIcon("assets/speed.svg"), "Speed", lambda value: f"x{value}")

        mutation_slider = QSlider(Qt.Orientation.Horizontal)
        mutation_slider.setObjectName("mutation_slider")
        mutation_slider.setRange(0, 10)
        mutation_slider.setValue(round(DEFAULT_MUTATION_RATE*10))
        mutation_slider.setFixedWidth(SLIDER_SIZE)
        mutation_slider.valueChanged.connect(self.__change_mutation_rate)

        mutation_slider_container = SliderWithButton(
            mutation_slider, QIcon("assets/dna.svg"), "Mutation Rate", lambda value: f"{value*10}%")

        food_slider = UnevenStepSlider(Qt.Orientation.Horizontal)
        food_slider.setObjectName("food_slider")
        food_slider.setSteps(FOOD_PER_TURN_STEPS)
        food_slider.setValue(DEFAULT_FOOD_PER_TURN)

        food_slider.setFixedWidth(SLIDER_SIZE)
        food_slider.on_value_changed(self.__change_food_rate)

        food_slider_container = SliderWithButton(
            food_slider, QIcon("assets/apple.svg"), "Food",
            lambda value: f"{str(round(value, 2))} per turn", food_slider.on_value_changed)

        self.settings_button: QPushButton = QPushButton()
        self.settings_button.setIcon(QIcon("assets/cog.svg"))
        self.settings_button.setIconSize(QSize(BUTTON_SIZE, BUTTON_SIZE))
        self.settings_button.clicked.connect(self.settings_button_clicked)
        self.settings_button.setCursor(
            QCursor(Qt.CursorShape.PointingHandCursor))
        self.settings_button.setFixedSize(QSize(BUTTON_SIZE, BUTTON_SIZE))

        self.graph_button: QPushButton = QPushButton()
        self.graph_button.setIcon(QIcon("assets/graph.svg"))
        self.graph_button.setIconSize(QSize(BUTTON_SIZE, BUTTON_SIZE))
        self.graph_button.setFixedSize(QSize(BUTTON_SIZE, BUTTON_SIZE))

        layout.setSpacing(20)

        layout.addWidget(play_pause_button)
        layout.addWidget(restart_button)
        layout.addWidget(speed_slider_container)
        layout.addWidget(mutation_slider_container)
        layout.addWidget(food_slider_container)
        spacer = QSpacerItem(
            0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        layout.addItem(spacer)
        layout.addWidget(self.graph_button)
        layout.addWidget(
            self.settings_button, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(layout)
        apply_style_sheet_file(self, CSS_FILES)

    def __change_mutation_rate(self, value: int) -> None:
        """
        Changes the mutation rate based on the slider value.

        Args:
            value (int): The new slider value.

        Returns:
            None
        """
        self.settings.mutation_rate = value/10
        self.game.change_settings(self.settings)

    def __change_food_rate(self, value: float) -> None:
        """
        Changes the food per turn rate based on the slider value.

        Args:
            value (float): The new slider value.

        Returns:
            None
        """
        self.settings.food_per_turn = value
        self.game.change_settings(self.settings)

    def __on_play_pause_changed(self, is_playing: bool) -> None:
        """
        Handles the play/pause state change event.

        Args:
            is_playing (bool): The new play/pause state.

        Returns:
            None
        """
        self.play_pause_button.setChecked(is_playing)

        if is_playing:
            self.play_pause_button.setIcon(self.pause_icon)
        else:
            self.play_pause_button.setIcon(self.play_icon)

    def __restart_button_clicked(self) -> None:
        """
        Handles the click event of the restart button.

        Restarts the simulation by clearing the history and initializing a new run.

        Returns:
            None
        """
        self.history_saver.clear_history()
        self.game.initialize_run()
