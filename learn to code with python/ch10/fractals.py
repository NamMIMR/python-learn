import turtle


def setup(pencil: turtle.Turtle) -> None:
    pencil.color('blue')
    pencil.penup()
    pencil.goto(-200, 100)
    pencil.pendown()

def koch(pencil: turtle.Turtle, size: int, order: int) -> None:
    if order == 0:
        pencil.forward(size)

    else:
        for angle in [60, -120, 60, 0]:
            koch(pencil, size/3, order-1)
            pencil.left(angle)

def main() -> None:
    pencil = turtle.Turtle()
    setup(pencil)

    order = 5
    size = 400
    # koch(pencil, size, order)
    for i in range(3):
        koch(pencil, size, order)
        pencil.right(120)


if __name__ == "__main__":
    main()
    turtle.tracer(100)
    turtle.mainloop()