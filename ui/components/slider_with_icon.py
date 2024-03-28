from typing import Callable, Optional
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSlider, QLabel, QSizePolicy, QToolTip
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import QSize, Qt

SPACING = 10
HANDLE_SIZE = 30


class SliderWithButton(QWidget):
    """
    A custom widget that combines a slider with an icon and label.

    Args:
        slider (QSlider): The slider widget.
        icon (QIcon): The icon to be displayed.
        label (str): The label to be displayed as a tooltip.
        tooltip_function (Optional[Callable[[float], str]]): A function that takes the slider value as input and returns a tooltip string. Default is None.
        on_value_changed (Optional[Callable[[Callable[[float], None]], None]]): A function that takes a callback function as input and connects it to the valueChanged signal of the slider. Default is None.
    """

    def __init__(self,
                 slider: QSlider,
                 icon: QIcon,
                 label: str,
                 tooltip_function: Optional[Callable[[float], str]] = None,
                 on_value_changed: Optional[Callable[[Callable[[float], None]], None]] = None
                 ):
        super().__init__()
        self.initUI(icon, slider, label)
        self.tooltip_function = tooltip_function

        if (on_value_changed):
            on_value_changed(self.show_slider_value)
        else:
            slider.valueChanged.connect(self.show_slider_value)

    def initUI(self, icon: QIcon, slider: QSlider, label: str) -> None:
        """
        Initializes the user interface of the widget.

        Args:
            icon (QIcon): The icon to be displayed.
            slider (QSlider): The slider widget.
            label (str): The label to be displayed as a tooltip.

        Returns:
            None
        """
        layout = QHBoxLayout()

        slider_icon = QLabel()
        slider_icon.setPixmap(icon.pixmap(QSize(HANDLE_SIZE, HANDLE_SIZE)))
        slider_icon.setToolTip(label)

        layout.addWidget(slider_icon)
        layout.addWidget(slider)

        layout.setSpacing(SPACING)

        slider.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.setLayout(layout)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    def show_slider_value(self, value: float) -> None:
        """
        Displays the tooltip with the slider value.

        Args:
            value (float): The current value of the slider.

        Returns:
            None
        """
        text = self.tooltip_function(value) if self.tooltip_function else f"{value}"
        QToolTip.showText(QCursor.pos(), text)
