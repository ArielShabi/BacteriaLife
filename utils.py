from project_types import Location, Vector


def sum_locations(location1: Location, location2: Location) -> Location:
    return (location1[0] + location2[0], location1[1] + location2[1])


def increase_location(location: Location, increase: int) -> Location:
    return (location[0] + increase, location[1] + increase)


def get_direction_vector(start: Location, end: Location) -> Location:
    return (end[0] - start[0], end[1] - start[1])


def get_distance(start: Location, end: Location) -> int:
    return int(round(
        ((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5)
    )


def is_point_on_line(start: Location, end: Location, point: Location, tolerance: float = 1e-9) -> bool:
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
    return (
        min(max_location[0], max(min_location[0], location[0])),
        min(max_location[1], max(min_location[1], location[1]))
    )


def round_vector(vector: Location) -> Location:
    return (round(vector[0]), round(vector[1]))


def set_vector_length(vector: Vector, length: int) -> Vector:
    magnitude = (vector[0] ** 2 + vector[1] ** 2) ** 0.5
    if magnitude == 0:
        return vector
    normalized_vector = (vector[0] / magnitude, vector[1] / magnitude)
    return round_vector(
        (normalized_vector[0] * length, normalized_vector[1] * length)
    )
