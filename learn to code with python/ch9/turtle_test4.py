import turtle
from turtle import Turtle

def make_shape(t: Turtle, sides: int) -> None:
    angle = 360/sides
    for i in range(0, sides):
        t.forward(100)
        t.right(angle)


if __name__ == "__main__":
    slowpoke = Turtle()
    slowpoke.shape('turtle')
    make_shape(slowpoke, 3)
    make_shape(slowpoke, 5)
    make_shape(slowpoke, 8)
    make_shape(slowpoke, 10)