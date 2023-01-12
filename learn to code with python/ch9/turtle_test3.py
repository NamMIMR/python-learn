import turtle
from turtle import Turtle

def make_shape(the_turtle: Turtle) -> None:
    for i in range(5):
        the_turtle.forward(100)
        the_turtle.right(144)

if __name__ == "__main__":
    slowpoke = Turtle()
    slowpoke.shape('turtle')
    slowpoke.pencolor('blue')
    slowpoke.penup()
    slowpoke.setposition(-120, 0)
    slowpoke.pendown()
    slowpoke.circle(50)
    make_shape(slowpoke)

    slowpoke.pencolor('red')
    slowpoke.penup()
    slowpoke.setposition(120, 0)
    slowpoke.pendown()
    slowpoke.circle(50)
    make_shape(slowpoke)

    turtle.mainloop()