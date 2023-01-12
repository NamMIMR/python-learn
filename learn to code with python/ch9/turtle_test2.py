import turtle
from turtle import Turtle

def make_shape(the_turtle: Turtle) -> None:
    for i in range(5):
        the_turtle.forward(100)
        the_turtle.right(144)

if __name__ == "__main__":
    slowpoke = Turtle()
    slowpoke.shape('turtle')
    make_shape(slowpoke)

    turtle.mainloop()