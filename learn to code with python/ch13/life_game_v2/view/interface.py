from tkinter import *
# from ..model import GridModel
import sys
sys.path.append('../')
from model.model_patterns import GridModel


class BaseWindow:
    """_summary_
    """
    def __init__(self, cell_size: int, model: GridModel) -> None:
        self.cell_size = cell_size
        self.model = model

    def setup_interface(self):
        global root, grid_view, cell_size, start_button, clear_button, choice

        self.root = Tk()
        self.root.title("The Game of Life")

        self.grid_view = Canvas(self.root,
                                width=self.model.width*self.cell_size,
                                height=self.model.height*self.cell_size,
                                borderwidth=0,
                                highlightthickness=0,
                                bg="white")

        self.start_button = Button(self.root, text="Start", width=12)
        self.clear_button = Button(self.root, text="Clear", width=12)
        self.choice = StringVar(self.root)
        self.choice.set("Choose a Pattern")
        self.options = OptionMenu(self.root, self.choice, "Choose a Pattern", "glider", "glider gun", "random")
        self.options.config(width=12)

        self.grid_view.grid(row=0, columnspan=3, padx=20, pady=20)
        self.start_button.grid(row=1, column=0, sticky=W, padx=20, pady=20)
        self.options.grid(row=1, column=1, padx=20)
        self.clear_button.grid(row=1, column=2, sticky=E, padx=20, pady=20)


if __name__ == "__main__":
    model = GridModel(100, 100)
    grid_view = BaseWindow(100, model)
    grid_view.setup_interface()
    mainloop()
