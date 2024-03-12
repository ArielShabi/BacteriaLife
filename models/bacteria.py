from models.bacteria_properties import BacteriaProperties
from models.models_types import BoardObject
from project_types import BacteriaStrategy, Vector


class Bacteria:
    def __init__(self, id: str, energy: int, properties: BacteriaProperties, strategy: BacteriaStrategy):
        self.id = id
        self.properties = properties
        self.energy = energy
        self.strategy = strategy

    def play_turn(self, area_of_sense: list[list[BoardObject]]) -> Vector:
        return self.strategy(area_of_sense, self.properties)
