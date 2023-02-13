

class GridModel:
    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width

    def start_model(self) -> None:
        self.start_model = [[0] * self.width for i in range(0, self.height)]

    def next_model(self) -> None:
        pass

    def gen_next(self):
        pass
