from models.models_types import BoardObject
from project_types import Vector
from helpers.random_generator import generate_random_vector


class BacteriaProperties:
    def __init__(self, speed: int = 1, sense: int = 1):
        self.speed = speed
        self.sense = sense


class Bacteria:
    def __init__(self, id: str, name: str, width: int, height: int, properties: BacteriaProperties):
        self.id = id
        self.name = name
        self.width = width
        self.height = height
        self.properties = properties

    def __str__(self):
        return self.name

    def play_turn(self, area_of_sense: list[list[BoardObject]]) -> Vector:
        return generate_random_vector(self.properties.speed)
