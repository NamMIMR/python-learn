import sys
sys.path.append('..')
from model import setup_model
from view import user_interface
from tkinter import *

grid_view = user_interface.setup_windows()
cell_size = user_interface.cell_size

def update_view():
    global grid_view

    grid_view = grid_view
    
    grid_view.delete('all')
    setup_model.next_gen()

    for i in range(0, setup_model.height):
        for j in range(0, setup_model.width):
            if setup_model.grid_model[i][j] == 1:
                draw_cell(i, j, 'black')

def draw_cell(height: int, width: int, color: str):
    global grid_view, cell_size

    if color.lower() == 'black':
        outline = 'grey'
    else:
        outline = 'white'

    grid_view.create_rectangle(row*cell_size,
                                col*cell_size,
                                row*cell_size + cell_size,
                                col*cell_size + cell_size,
                                fill=color, outline=outline)


if __name__ == "__main__":
    update_view()
    mainloop()