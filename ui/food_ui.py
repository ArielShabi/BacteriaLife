from PyQt5.QtSvg import QGraphicsSvgItem
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsColorizeEffect
from helpers.color import get_bacteria_color, get_food_color

from models.food import Food

FOOD_SVG = "assets/apple.svg"


FOOD_WIDTH = 4
FOOD_HEIGHT = 4


class FoodUI(QGraphicsSvgItem):
    def __init__(self, food: Food, width_offset: float, height_offset: float):

        super().__init__(FOOD_SVG)

        desired_width = FOOD_WIDTH * width_offset
        desired_height = FOOD_HEIGHT * height_offset
        current_width = self.boundingRect().width()
        current_height = self.boundingRect().height()
        scale_factor_x = desired_width / current_width
        scale_factor_y = desired_height / current_height
        self.setScale(min(scale_factor_x, scale_factor_y))

        colorize_effect = QGraphicsColorizeEffect()
        colorize_effect.setColor(get_food_color(food))
        self.setGraphicsEffect(colorize_effect)
