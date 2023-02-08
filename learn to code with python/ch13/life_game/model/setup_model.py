from typing import List


height = 100
width = 100

grid_model = [0] * height
next_grid_model = [0] * height

for i in range(height):
    grid_model[i] = [0] * width
    next_grid_model[i] = [0] * width


# grid_model = setup()

def next_gen():
    global grid_model, next_grid_model

    for i in range(0, height):
        for j in range(0, width):
            cell = 0
            print('Checking cell', i, j)
            neighbor = count_neighbors(grid_model, i, j)

            if grid_model[i][j] == 0:
                if neighbor == 3:
                    cell = 1
            elif grid_model[i][j] == 1:
                if neighbor == 2 or neighbor == 3:
                    cell = 1
            next_grid_model[i][j] = cell
            print('New value is', next_grid_model[i][j])
    
    grid_model, next_grid_model = next_grid_model, grid_model

def count_neighbors(grid_model: List[List[int]], row: int, col: int) -> int:
    count = 0

    if row-1 >= 0:
        count = count + grid_model[row-1][col]
    if (row-1 >= 0) and (col-1 >=  0):
        count = count + grid_model[row-1][col-1]
    if (row-1 >= 0) and (col+1 < width):
        count = count + grid_model[row-1][col+1]
    if col-1 >= 0:
        count = count + grid_model[row][col-1]
    if col+1 < width:
        count = count + grid_model[row][col+1]
    if row+1 < height:
        count = count + grid_model[row+1][col]
    if (row+1 < height) and (col-1 >=0):
        count = count + grid_model[row+1][col-1]
    if (row+1 < height) and (col+1 < width):
        count = count + grid_model[row+1][col+1]
    
    return count

if __name__ == "__main__":
    next_gen()