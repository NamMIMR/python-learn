import random


class GridModel:
    def __init__(self):
        self.height: int = 100
        self.width: int = 100
    
    def setup(self):
        self.grid_model: list[list[int]] = [[0] * self.height] * self.width
        self.next_grid_model: list[list[int]] = [[1] * self.height] * self.width
    
    def count_neighbor(self, row: int, col: int):
        count = 0

        if row-1 >= 0:
            count = count + grid[row-1][col]
        if (row-1 >= 0) and (col-1 >= 0):
            count = count + grid[row-1][col-1]
        if (row-1 >= 0) and (col+1 < self.width):
            count = count + grid[row-1][col+1]
        if col-1 >= 0:
            count = count + grid[row][col-1]
        if col + 1 < self.width:
            count = count + grid[row][col+1]
        if row + 1 < self.height:
            count = count + grid[row+1][col]
        if (row + 1 < self.height) and (col-1 >= 0):
            count = count + grid[row+1][col-1]
        if (row + 1 < self.height) and (col+1 < self.width):
            count = count + grid[row+1][col+1]
        return count

    def next_gen(self):
        for i in range(0, self.height):
            for j in range(0, self.width):
                cell = 0
                count = self.count_neighbor(i, j)

                if self.grid_model[i][j]==0 and count==3:
                    cell = 1
                elif self.grid_model[i][j]==1:
                    if count==2 or count==3:
                        cell = 1
                self.next_grid_model[i][j] = cell
        self.grid_model, self.next_grid_model = self.next_grid_model, self.grid_model

if __name__ == "__main__":
    
    HEIGHT = 10
    WIDTH = 10

    GRID_MODEL = [0] * HEIGHT
    NEXT_GRID_MODEL = [0] * HEIGHT
    for i in range(HEIGHT):
        GRID_MODEL[i] = [0] * WIDTH
        NEXT_GRID_MODEL[i] = [1] * WIDTH
    print(GRID_MODEL)
    print(f'\n\n{NEXT_GRID_MODEL}')