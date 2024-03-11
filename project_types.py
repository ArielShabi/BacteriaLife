from typing import Callable
from models.bacteria_properties import BacteriaProperties

from models.models_types import BoardObject


Location = tuple[int, int]
Vector = tuple[int, int]

BacteriaStrategy = Callable[[
    list[list[BoardObject]], BacteriaProperties], Vector]
