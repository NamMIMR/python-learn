from typing import List
from .model_patterns import *


def setup_model(height: int, width: int, pattern: str = 'default') -> GridModel:
    global model
    if pattern == 'default':
        model = GridModel(height, width)
    elif pattern == 'random':
        model = RandomGridModel(height, width)
    return model

if __name__ == "__main__":
    model = setup_model(100, 100)
