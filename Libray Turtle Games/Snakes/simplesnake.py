import turtle
import time
import random

#generate screen
wn = turtle.Screen()
wn.tracer(0)
wn.setup(600,600)
wn.bgcolor("white")
wn.stay = True

def Up():
    snake.direction = "Up"

def Down():
    snake.direction = "Down"

def Left():
    snake.direction = "Left"

def Right():
   snake.direction = "Right"




def direction():
    d = snake.direction
    print(d)
    speed = 10

    if d == "Up":
         y = snake.ycor()
         snake.sety(y+speed)

    if d == "Down":
         y = snake.ycor()
         snake.sety(y-speed)

    if d == "Left":
         x = snake.xcor()
         snake.setx(x-speed)

    if d == "Right":
         x = snake.xcor()
         snake.setx(x+speed)


def exit():
    wn.stay = False
    return not wn.stay

#generate snake // turtle

snake = turtle.Turtle()
snake.shape("square")
snake.penup()
snake.speed()
snake.color("black")
snake.goto(0,0)
snake.direction = "stop"


wn.listen()
wn.onkey(Up,"Up")
wn.onkey(Down,"Down")
wn.onkey(Left,"Left")
wn.onkey(Right,"Right")
wn.onkey(exit,"q")



while wn.stay:
    wn.update()
    direction()



    time.sleep(0.1)

# wn.mainloop()