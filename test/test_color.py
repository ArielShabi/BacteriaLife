import pytest
from PyQt5.QtGui import QColor
from const import MAX_BACTERIA_SENSE, MAX_BACTERIA_SPEED
from helpers.color import (
    get_bacteria_color,
    get_bacteria_color_from_properties,
    get_food_color,
    get_portal_color,
    neon_color,
)
from models.bacteria_properties import BacteriaProperties
from models.food import Food


@pytest.mark.parametrize("speed, sense, expected", [
    (0, 0, QColor(100, 0, 0)),
    (MAX_BACTERIA_SPEED, MAX_BACTERIA_SENSE, QColor(255, 0, 205)),
])
def test_get_bacteria_color(speed, sense, expected):
    assert get_bacteria_color(speed, sense) == expected


@pytest.mark.parametrize("bacteria, expected", [
    (BacteriaProperties("", 0, 0), QColor(100, 0, 0)),
    (BacteriaProperties("", MAX_BACTERIA_SPEED,
     MAX_BACTERIA_SENSE), QColor(255, 0, 205)),
])
def test_get_bacteria_color_from_properties(bacteria, expected):
    assert get_bacteria_color(bacteria) == expected


def test_get_food_color():
    assert get_food_color(Food(0)) == QColor(255, 0, 0)


def test_get_portal_color():
    assert get_portal_color() == QColor("#00FFC9")
