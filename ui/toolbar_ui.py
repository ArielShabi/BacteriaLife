from PyQt5.QtWidgets import QPushButton, QWidget, QHBoxLayout, QSlider
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import QSize, Qt

from logic.event_emitter import EventEmitter
from ui.utils import apply_style_sheet_file

CSS_FILE = "toolbar.css"
BUTTON_SIZE = 35

ON_PLAY_PAUSE = "on_play_pause"
ON_SPEED_CHANGE = "on_speed_change"

class ToolbarUI(QWidget, EventEmitter):
    def __init__(self):
        super().__init__()
        self.play_icon = QIcon("assets/play.svg")
        self.pause_icon = QIcon("assets/pause.svg")

        self.initUI()

    def togglePlayPause(self, is_checked: bool):
        print(is_checked)
        if is_checked:
            self.play_pause_button.setIcon(self.pause_icon)
        else:
            self.play_pause_button.setIcon(self.play_icon)

        self.fire_event(ON_PLAY_PAUSE, is_checked)

    def initUI(self):
        layout = QHBoxLayout(self)
        layout.setAlignment(Qt.AlignLeft)

        play_pause_button = QPushButton(icon=self.pause_icon)
        play_pause_button.setCheckable(True)
        
        play_pause_button.clicked.connect(self.togglePlayPause)
        play_pause_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.play_pause_button = play_pause_button
        play_pause_button.setFixedSize(QSize(BUTTON_SIZE, BUTTON_SIZE))

        speed_slider = QSlider(Qt.Horizontal)
        speed_slider.setRange(1, 10)
        speed_slider.setValue(1)
        speed_slider.setFixedWidth(150)
        speed_slider.valueChanged.connect(lambda value: self.fire_event(ON_SPEED_CHANGE, value))

        self.speed_slider = speed_slider

        layout.setSpacing(20)

        layout.addWidget(play_pause_button)
        layout.addWidget(speed_slider)

        self.setLayout(layout)
        apply_style_sheet_file(self, CSS_FILE)
