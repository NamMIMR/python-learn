import random


class GridModel:
    def __init__(self):
        self.height: int = 100
        self.width: int = 100

    def setup_model(self):
        self.grid_model: list[list[int]] = [[0] * self.height] * self.width
        self.next_grid_model: list[list[int]] = [[1] * self.height] * self.width

    def count_neighbor(self, row: int, col: int) -> int:
        count = 0

        if row-1 >= 0:
            count = count + self.grid_model[row-1][col]
        if (row-1 >= 0) and (col-1 >= 0):
            count = count + self.grid_model[row-1][col-1]
        if (row-1 >= 0) and (col+1 < self.width):
            count = count + self.grid_model[row-1][col+1]
        if col-1 >= 0:
            count = count + self.grid_model[row][col-1]
        if col + 1 < self.width:
            count = count + self.grid_model[row][col+1]
        if row + 1 < self.height:
            count = count + self.grid_model[row+1][col]
        if (row + 1 < self.height) and (col-1 >= 0):
            count = count + self.grid_model[row+1][col-1]
        if (row + 1 < self.height) and (col+1 < self.width):
            count = count + self.grid_model[row+1][col+1]
        return count

    def next_gen(self) -> None:
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

    def load_pattern(self, pattern: list[list[int]], x_offset: int = 0, y_offset: int = 0) -> None:
        for i in range(0, self.height):
            for j in range(0, self.width):
                self.grid_model[i][j] = 0

        j = y_offset

        for row in pattern:
            i = x_offset
            for value in row:
                self.grid_model[i][j] = value
                i += 1
            j += 1

if __name__ == "__main__":

    grid_model = GridModel()
    grid_model.setup_model()
