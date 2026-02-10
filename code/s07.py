import jupyturtle
from jupyturtle import make_turtle, forward, left


def draw_spiral(n, size):
    "draw one squar, turn at angle, then draw another and so own "
    make_turtle(delay=0.01)
    for i in range(n):
        draw_square(size)
        left(10)

def draw_square(size):
        for i in range(4):
            forward(size)
            left(90)

draw_spiral(30,40)