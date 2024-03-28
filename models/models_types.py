from typing import Callable, Union

from project_types import Vector

from .bacteria_properties import BacteriaProperties
from .food import Food

BoardObject = Union[None, BacteriaProperties, Food]

BacteriaStrategy = Callable[[
    list[list[BoardObject]], BacteriaProperties], Vector]

"""
This module defines the types used in the BacteriaSim models.

- `BoardObject`: Represents an object on the simulation board. It can be either `None`, `BacteriaProperties`, or `Food`.
- `BacteriaStrategy`: Represents a callable function that takes a 2D list of `BoardObject` and `BacteriaProperties` as input and returns a `Vector` representing the next move of a bacteria.

Note: The `Vector` and other types used in this module are imported from the `project_types` module.
"""
