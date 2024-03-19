from PyQt5.QtGui import QColor
from multipledispatch import dispatch


from const import MAX_BACTERIA_SENSE, MAX_BACTERIA_SPEED
from models.bacteria_properties import BacteriaProperties
from models.food import Food


@dispatch(BacteriaProperties)
def get_bacteria_color(bacteria: BacteriaProperties) -> QColor:
    speed_color = int((bacteria.speed / MAX_BACTERIA_SPEED) * 255)
    sense_color = int((bacteria.sense / MAX_BACTERIA_SENSE) * 255)
    return QColor(speed_color, 0, sense_color)


@dispatch(int, int)
def get_bacteria_color(speed: int, sense: int) -> QColor:
    speed_color = int((speed / MAX_BACTERIA_SPEED) * 255)
    sense_color = int((sense / MAX_BACTERIA_SENSE) * 255)
    return QColor(speed_color, 0, sense_color)


def get_food_color(food: Food) -> QColor:
    return QColor(255, 0, 0)
