from PyQt5.QtWidgets import QWidget, QSlider, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt

from ui.utils import apply_style_sheet_file

CSS_FILE = "history_slider.css"

LABEL_WIDTH = 50

class HistorySliderUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QHBoxLayout(self)
        self.slider = QSlider(Qt.Horizontal)

        self.slider.setRange(1, 10)
        self.slider.setValue(1)

        self.slider_label = QLabel("0/0")
        self.slider_label.setFixedWidth(LABEL_WIDTH)
        self.slider_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.slider)
        layout.addWidget(self.slider_label)

        self.setLayout(layout)
        apply_style_sheet_file(self, CSS_FILE)
