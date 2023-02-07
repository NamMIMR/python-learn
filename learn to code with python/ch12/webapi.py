import requests, json, turtle
from typing import Union

def setup() -> turtle.Turtle:
    screen = turtle.Screen()
    screen.setup(1000, 500)
    screen.bgpic('earth.gif')
    screen.setworldcoordinates(-180, -90, 180, 90)

    iss = turtle.Turtle()
    # iss.shape('circle')
    # iss.color('red')
    turtle.register_shape('iss.gif')
    iss.shape('iss.gif')
    return iss

def move_iss(iss: turtle.Turtle, lat: float, long: float) -> None:
    iss.penup()
    iss.goto(lat, long)
    iss.pendown()

def get_position() -> float or None:
    url = r'http://api.open-notify.org/iss-now.json'
    response = requests.get(url)
    # print(type(response))
    # print(response.status_code)
    # print(response.headers)
    # print(response.text)
    if response.status_code == 200:
        # print(response.text)
        response_dict = json.loads(response.text)
        position = response_dict['iss_position']
        print('International Space Station at ' + position['latitude'] + ', ' + position['longitude'])
        lat = float(position['latitude'])
        long = float(position['longitude'])
        return lat, long
    else:
        print('Houston, we have a problem:', response.status_code)

def main() -> None:
    iss = setup()
    lat, long = get_position()
    move_iss(iss, lat, long)
    turtle.mainloop()

if __name__ == "__main__":
    main()
