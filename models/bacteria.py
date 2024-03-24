from .bacteria_properties import BacteriaProperties
from .models_types import BacteriaStrategy, BoardObject
from project_types import Vector


class Bacteria:
    def __init__(self, id: str, energy: int, properties: BacteriaProperties, strategy: BacteriaStrategy):
        self.id = id
        self.properties = properties
        self.energy = energy
        self.strategy = strategy

    def play_turn(self, area_of_sense: list[list[BoardObject]]) -> Vector:
        return self.strategy(area_of_sense, self.properties)

    def energy_per_turn(self) -> int:
        return self.properties.sense + self.properties.speed ** 2
