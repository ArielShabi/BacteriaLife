import pytest

import utils
import pytest
import utils


@pytest.mark.parametrize("location, min_location, max_location, expected", [
    ((0, 0), (0, 0), (0, 0), (0, 0)),
    ((0, 0), (0, 0), (1, 1), (0, 0)),
    ((5, 5), (0, 0), (1, 1), (1, 1)),
    ((5, 5), (3, 3), (7, 7), (5, 5)),
    ((0, 0), (3, 3), (7, 7), (3, 3))])
def test_clamp_vector(location, min_location, max_location, expected):
    assert utils.clamp_location(
        location, min_location, max_location) == expected


@pytest.mark.parametrize("location1, location2, expected", [
    ((0, 0), (0, 0), (0, 0)),
    ((1, 2), (3, 4), (4, 6)),
    ((-1, -2), (3, 4), (2, 2)),
    ((-1, -2), (-3, -4), (-4, -6)),
])
def test_sum_locations(location1, location2, expected):
    assert utils.sum_locations(location1, location2) == expected


@pytest.mark.parametrize("location, increase, expected", [
    ((0, 0), 0, (0, 0)),
    ((1, 2), 3, (4, 5)),
    ((-1, -2), -3, (-4, -5)),
])
def test_increase_location(location, increase, expected):
    assert utils.increase_location(location, increase) == expected


@pytest.mark.parametrize("start, end, expected", [
    ((0, 0), (0, 0), (0, 0)),
    ((1, 2), (3, 4), (2, 2)),
    ((-1, -2), (3, 4), (4, 6)),
])
def test_get_direction_vector(start, end, expected):
    assert utils.get_direction_vector(start, end) == expected


@pytest.mark.parametrize("start, end, expected", [
    ((0, 0), (0, 0), 0),
    ((1, 2), (3, 4), 8**0.5),
    ((1, -2), (3, 3), 29**0.5),
])
def test_get_distance(start, end, expected):
    assert utils.get_distance(start, end) == expected


@pytest.mark.parametrize("start, end, point, tolerance, expected", [
    ((0, 0), (0, 0), (0, 0), 1e-9, True),
    ((0, 0), (1, 1), (0.5, 0.5), 1e-9, True),
    ((0, 0), (1, 1), (0.5, 0.6), 1e-9, False),
])
def test_is_point_on_line(start, end, point, tolerance, expected):
    assert utils.is_point_on_line(start, end, point, tolerance) == expected


@pytest.mark.parametrize("location, min_location, max_location, expected", [
    ((0, 0), (0, 0), (0, 0), (0, 0)),
    ((0, 0), (0, 0), (1, 1), (0, 0)),
    ((5, 5), (0, 0), (1, 1), (1, 1)),
    ((5, 5), (3, 3), (7, 7), (5, 5)),
    ((0, 0), (3, 3), (7, 7), (3, 3)),
])
def test_clamp_location(location, min_location, max_location, expected):
    assert utils.clamp_location(
        location, min_location, max_location) == expected


@pytest.mark.parametrize("vector, expected", [
    ((0, 0), (0, 0)),
    ((1.5, 2.7), (2, 3)),
    ((-1.5, -2.7), (-2, -3)),
])
def test_round_vector(vector, expected):
    assert utils.round_vector(vector) == expected


@pytest.mark.parametrize("vector, length, expected", [
    ((0, 0), 0, (0, 0)),
    ((3, 4), 5, (3, 4)),
    ((-3, -4), 5, (-3, -4)),
])
def test_set_vector_length(vector, length, expected):
    assert utils.set_vector_length(vector, length) == expected


if __name__ == "__main__":
    pytest.main()
