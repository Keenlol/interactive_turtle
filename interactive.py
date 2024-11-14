import turtle

SPEED = 10

def move_up():
    if turtle.heading != 90:
        turtle.setheading(90)
    turtle.forward(SPEED)

def move_down():
    if turtle.heading != 270:
        turtle.setheading(270)
    turtle.forward(SPEED)

def move_left():
    if turtle.heading != 180:
        turtle.setheading(180)
    turtle.forward(SPEED)

def move_right():
    if turtle.heading != 0:
        turtle.setheading(0)
    turtle.forward(SPEED)

turtle.speed(0)

turtle.onkey(move_up, "Up")
turtle.onkey(move_down, "Down")
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")


turtle.listen()
turtle.done()
