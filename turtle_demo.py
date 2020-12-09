from turtle import Turtle, Screen

def draw_square(some_turtle):

    for _ in range(4):
        some_turtle.forward(200)
        some_turtle.right(90)

def draw_art():
    # Turtle Brad
    chad = Turtle(shape="turtle")
    chad.color("green")
    chad.pensize(5)
    chad.speed(0)  # 6/normal is the default so don't need to do it

    for _ in range(6):
        draw_square(chad)
        chad.right(60)



    # Turtle Brad
    brad = Turtle(shape="turtle")
    brad.color("yellow")
    brad.pensize(2)
    brad.speed(0)  # 6/normal is the default so don't need to do it

    for _ in range(36):
        draw_square(brad)
        brad.right(10)

    # Turtle Angie
    angie = Turtle(shape="turtle")
    angie.color("orange")
    angie.pensize(5)
    angie.speed(0)  # slightly slower than brad

    size = 1

    for _ in range(300):
        angie.forward(size)
        angie.right(91)
        size += 1

 # Turtle Angie
    todd = Turtle(shape="turtle")
    todd.color("red")
    todd.pensize(3)
    todd.speed(0)  # slightly slower than brad

    size = 1

    for _ in range(300):
        todd.forward(size)
        todd.right(91)
        size += 3
# Turtle Angie
    jane = Turtle(shape="turtle")
    jane.color("red")
    jane.pensize(3)
    jane.speed(0)  # slightly slower than brad

    size = 1

    for _ in range(600):
        jane.forward(size)
        jane.left(91)
        size += 3

window = Screen()
window.bgcolor("black")

draw_art()

window.exitonclick()