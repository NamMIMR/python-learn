import turtle, time, asyncio
from turtle import Turtle


async def make_square(the_turtle: Turtle) -> None:
    for i in range(4):
        the_turtle.forward(100)
        the_turtle.right(90)

async def make_spiral(the_turtle: Turtle) -> None:
    for i in range(36):
        await make_square(the_turtle)
        the_turtle.right(10)

async def main() -> None:
    slowpoke = Turtle()
    slowpoke.shape('turtle')
    slowpoke.color('blue')
    pokey = Turtle()
    pokey.shape('turtle')
    pokey.color('red')

    # await make_square(slowpoke)
    # pokey.right(45)
    # await make_square(pokey)

    await make_spiral(slowpoke)
    pokey.right(5)
    await make_spiral(pokey)


    turtle.mainloop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = [main()]
    resp = loop.run_until_complete(asyncio.gather(*tasks))
    print(resp)
    