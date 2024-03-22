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

    color.setHsv(color.hue(), 255, 255)

    return color


def get_food_color(food: Food) -> QColor:
    if (food.energy == 999):
        return QColor(0, 255, 0)
    return QColor(255, 0, 0)
