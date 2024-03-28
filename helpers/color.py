from PyQt5.QtGui import QColor
from multipledispatch import dispatch

from const import MAX_BACTERIA_SENSE, MAX_BACTERIA_SPEED
from models.bacteria_properties import BacteriaProperties
from models.food import Food


@dispatch(BacteriaProperties)
def get_bacteria_color(bacteria: BacteriaProperties) -> QColor:
    """
    Get the color for a bacteria based on its properties.

    Args:
        bacteria (BacteriaProperties): The properties of the bacteria.

    Returns:
        QColor: The color for the bacteria.
    """
    return get_bacteria_color_from_properties(bacteria.speed, bacteria.sense)


@dispatch(int, int)  # type: ignore
def get_bacteria_color(speed: int, sense: int) -> QColor:
    """
    Get the color for a bacteria based on its speed and sense values.

    Args:
        speed (int): The speed of the bacteria.
        sense (int): The sense of the bacteria.

    Returns:
        QColor: The color for the bacteria.
    """
    speed_color = int((speed / MAX_BACTERIA_SPEED) * 255)
    sense_color = int((sense / MAX_BACTERIA_SENSE) * 255)
    return neon_color(QColor(speed_color, 0, sense_color))


def get_bacteria_color_from_properties(speed: int, sense: int) -> QColor:
    """
    Get the color for a bacteria based on its speed and sense values.

    Args:
        speed (int): The speed of the bacteria.
        sense (int): The sense of the bacteria.

    Returns:
        QColor: The color for the bacteria.
    """
    speed_color = int((speed / MAX_BACTERIA_SPEED) * 255)
    sense_color = int((sense / MAX_BACTERIA_SENSE) * 255)
    return neon_color(QColor(speed_color, 0, sense_color))


def neon_color(color: QColor) -> QColor:
    """
    Create a neon color based on the given color.

    Args:
        color (QColor): The base color.

    Returns:
        QColor: The neon color.
    """
    r = color.red()
    g = color.green()
    b = color.blue()

    neon_r = min(255, r + 100)
    neon_g = max(0, g - 50)
    neon_b = max(0, b - 50)

    return QColor(neon_r, neon_g, neon_b)


def get_food_color(food: Food) -> QColor:
    """
    Get the color for a food item.

    Args:
        food (Food): The food item.

    Returns:
        QColor: The color for the food item.
    """
    return QColor(255, 0, 0)


def get_portal_color() -> QColor:
    """
    Get the color for a portal.

    Returns:
        QColor: The color for the portal.
    """
    return QColor("#00FFC9")
