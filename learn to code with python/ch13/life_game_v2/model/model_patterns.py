from abc import abstractmethod
from random import randint

class GridModel:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width

    def setup_model(self):
        self.start_model = [[0] * self.width for i in range(0, self.height)]
        self.next_model = [[0] * self.width for i in range(0, self.height)]
        # return self.start_model, self.next_model

    def count_neighbors(self, row: int, col: int) -> int:
        count = 0

        if row-1 >= 0:
            count = count + self.start_model[row-1][col]
        if (row-1 >= 0) and (col-1 >=  0):
            count = count + self.start_model[row-1][col-1]
        if (row-1 >= 0) and (col+1 < self.width):
            count = count + self.start_model[row-1][col+1]
        if col-1 >= 0:
            count = count + self.start_model[row][col-1]
        if col+1 < self.width:
            count = count + self.start_model[row][col+1]
        if row+1 < self.height:
            count = count + self.start_model[row+1][col]
        if (row+1 < self.height) and (col-1 >=0):
            count = count + self.start_model[row+1][col-1]
        if (row+1 < self.height) and (col+1 < self.width):
            count = count + self.start_model[row+1][col+1]

        return count

    def gen_next(self):
        for i in range(0, self.height):
            for j in range(0, self.width):
                cell = 0
                neighbors = self.count_neighbors(i, j)

                if self.start_model[i][j] == 0 & neighbors == 3:
                    cell = 1
                elif self.start_model[i][j] == 1 & (neighbors==2 or neighbors==3):
                    cell = 1
                self.next_model[i][j] = cell
        self.start_model, self.next_model = self.next_model, self.start_model


class RandomGridModel(GridModel):
    def __init__(self, height: int, width: int):
        super().__init__(height, width)

    def setup_model(self):
        super().setup_model()
        for i in range(0, self.height):
            for j in range(0, self.width):
                self.start_model[i][j] = randint(0, 1)
