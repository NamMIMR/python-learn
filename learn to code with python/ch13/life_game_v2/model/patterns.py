from typing import List


def class GridModel:
    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width
    
    def start_model(self) -> List[List[int]]:
        pass

    def next_model(self) -> List[List[int]]:
        pass

    def setup_model(self) -> List[List[int]]:
        grid_model = start_model()
        next_grid_model = next_model()
        global grid_model, next_grid_model
        return grid_model, next_grid_model