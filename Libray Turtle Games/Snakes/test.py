

import turtle
import time
import random

#Generate a screen

wn = turtle.Screen()
wn.title("hello in my game")
wn.setup(width = 300,height = 600)
wn.bgcolor("green")
wn.tracer(0)

# generate head of snake

head = turtle.Turtle()
head.color("black")
head.shape("square")
head.penup()
head.goto(0,0)
head.speed(0)
head.pensize(30)
head.direction = "stop"

#generate food

food = turtle.Turtle()
food.penup()
food.color("red")
food.shape("circle")
food.pensize(30)
food.goto(0,100)

#segments 

segments = []



def go_up():
    head.direction = "Up"

def go_down():
    head.direction = "Down"

def go_left():
    head.direction = "Left"

def go_right():
    head.direction = "Right"

def move():
    if head.direction == "Up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "Down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "Left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "Right":
        x = head.xcor()
        head.setx(x + 20)
        




#control snake
wn.listen()
wn.onkey(go_up,"Up")
wn.onkey(go_down,"Down")
wn.onkey(go_right,"Right")
wn.onkey(go_left,"Left")

while True:
    wn.update()

    if head.distance(food)<20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        
        

    for index in range(len(segments)-1,0,-1):
            
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    delay = 0.1
    time.sleep(delay)






wn.mainloop()
