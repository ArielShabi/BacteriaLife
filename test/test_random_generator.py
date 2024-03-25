import random
import pytest

from helpers.random_generator import (
    generate_random_location,
    generate_random_vector,
    random_event_occurred,
    alter_value
)


@pytest.mark.parametrize("width, height", [
    (10, 10),
    (100, 100),
    (5, 5)
])
def test_generate_random_location(width, height):
    location = generate_random_location(width, height)
    assert 0 <= location[0] < height
    assert 0 <= location[1] < width


@pytest.mark.parametrize("amplitude", [
    1,
    5,
    10
])
def test_generate_random_vector(amplitude):
    vector = generate_random_vector(amplitude)
    assert isinstance(vector, tuple)
    assert len(vector) == 2
    assert abs(vector[0]) <= amplitude
    assert abs(vector[1]) <= amplitude


@pytest.mark.parametrize("change_rate", [
    0.0,
    0.5,
    1.0
])
def test_random_event_occurred(change_rate):
    random.seed(0)  # Set seed for deterministic results
    assert random_event_occurred(change_rate) == (random.random() < change_rate)


@pytest.mark.parametrize("value, change_value, min_value, max_value", [
    (5, 1, 0, 10),
    (10, 2, 5, 15),
    (-5, 3, -10, 0)
])
def test_alter_value(value, change_value, min_value, max_value):
    altered_value = alter_value(value, change_value, min_value, max_value)
    assert min_value <= altered_value <= max_value
    assert altered_value != value


if __name__ == "__main__":
    pytest.main()