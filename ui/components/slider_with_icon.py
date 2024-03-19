from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSlider, QLabel, QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


class SliderWithButton(QWidget):
    def __init__(self, slider: QSlider, icon: QIcon, label: str):
        super().__init__()
        self.initUI(icon, slider, label)

    def initUI(self, icon: QIcon, slider: QSlider, label: str):
        layout = QHBoxLayout()

        slider_icon = QLabel()
        slider_icon.setPixmap(icon.pixmap(QSize(30, 30)))
        slider_icon.setToolTip(label)

        layout.addWidget(slider_icon)
        layout.addWidget(slider)
        layout.setSpacing(10)

        self.setLayout(layout)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
