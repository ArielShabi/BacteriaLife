from PyQt5.QtWidgets import QPushButton, QWidget, QHBoxLayout, QSizePolicy
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import QSize, Qt

from ui.utils import apply_style_sheet_file

CSS_FILE = "toolbar.css"
BUTTON_SIZE = 35


class ToolbarUI(QHBoxLayout):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.play_icon = QIcon("assets/play.svg")
        self.pause_icon = QIcon("assets/pause.svg")

        self.initUI()

    def togglePlayPause(self, is_checked: bool):
        print(is_checked)
        if is_checked:
            self.play_pause_button.setIcon(self.pause_icon)
        else:
            self.play_pause_button.setIcon(self.play_icon)

    def initUI(self):
        play_pause_button = QPushButton(icon=self.pause_icon)
        play_pause_button.setCheckable(True)
        play_pause_button.setChecked(True)
        play_pause_button.clicked.connect(self.togglePlayPause)
        play_pause_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.play_pause_button = play_pause_button
        play_pause_button.setFixedSize(QSize(BUTTON_SIZE, BUTTON_SIZE))

        apply_style_sheet_file(play_pause_button, CSS_FILE)
        self.addWidget(play_pause_button, alignment=Qt.AlignLeft)
