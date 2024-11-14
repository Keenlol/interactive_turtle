import turtle

def move_forward():
     turtle.forward(100)

turtle.onkey(move_forward, "Up")

turtle.listen()
turtle.done()