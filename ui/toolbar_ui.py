from PyQt5.QtWidgets import QPushButton, QWidget, QHBoxLayout, QSlider, QDialog, QSizePolicy, QSpacerItem
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import QSize, Qt

from const import BUTTON_SIZE, DEFAULT_MUTATION_RATE
from logic.game_runner import ON_PAUSE_PLAY_TOGGLE, GameRunner
from ui.components.slider_with_icon import SliderWithButton
from ui.settings_modal import SettingsModal
from ui.utils import apply_style_sheet_file

CSS_FILES = [
    "filled_slider.css",
    "toolbar.css",
]

SLIDER_SIZE = 200
MAX_SLIDER_VALUE = 30


class ToolbarUI(QWidget):
    def __init__(self, game: GameRunner):
        super().__init__()
        self.play_icon = QIcon("assets/play.svg")
        self.pause_icon = QIcon("assets/pause.svg")
        self.settings = game.settings
        self.game = game

        self.initUI()

        self.game.add_listener(ON_PAUSE_PLAY_TOGGLE,
                               self.__on_play_pause_changed)

    def toggle_play_pause(self, is_checked: bool):
        self.game.toggle_play_pause(is_checked)

    def settings_button_clicked(self):
        settingsModal = SettingsModal(self.settings)
        is_running = self.play_pause_button.isChecked()

        if is_running:
            self.toggle_play_pause(False)

        results = settingsModal.exec_()

        if results == QDialog.Accepted:
            self.settings = settingsModal.settings
            self.game.change_settings(self.settings)

        if is_running:
            self.toggle_play_pause(True)

    def initUI(self):
        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignLeft)

        play_pause_button = QPushButton(icon=self.play_icon)
        play_pause_button.setCheckable(True)

        play_pause_button.clicked.connect(self.toggle_play_pause)
        play_pause_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.play_pause_button = play_pause_button
        play_pause_button.setFixedSize(QSize(BUTTON_SIZE, BUTTON_SIZE))

        speed_slider = QSlider(Qt.Horizontal)
        speed_slider.setObjectName("speed_slider")

        speed_slider.setRange(1, MAX_SLIDER_VALUE)
        speed_slider.setValue(1)
        speed_slider.setFixedWidth(SLIDER_SIZE)
        speed_slider.valueChanged.connect(self.game.change_speed)                

        self.speed_slider = speed_slider

        speed_slider_container = SliderWithButton(
            speed_slider, QIcon("assets/speed.svg"), "Speed")

        mutation_slider = QSlider(Qt.Horizontal)
        mutation_slider.setObjectName("mutation_slider")
        mutation_slider.setRange(0, 10)
        mutation_slider.setValue(round(DEFAULT_MUTATION_RATE*10))
        mutation_slider.setFixedWidth(SLIDER_SIZE)
        mutation_slider.valueChanged.connect(self.__change_mutation_rate)

        mutation_slider_container = SliderWithButton(
            mutation_slider, QIcon("assets/dna.svg"), "Mutation Rate")

        settings_button = QPushButton(icon=QIcon("assets/cog.svg"))
        settings_button.setIconSize(QSize(BUTTON_SIZE, BUTTON_SIZE))
        settings_button.clicked.connect(self.settings_button_clicked)
        settings_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.settings_button = settings_button
        settings_button.setFixedSize(QSize(BUTTON_SIZE, BUTTON_SIZE))

        self.graph_button = QPushButton(icon=QIcon("assets/graph.svg"))
        self.graph_button.setIconSize(QSize(BUTTON_SIZE, BUTTON_SIZE))
        self.graph_button.setFixedSize(QSize(BUTTON_SIZE, BUTTON_SIZE))

        layout.setSpacing(20)

        layout.addWidget(play_pause_button)
        layout.addWidget(speed_slider_container)
        layout.addWidget(mutation_slider_container)
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout.addItem(spacer)
        layout.addWidget(self.graph_button)
        layout.addWidget(settings_button, alignment=Qt.AlignRight)

        self.setLayout(layout)
        apply_style_sheet_file(self, CSS_FILES)

    def __change_mutation_rate(self, value: int):
        self.settings.mutation_rate = value/10
        self.game.change_settings(self.settings)

    def __on_play_pause_changed(self, is_playing: bool):
        self.play_pause_button.setChecked(is_playing)

        if is_playing:
            self.play_pause_button.setIcon(self.pause_icon)
        else:
            self.play_pause_button.setIcon(self.play_icon)
