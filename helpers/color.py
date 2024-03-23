from PyQt5.QtGui import QColor
from multipledispatch import dispatch


from const import MAX_BACTERIA_SENSE, MAX_BACTERIA_SPEED
from models.bacteria_properties import BacteriaProperties
from models.food import Food


@dispatch(BacteriaProperties)
def get_bacteria_color(bacteria: BacteriaProperties) -> QColor:

    return get_bacteria_color(bacteria.speed, bacteria.sense)


@dispatch(int, int)
def get_bacteria_color(speed: int, sense: int) -> QColor:
    speed_color = int((speed / MAX_BACTERIA_SPEED) * 255)
    sense_color = int((sense / MAX_BACTERIA_SENSE) * 255)
    return neon_color(QColor(speed_color, 0, sense_color))


def neon_color(color: QColor) -> QColor:
    r, g, b, _ = color.getRgb()

    neon_r = min(255, r + 100)
    neon_g = max(0, g - 50)
    neon_b = max(0, b - 50)

    return QColor(neon_r, neon_g, neon_b)


def get_food_color(food: Food) -> QColor:
    return QColor(255, 0, 0)


def get_portal_color() -> QColor:
    return QColor("#00FFC9")
