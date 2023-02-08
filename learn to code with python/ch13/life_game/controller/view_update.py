import sys
sys.path.append('..')
from model import setup_model
from view import user_interface

grid_view = user_interface.setup_windows()

def update_view():
    global grid_view

    grid_view = grid_view
    
    grid_view.delete(ALL)
    setup_model.next_gen()

    for i in range(0, setup_model.height):
        for j in range(0, setup_model.width):
            if setup_model.grid_model[i][j] == 1:
                draw_cell(i, j, 'black')

def draw_cell(height: int, width: int, color: str):
    pass


if __name__ == "__main__":
    update_view()