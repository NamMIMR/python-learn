from tkinter import *
import model


class GridView:
    def __init__(self) -> None:
        self.grid_model = model.GridModel()
        self.grid_model.setup_model()

        self.cell_size = 5
        self.is_running = False

        self.root = Tk()
        self.root.title("The Game of Life")
        self.grid_view = Canvas(
            self.root,
            width=self.grid_model.width * self.cell_size,
            height=self.grid_model.height * self.cell_size,
            borderwidth=0,
            highlightthickness=0,
            bg="white",
        )
        self.start_button = Button(self.root, text="Start", width=12)
        self.clear_button = Button(self.root, text="Clear", width=12)
        self.choice = StringVar(self.root)
        self.choice.set("Choose a Pattern")
        self.option = OptionMenu(
            self.root,
            self.choice,
            "Choose a Pattern",
            "GLIDER",
            "GLIDER_GUN",
            "RANDOM",
            command=self.option_handler,
        )
        self.option.config(width=12)

    def setup_grid_view(self):
        self.grid_view.grid(row=0, columnspan=3, padx=20, pady=20)
        self.grid_view.bind("<Button-1>", self.grid_handler)
        self.start_button.grid(row=1, column=0, sticky=W, padx=20, pady=20)
        self.start_button.bind("<Button-1>", self.start_handler)
        self.option.grid(row=1, column=1, padx=20)
        self.clear_button.grid(row=1, column=2, sticky=E, padx=20, pady=20)
        self.clear_button.bind("<Button-1>", self.clear_handler)

    def option_handler(self, event):
        self.is_running = False
        self.start_button.configure(text="Start")

        selection = self.choice.get()

        if selection == "RANDOM":
            self.grid_model.load_pattern("RANDOM")
        else:
            self.grid_model.load_pattern(selection, 10, 10)

        self.update()

    def start_handler(self, event):
        if self.is_running:
            self.is_running = False
            self.start_button.configure(text="Start")
        else:
            self.is_running = True
            self.start_button.configure(text="Pause")
            self.update()

    def clear_handler(self, event):
        self.is_running = False
        self.grid_model.initial_model()
        self.start_button.configure(text="Start")
        self.update()

    def grid_handler(self, event):
        x = int(event.x / self.cell_size)
        y = int(event.y / self.cell_size)

        if self.grid_model.grid_model[x][y] == 1:
            self.grid_model.grid_model[x][y] = 0
            self.draw_cell(x, y, "white")
        else:
            self.grid_model.grid_model[x][y] = 1
            self.draw_cell(x, y, "black")

    def update(self):
        self.grid_view.delete(ALL)

        self.grid_model.next_gen()
        for i in range(0, self.grid_model.height):
            for j in range(0, self.grid_model.width):
                if self.grid_model.grid_model[i][j] == 1:
                    self.draw_cell(i, j, "black")

        if self.is_running:
            self.root.after(100, self.update)

    def draw_cell(self, row: int, col: int, color: str):
        if color == "black":
            outline = "gray"
        else:
            outline = "white"

        self.grid_view.create_rectangle(
            row * self.cell_size,
            col * self.cell_size,
            row * self.cell_size + self.cell_size,
            col * self.cell_size + self.cell_size,
            fill=color,
            outline=outline,
        )


if __name__ == "__main__":
    GRIDVIEW = GridView()
    GRIDVIEW.setup_grid_view()
    GRIDVIEW.update()
    mainloop()
