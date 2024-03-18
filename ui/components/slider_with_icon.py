from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSlider, QLabel, QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


class SliderWithButton(QWidget):
    def __init__(self, slider: QSlider, icon: QIcon):
        super().__init__()
        self.initUI(icon, slider)

    def initUI(self, icon: QIcon, slider: QSlider):
        layout = QHBoxLayout()

        slider_icon = QLabel()
        slider_icon.setPixmap(icon.pixmap(QSize(30, 30)))

        layout.addWidget(slider_icon)
        layout.addWidget(slider)
        layout.setSpacing(10)

        self.setLayout(layout)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
