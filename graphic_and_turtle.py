from turtle import Turtle, Screen
from graphics import *


def draw_square(some_turtle):
    for _ in range(4):
        some_turtle.forward(200)
        some_turtle.right(90)


def draw_art():
    # Turtle Brad
    brad = Turtle(shape="turtle")
    brad.color("green")
    brad.pensize(7)
    brad.speed(0)  # 6/normal is the default so don't need to do it

    for _ in range(36):
        draw_square(brad)
        brad.right(10)

    # Turtle Brad
    brad = Turtle(shape="turtle")
    brad.color("red")
    brad.pensize(3)
    brad.speed(0)  # 6/normal is the default so don't need to do it

    for _ in range(36):
        draw_square(brad)
        brad.right(10)


    # Turtle Angie
    angie = Turtle(shape="turtle")
    angie.color("blue")
    angie.pensize(2)
    angie.speed(0)  # slightly slower than brad

    size = 1

    for _ in range(300):
        angie.forward(size)
        angie.right(420)
        size += 1

    # Turtle Angie
    angie = Turtle(shape="turtle")
    angie.color("pink")
    angie.pensize(2)
    angie.speed(0)  # slightly slower than brad

    size = 1

    for _ in range(300):
        angie.forward(size)
        angie.right(69)
        size += 1


window = Screen()
window.bgcolor("black")

draw_art()

window.exitonclick()
