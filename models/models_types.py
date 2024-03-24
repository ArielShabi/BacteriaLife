from typing import Callable, Union

from project_types import Vector

from .bacteria_properties import BacteriaProperties
from .food import Food

BoardObject = Union[None, BacteriaProperties, Food]

BacteriaStrategy = Callable[[
    list[list[BoardObject]], BacteriaProperties], Vector]
