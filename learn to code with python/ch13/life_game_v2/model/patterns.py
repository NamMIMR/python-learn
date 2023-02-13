from abc import abstractmethod


class GridModel:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width

    def setup_model(self):
        self.start_model = [[0] * self.width for i in range(0, self.height)]
        self.next_model = [[0] * self.width for i in range(0, self.height)]
        return self.start_model, self.next_model

    def gen_next(self):
        pass
