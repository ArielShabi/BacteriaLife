from models.models_types import Board_Object
from project_types import Vector
from random_generator import generate_random_vector


class Bacteria_Properties:
    def __init__(self, speed: int = 0, sense: int = 0):
        self.speed = speed
        self.sense = sense


class Bacteria:
    def __init__(self, id: str, name: str, width: int, height: int, properties: Bacteria_Properties):
        self.id = id
        self.name = name
        self.width = width
        self.height = height
        self.properties = properties

    def __str__(self):
        return self.name

    def play_turn(self, area_of_sense: list[list[Board_Object]]) -> Vector:
        return generate_random_vector(self.properties.speed)
