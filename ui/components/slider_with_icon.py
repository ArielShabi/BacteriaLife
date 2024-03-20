from typing import Callable
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSlider, QLabel, QSizePolicy, QToolTip
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import QSize


class SliderWithButton(QWidget):
    def __init__(self,
                 slider: QSlider,
                 icon: QIcon,
                 label: str,
                 tooltip: Callable[[int], str] = None,
                 on_value_changed: Callable[[
                     Callable[[int], None]], None] = None
                 ):
        super().__init__()
        self.initUI(icon, slider, label)
        self.tooltip_function = tooltip

        if (on_value_changed):
            on_value_changed(self.show_slider_value)
        else:
            slider.valueChanged.connect(self.show_slider_value)

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

    def show_slider_value(self, value: int) -> None:
        text = self.tooltip_function(
            value) if self.tooltip_function else f"{value}"
        QToolTip.showText(QCursor.pos(), text)
