## ping pong

import turtle
import time

class Paddle(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.penup()
        self.color("white")
        self.speed(0)
        self.goto(0,0)


wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.bgcolor("black")
wn.title("New Game ping pong")
wn.tracer(0)
        
paddle_1 = Paddle()

paddle_1.goto(-280,0)


while True:


    wn.update()
    time.sleep(0.1)