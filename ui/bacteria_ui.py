from PyQt5.QtSvg import QGraphicsSvgItem
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsColorizeEffect
from helpers.color import get_bacteria_color


from models.bacteria import Bacteria

BACTERIA_SVG = "assets/bacteria.svg"


class BacteriaUI(QGraphicsSvgItem):
    def __init__(self, bacteria: Bacteria, width_offset: float, height_offset: float):

        super().__init__(BACTERIA_SVG)

        desired_width = bacteria.width * width_offset
        desired_height = bacteria.height * height_offset
        current_width = self.boundingRect().width()
        current_height = self.boundingRect().height()
        scale_factor_x = desired_width / current_width
        scale_factor_y = desired_height / current_height
        self.setScale(min(scale_factor_x, scale_factor_y))

        colorize_effect = QGraphicsColorizeEffect()
        colorize_effect.setColor(get_bacteria_color(bacteria))
        self.setGraphicsEffect(colorize_effect)
