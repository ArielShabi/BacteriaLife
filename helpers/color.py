from PyQt5.QtGui import QColor

from models.bacteria import Bacteria
from models.food import Food

MAX_SPEED = 10
MAX_SENSE = 30


def get_bacteria_color(bacteria: Bacteria) -> QColor:
    speed_color = int((bacteria.properties.speed / MAX_SPEED) * 255)
    sense_color = int((bacteria.properties.sense / MAX_SENSE) * 255)
    return QColor(speed_color, 0, sense_color)


def get_food_color(food: Food) -> QColor:
    return QColor(255, 0, 0)
