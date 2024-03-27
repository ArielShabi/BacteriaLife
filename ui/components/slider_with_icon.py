from typing import Callable, Optional
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSlider, QLabel, QSizePolicy, QToolTip
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import QSize, Qt

SPACING = 10


class SliderWithButton(QWidget):
    def __init__(self,
                 slider: QSlider,
                 icon: QIcon,
                 label: str,
                 tooltip_function: Optional[Callable[[float], str]] = None,
                 on_value_changed: Optional[Callable[[
                     Callable[[float], None]], None]] = None
                 ):
        super().__init__()
        self.initUI(icon, slider, label)
        self.tooltip_function = tooltip_function

        if (on_value_changed):
            on_value_changed(self.show_slider_value)
        else:
            slider.valueChanged.connect(self.show_slider_value)

    def initUI(self, icon: QIcon, slider: QSlider, label: str) -> None:
        layout = QHBoxLayout()

        slider_icon = QLabel()
        slider_icon.setPixmap(icon.pixmap(QSize(30, 30)))
        slider_icon.setToolTip(label)

        layout.addWidget(slider_icon)
        layout.addWidget(slider)

        layout.setSpacing(SPACING)

        slider.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.setLayout(layout)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    def show_slider_value(self, value: float) -> None:
        text = self.tooltip_function(
            value) if self.tooltip_function else f"{value}"
        QToolTip.showText(QCursor.pos(), text)
