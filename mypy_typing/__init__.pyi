from PyQt5.QtGui import QColor
from models.bacteria_properties import BacteriaProperties
from typing import overload


@overload
def get_bacteria_color(bacteria: BacteriaProperties) -> QColor:
    ...


@overload
def get_bacteria_color(speed: int, sense: int) -> QColor:
    ...
