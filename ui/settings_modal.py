from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QGridLayout, QSpinBox
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

        self.board_width = QSpinBox()
        self.board_width.setMinimum(0)
        self.board_width.setMaximum(5000)
        board_size_label = QLabel("x")

        self.board_height = QSpinBox()
        self.board_height.setMinimum(0)
        self.board_height.setMaximum(5000)

        grid_layout.addWidget(QLabel("Board Size:"), 0, 0)
        grid_layout.addWidget(self.board_width, 0, 1)
        grid_layout.addWidget(board_size_label, 0, 2)
        grid_layout.addWidget(self.board_height, 0, 3)

        ok_button = QPushButton("Save")
        ok_button.clicked.connect(self.accept)

        layout.addLayout(grid_layout)
        layout.addWidget(ok_button)

        self.setLayout(layout)

    def accept(self):
        self.settings.board_size = (
            self.board_width.value(), self.board_height.value())
        super().accept()

    def showEvent(self, event):
        super().showEvent(event)
        self.board_width.setValue(self.settings.board_size[0])
        self.board_height.setValue(self.settings.board_size[1])
