from tkinter import *
import model.setup

cell_size = 5

def setup():
    global root, grid_view, cell_size, start_button, clear_button, choice, pause_button

    root = Tk()
    root.title('The Game of Life')

    grid_view = Canvas(root, width = setup.width*cell_size,
                    height = setup.height*cell_size,
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

    grid_view.pack()
    start_button.pack()
    pause_button.pack()
    clear_button.pack()
    option.pack()

if __name__ == "__main__":
    setup()
    mainloop()