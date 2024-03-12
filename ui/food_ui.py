from PyQt5.QtSvg import QGraphicsSvgItem
from PyQt5.QtWidgets import QGraphicsColorizeEffect
from const import SVG_SIZE
from helpers.color import get_food_color

from models.food import Food

FOOD_SVG = "assets/apple.svg"


class FoodUI(QGraphicsSvgItem):
    def __init__(self, food: Food, width_offset: float, height_offset: float):

        super().__init__(FOOD_SVG)

        desired_width = SVG_SIZE * width_offset
        desired_height = SVG_SIZE * height_offset
        current_width = self.boundingRect().width()
        current_height = self.boundingRect().height()
        scale_factor_x = desired_width / current_width
        scale_factor_y = desired_height / current_height
        self.setScale(min(scale_factor_x, scale_factor_y))

        colorize_effect = QGraphicsColorizeEffect()
        colorize_effect.setColor(get_food_color(food))
        self.setGraphicsEffect(colorize_effect)
