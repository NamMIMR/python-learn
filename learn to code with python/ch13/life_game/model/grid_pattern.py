import random
from typing import List
from model.setup import grid_model, height, width


def randomize(grid_model: List[List[int]], height: int, width: int) -> List[List[int]]:
    for i in range(0, height):
        for j in range(0, width):
            grid_model[i][j] = random.randint(0, 1)
    
    return grid_model