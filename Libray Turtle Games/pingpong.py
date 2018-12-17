# ping pong easy game

import turtle
import random
import time


class Paddle(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("white")
        self.shape("square")
        self.speed(0)
        self.penup()
        # size 100x20
        self.shapesize(5, 1)

    def up(self):
        y = self.ycor()
        self.sety(y+15)

    def down(self):
        y = self.ycor()
        self.sety(y-15)


class ExtraBall(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("orange")
        self.shape("circle")
        self.speed(0)
        self.penup()
        self.goto(0, 0)
        self.yspeed = 6
        self.xspeed = 4



class Ball(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("white")
        self.shape("circle")
        self.speed(0)
        self.penup()
        self.goto(0, 0)
        self.yspeed = 5
        self.xspeed = 3

    def move(self,paddle1,paddle2):
        x = self.xcor()+self.xspeed
        y = self.ycor()+self.yspeed
        self.goto(x, y)
        time.sleep(0.02)
        self.collision(paddle1,paddle2)

    def collision(self,paddle1,paddle2):
        x = self.xcor()
        y = self.ycor()
        if(y > 290 or y < -290):
            self.yspeed *= -1 
            #self.xspeed *=-1

        if(x > 320 or x<-320):
            #self.yspeed *=-1
            self.goto(0,0)
            

        y_p1 = paddle1.ycor()
        y_p2 = paddle2.ycor()

        if(     x <-310 and (y_p1+50>y and y_p1-50<y)  )     :
            self.xspeed *= -1

        if(     x >310 and (y_p2+50>y and y_p2-50<y)  )     :
            self.xspeed *= -1


     


wn = turtle.Screen()
wn.setup(width=700, height=600)
wn.bgcolor("black")
wn.title("Ping Pong")
wn.delay(0)


Paddle_one = Paddle()
Paddle_one.goto(-330, 0)

Paddle_two = Paddle()
Paddle_two.goto(320, 0)

wn.listen()
wn.onkeypress(Paddle_one.up, "Up")
wn.onkeypress(Paddle_one.down, "Down")

wn.onkeypress(Paddle_two.up, "w")
wn.onkeypress(Paddle_two.down, "s")

Ball = Ball()


while True:

    Ball.move(Paddle_one,Paddle_two)

  

wn.mainloop()
