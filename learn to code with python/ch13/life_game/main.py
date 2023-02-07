from model import setup, grid_pattern



if __name__ == "__main__":
    grid = setup.grid_model
    next_grid = setup.next_grid_model
    height = setup.height
    width = setup.width

    # print(grid, height, width)
    random_grid = grid_pattern.randomize(grid, height, width)
    print(random_grid)