from logic.bacteria_strategies.random_strategy import random_strategy
from models.bacteria_properties import BacteriaProperties
from models.models_types import BoardObject
from project_types import Vector


def test_random_strategy():
    bacteria = BacteriaProperties("", speed=3, sense=1)

    area_of_sense = [
        [None, None, None],
        [None, bacteria, None],
        [None, None, None]
    ]

    result = random_strategy(area_of_sense, bacteria)
    
    print(result)

    vector_length = round((result[0] ** 2 + result[1] ** 2) ** 0.5)

    # in case the vector is 0,0
    assert vector_length == 3 or vector_length == 0
