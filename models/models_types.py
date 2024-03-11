from enum import Enum
from typing import Union

from models.bacteria_properties import BacteriaProperties
from models.food import Food

BoardObject = Union[None, BacteriaProperties, Food]
