from utils import clamp_location
import pytest
from utils import round_vector
from utils import is_point_on_line


def test_clamp_vector():
    assert clamp_location((0, 0), (0, 0), (0, 0)) == (0, 0)
    assert clamp_location((0, 0), (0, 0), (1, 1)) == (0, 0)
    assert clamp_location((5, 5), (0, 0), (1, 1)) == (1, 1)
    assert clamp_location((5, 5), (3, 3), (7, 7)) == (5, 5)
    assert clamp_location((0, 0), (3, 3), (7, 7)) == (3, 3)


def test_round_vector():
    assert round_vector((0.5, 0.5)) == (0, 0)
    assert round_vector((1.2, 2.7)) == (1, 3)
    assert round_vector((-3.8, 4.1)) == (-4, 4)
    assert round_vector((0, 0)) == (0, 0)
    assert round_vector((5.9, -2.3)) == (6, -2)


def test_is_point_on_line():
    assert is_point_on_line((0, 0), (0, 0), (0, 0)) == True
    assert is_point_on_line((0, 0), (0, 0), (1, 1)) == False
    assert is_point_on_line((0, 0), (1, 1), (0.5, 0.5)) == True
    assert is_point_on_line((0, 0), (1, 1), (1, 0)) == False
    assert is_point_on_line((0, 0), (2, 6), (1, 3)) == True
