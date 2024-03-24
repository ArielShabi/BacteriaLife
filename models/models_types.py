from typing import Union

from .bacteria_properties import BacteriaProperties
from .food import Food

BoardObject = Union[None, BacteriaProperties, Food]
