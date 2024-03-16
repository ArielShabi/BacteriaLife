from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QSlider, QGridLayout
from PyQt5.QtCore import Qt

from models.settings import Settings

MAX_SLIDER_VALUE = 10
SLIDER_SIZE = 150


class SettingsModal(QDialog):
    def __init__(self, settings: Settings, parent=None):
        super().__init__(parent)
        self.settings = settings
        self.setWindowTitle("Settings")
        self.setMinimumWidth(300)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        grid_layout = QGridLayout()

        header_label = QLabel("Choose your settings:")
        layout.addWidget(header_label, alignment=Qt.AlignCenter)

        food_per_turn_slider = QSlider(Qt.Horizontal)

        food_per_turn_slider.setRange(1, MAX_SLIDER_VALUE)
        food_per_turn_slider.setValue(self.settings.food_per_turn)
        food_per_turn_slider.setFixedWidth(SLIDER_SIZE)
        food_per_turn_slider.valueChanged.connect(self.__set_food_per_turn)
        food_per_turn_label = QLabel(
            f"Food per turn: {self.settings.food_per_turn}")

        self.food_per_turn_slider = food_per_turn_slider
        self.food_per_turn_label = food_per_turn_label

        ok_button = QPushButton("Save")
        ok_button.clicked.connect(self.accept)

        grid_layout.addWidget(food_per_turn_slider, 0, 1)
        grid_layout.addWidget(food_per_turn_label, 0, 0)

        layout.addLayout(grid_layout)
        layout.addWidget(ok_button)

        self.setLayout(layout)

    def __set_food_per_turn(self, value: int):
        self.settings.food_per_turn = value
        self.food_per_turn_label.setText(f"Food per turn: {value}")
