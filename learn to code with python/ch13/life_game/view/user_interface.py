from tkinter import *
import sys
sys.path.append('..')
from model import setup_model

cell_size = 5

def setup_windows():
    global root, grid_view, cell_size, start_button, clear_button, choice, pause_button

    root = Tk()
    root.title('The Game of Life')

    grid_view = Canvas(root, width = setup_model.width*cell_size,
                    height = setup_model.height*cell_size,
                    borderwidth = 0,
                    highlightthickness = 0,
                    bg = 'white')

    start_button = Button(root, text = 'Start', width = 12)
    pause_button = Button(root, text = 'Pause', width = 12)
    clear_button = Button(root, text = 'Clear', width = 12)

    choice = StringVar(root)
    choice.set('Choose a Pattern')
    option = OptionMenu(root, choice, 'Choose a Pattern', 'glider', 'glider gun', 'random')
    option.config(width = 12)

    # grid_view.pack()
    # start_button.pack()
    # pause_button.pack()
    # clear_button.pack()
    # option.pack()

    grid_view.grid(row=0, columnspan=4, padx=20, pady=20)
    start_button.grid(row=1, column=0, sticky=W, padx=20, pady=20)
    pause_button.grid(row=1, column=1, sticky=W, padx=20, pady=20)
    option.grid(row=1, column=2, padx=20)
    clear_button.grid(row=1, column=3, sticky=E, padx=20, pady=20)

    return grid_view

if __name__ == "__main__":
    setup_windows()
    mainloop()