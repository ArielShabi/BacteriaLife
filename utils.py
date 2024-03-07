from project_types import Location


def sum_locations(location1: Location, location2: Location) -> Location:
    return (location1[0] + location2[0], location1[1] + location2[1])

def increase_location(location: Location, increase: int) -> Location:
    return (location[0] + increase, location[1] + increase)