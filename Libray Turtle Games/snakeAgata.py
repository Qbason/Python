

import turtle
import time
import random


wn = turtle.Screen()
wn.setup(width=600,height=600)
wn.bgcolor("blue")
wn.tracer(0)



def up(self):
    self.direction = "Up"

def down(self):
    self.direction = "Down"

def left(self):
    self.direction = "Left"

def right(self):
    self.direction = "Right"

def move(self):
    if self.direction == "Up":
        y = self.ycor()
        self.sety(y+15)
    if self.direction == "Down":
        y = self.ycor()
        self.sety(y-15)
    if self.direction == "Left":
        x = self.xcor()
        self.setx(x-15)
    if self.direction == "Right":
        x = self.xcor()
        self.setx(x+15)


    

#left right up down
class head(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape("circle")
        self.penup()
        self.direction="stop"

class food(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.color("white")
        self.penup()
        self.shape("circle")
        self.segments = []


Agata = head()
segments_a = []
Kuba = head()
segments_k = []

Agata.color("ping")
Agata.goto(200,200)
Kuba.color("red")
Kuba.goto(-200,-200)

food_1 = food()
food_1.goto(10,10)

food_2 = food()
food_2.goto(-10,-10)








wn.listen()
wn.onkey(up(Agata),"Up")
wn.onkey(up(Agata),"w")
wn.onkey(down(Agata),"Down")
wn.onkey(down(Kuba),"s")
wn.onkey(left(Agata),"Left")
wn.onkey(left(Kuba),"a")
wn.onkey(right(Agata),"Right")
wn.onkey(right(Kuba),"d")





while True:
    wn.update()
    
    if Kuba.distance(food_1)<20:
        x = random.randint(-270,270)
        y = random.randint(-270,270)
        food_1.goto(x,y)
    if Kuba.distance(food_2)<20:
        x = random.randint(-270,270)
        y = random.randint(-270,270)
        food_2.goto(x,y)

        segment = turtle.Turtle()
        segment.color("grey")
        segment.speed(0)
        segment.shape("circle")
        segment.penup()
        segments_a.append(segment)

    for var in range(len(segments_a)-1,0,-1):
        y = segments_a[var-1].ycor()
        x = segments_a[var-1].xcor()
        segments_a[var].goto(x,y)

    if len(segments_a)>0:
       y = head.ycor()
       x = head.xcor()
       segments_a[0].goto(x,y)
      
        


    move(Kuba)
    move(Agata)
    time.sleep(0.1)


wn.mainloop()