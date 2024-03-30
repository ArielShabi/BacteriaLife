from project_types import Location, Vector


def sum_locations(location1: Location, location2: Location) -> Location:
    """
    Sums two locations and returns the result.

    Args:
        location1 (Location): The first location.
        location2 (Location): The second location.

    Returns:
        Location: The sum of the two locations.
    """
    return (location1[0] + location2[0], location1[1] + location2[1])


def increase_location(location: Location, increase: int) -> Location:
    """
    Increases the coordinates of a location by a given amount.

    Args:
        location (Location): The location to be increased.
        increase (int): The amount to increase the coordinates by.

    Returns:
        Location: The increased location.
    """
    return (location[0] + increase, location[1] + increase)


def get_direction_vector(start: Location, end: Location) -> Location:
    """
    Calculates the direction vector from the start location to the end location.

    Args:
        start (Location): The start location.
        end (Location): The end location.

    Returns:
        Location: The direction vector from start to end.
    """
    return (end[0] - start[0], end[1] - start[1])


def get_distance(start: Location, end: Location) -> float:
    """
    Calculates the distance between two locations.

    Args:
        start (Location): The start location.
        end (Location): The end location.

    Returns:
        float: The distance between the two locations.
    """
    return float(((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5)


def is_point_on_line(start: Location, end: Location, point: Location, tolerance: float = 1e-9) -> bool:
    """
    Checks if a point lies on a line segment defined by two locations.

    Args:
        start (Location): The start location of the line segment.
        end (Location): The end location of the line segment.
        point (Location): The point to be checked.
        tolerance (float, optional): Tolerance for floating point comparisons. Defaults to 1e-9.

    Returns:
        bool: True if the point lies on the line segment, False otherwise.
    """
    x1, y1 = start
    x2, y2 = end
    x, y = point

    # Check if the point is on the line formed by start and end
    cross_product = abs((x2 - x1) * (y - y1) - (x - x1) * (y2 - y1))
    if cross_product <= tolerance:
        # Check if the point is within the line segment
        if min(x1, x2) - tolerance <= x <= max(x1, x2) + tolerance and \
           min(y1, y2) - tolerance <= y <= max(y1, y2) + tolerance:
            return True

    return False


def clamp_location(location: Location, min_location: Location, max_location: Location) -> Location:
    """
    Clamps a location within the specified minimum and maximum locations.

    Args:
        location (Location): The location to be clamped.
        min_location (Location): The minimum allowed location.
        max_location (Location): The maximum allowed location.

    Returns:
        Location: The clamped location.
    """
    return (
        min(max_location[0], max(min_location[0], location[0])),
        min(max_location[1], max(min_location[1], location[1]))
    )


def round_vector(vector: Location) -> Location:
    """
    Rounds the coordinates of a vector to the nearest integer values.

    Args:
        vector (Location): The vector to be rounded.

    Returns:
        Location: The rounded vector.
    """
    return (round(vector[0]), round(vector[1]))


def set_vector_length(vector: Vector, length: float) -> Vector:
    """
    Sets the length of a vector to a specified value.

    Args:
        vector (Vector): The vector whose length is to be set.
        length (float): The desired length of the vector.

    Returns:
        Vector: The vector with the specified length.
    """
    magnitude = (vector[0] ** 2 + vector[1] ** 2) ** 0.5
    if magnitude == 0:
        return vector
    normalized_vector = (vector[0] / magnitude, vector[1] / magnitude)
    return round_vector(
        (normalized_vector[0] * length, normalized_vector[1] * length)
    )
