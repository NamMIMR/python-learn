import random


HEIGHT = 100
WIDTH = 100

GRID_MODEL = [0] * HEIGHT
NEXT_GRID_MODEL = [0] * HEIGHT
for i in range(HEIGHT):
    GRID_MODEL[i] = [0] * WIDTH
    NEXT_GRID_MODEL[i] = [1] * WIDTH

GLIDER_PATTERN = [[0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0]]

GLIDER_GUN_PATTERN = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def randomize(grid, width, height):
    for i in range(0, height):
        for j in range(0, width):
            grid[i][j] = random.randint(0,1)

def next_gen():
    global GRID_MODEL, NEXT_GRID_MODEL

    for i in range(0, HEIGHT):
        for j in range(0, WIDTH):
            cell = 0
            count = count_neighbors(GRID_MODEL, i, j)

            if GRID_MODEL[i][j] == 0:
                if count == 3:
                    cell = 1
            elif GRID_MODEL[i][j] == 1:
                if count==2 or count==3:
                    cell = 1
            NEXT_GRID_MODEL[i][j] = cell

    GRID_MODEL, NEXT_GRID_MODEL = NEXT_GRID_MODEL, GRID_MODEL

def count_neighbors(grid, row, col):
    count = 0
    if row-1 >= 0:
        count = count + grid[row-1][col]
    if (row-1 >= 0) and (col-1 >= 0):
        count = count + grid[row-1][col-1]
    if (row-1 >= 0) and (col+1 < width):
        count = count + grid[row-1][col+1]
    if col-1 >= 0:
        count = count + grid[row][col-1]
    if col + 1 < width:
        count = count + grid[row][col+1]
    if row + 1 < height:
        count = count + grid[row+1][col]
    if (row + 1 < height) and (col-1 >= 0):
        count = count + grid[row+1][col-1]
    if (row + 1 < height) and (col+1 < width):
        count = count + grid[row+1][col+1]
    return count

def load_pattern(pattern, x_offset=0, y_offset=0):
    global GRID_MODEL

    for i in range(0, HEIGHT):
        for j in range(0, WIDTH):
            GRID_MODEL[i][j] = 0
    
    j = y_offset

    for row in pattern:
        i = x_offset
        for value in row:
            GRID_MODEL[i][j] = value
            i += 1
        j += 1


if __name__ == "__main__":
    next_gen()
    