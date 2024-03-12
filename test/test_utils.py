from utils import clamp_location
import pytest


def test_clamp_vector():
    assert clamp_location((0, 0), (0, 0), (0, 0)) == (0, 0)
    assert clamp_location((0, 0), (0, 0), (1, 1)) == (0, 0)
    assert clamp_location((5, 5), (0, 0), (1, 1)) == (1, 1)
    assert clamp_location((5, 5), (3, 3), (7, 7)) == (5, 5)
    assert clamp_location((0, 0), (3, 3), (7, 7)) == (3, 3)
