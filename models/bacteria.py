from .bacteria_properties import BacteriaProperties
from .models_types import BacteriaStrategy, BoardObject
from project_types import Vector


class Bacteria(BacteriaProperties):    
    """
    Represents a bacteria in the simulation.

    Args:
        id (str): The unique identifier of the bacteria.
        energy (int): The initial energy level of the bacteria.
        properties (BacteriaProperties): The properties of the bacteria.
        strategy (BacteriaStrategy): The strategy used by the bacteria.

    Attributes:
        id (str): The unique identifier of the bacteria.
        properties (BacteriaProperties): The properties of the bacteria.
        energy (int): The current energy level of the bacteria.
        strategy (BacteriaStrategy): The strategy used by the bacteria.
    """

    def __init__(self, id: str, energy: int, properties: BacteriaProperties, strategy: BacteriaStrategy):
        """
        Initializes a new instance of the Bacteria class.

        Args:
            id (str): The unique identifier of the bacteria.
            energy (int): The initial energy level of the bacteria.
            properties (BacteriaProperties): The properties of the bacteria.
            strategy (BacteriaStrategy): The strategy used by the bacteria.
        """
        self.id = id
        self.properties = properties
        self.energy = energy
        self.strategy = strategy

    def play_turn(self, area_of_sense: list[list[BoardObject]]) -> Vector:
        return self.strategy(area_of_sense, self.properties)

    def energy_per_turn(self) -> int:
        return self.properties.sense + self.properties.speed ** 2
