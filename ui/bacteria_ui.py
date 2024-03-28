from PyQt5.QtSvg import QGraphicsSvgItem
from PyQt5.QtWidgets import QGraphicsColorizeEffect
from PyQt5.QtGui import QColor
from const import SVG_SIZE


class BoardItemSvg(QGraphicsSvgItem):
    """
    This class represents a custom SVG item for the game board.

    Args:
        svg_path (str): The path to the SVG file.
        color (QColor): The color to apply to the SVG item.
        width_offset (float): The desired width offset for scaling the SVG item.
        height_offset (float): The desired height offset for scaling the SVG item.
    """

    def __init__(self, svg_path: str, color: QColor, width_offset: float, height_offset: float):
        """
        Initializes a new instance of the BoardItemSvg class.

        Args:
            svg_path (str): The path to the SVG file.
            color (QColor): The color to apply to the SVG item.
            width_offset (float): The desired width offset for scaling the SVG item.
            height_offset (float): The desired height offset for scaling the SVG item.

        Returns:
            None
        """

        super().__init__(svg_path)

        desired_width = SVG_SIZE * width_offset
        desired_height = SVG_SIZE * height_offset
        current_width = self.boundingRect().width()
        current_height = self.boundingRect().height()
        scale_factor_x = desired_width / current_width
        scale_factor_y = desired_height / current_height
        self.setScale(min(scale_factor_x, scale_factor_y))

        colorize_effect = QGraphicsColorizeEffect()
        colorize_effect.setColor(color)

        self.setGraphicsEffect(colorize_effect)
