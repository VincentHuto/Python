from turtle import Turtle, Screen
import random
import math
def draw_square(some_turtle):

    for _ in range(4):
        some_turtle.forward(200)
        some_turtle.right(90)

def draw_art():
# Turtle Angie
    dick = Turtle(shape="turtle")
    dick.color("blue")
    dick.pensize(3)
    dick.speed(0)  # slightly slower than brad
    size = 1
# Turtle Angie
    jane = Turtle(shape="turtle")
    jane.color("green")
    jane.pensize(3)
    jane.speed(0)  # slightly slower than brad
    size = 1

# Turtle Angie
    alec = Turtle(shape="turtle")
    alec.color("yellow")
    alec.pensize(3)
    alec.speed(0)  # slightly slower than brad
    size = 1
# Turtle Angie
    trent = Turtle(shape="turtle")
    trent.color("pink")
    trent.pensize(3)
    trent.speed(0)  # slightly slower than brad
    size = 1

# Turtle Angie
    alyysa = Turtle(shape="turtle")
    alyysa.color("red")
    alyysa.pensize(3)
    alyysa.speed(0)  # slightly slower than brad
    size = 1
# Turtle Angie
    coc = Turtle(shape="turtle")
    coc.color("orange")
    coc.pensize(3)
    coc.speed(0)  # slightly slower than brad
    size = 1


    for _ in range(150):
        jane.forward(size)
        jane.left(90+(random.randint(90,120)*math.tan(_)))
        size += random.randint(0,3)
        dick.forward(size)
        dick.left(90+(random.randint(90,120)*math.sin(_)))
        size += random.randint(0,3)

        trent.forward(size)
        trent.left(90+(random.randint(90,120)*math.tanh(_)))
        size += random.randint(0,3)
        alec.forward(size)
        alec.left(90+(random.randint(90,120)*math.cos(_)))
        size += random.randint(0,3)

        coc.forward(size)
        coc.left(90+(random.randint(90,120)*math.tanh(_)))
        size += random.randint(0,3)
        alyysa.forward(size)
        alyysa.left(90+(random.randint(20,30)*math.sin(_)))
        size += random.randint(0,3)


window = Screen()
window.bgcolor("black")

draw_art()

window.exitonclick()