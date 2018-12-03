


#import the turtle
import turtle
import time
import random

wn = turtle.Screen()
wn.setup(600,600)
wn.bgcolor("green")
wn.title("Snake for 2 people")
wn.tracer(0)


class HeadOfTurtle(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("black")
        self.shape("square")
        self.penup()
        self.speed(0)
        self.goto(random.randint(-270,270),random.randint(-270,270))
        self.direction = "stop"
        self.segments = []

    def up(self):
        self.direction = "up"
        
    def down(self):
        self.direction = "down"
        
    def left(self):
        self.direction = "left"

    def right(self):
        self.direction = "right"
    def stop(self):
        self.direction = "stop"
        

    def move(self):
        speed = 25
        if(self.direction =="left"):
            x = self.xcor()
            self.setx(x-speed)
        if(self.direction =="right"):
            x = self.xcor()
            self.setx(x+speed)
        if(self.direction =="down"):
            y = self.ycor()
            self.sety(y-speed)
        if(self.direction =="up"):
            y = self.ycor()
            self.sety(y+speed)        

    def meetfood(self,name_food):
        if self.distance(name_food)<20:
            name_food.random_location()
            a = Segment()
            self.segments.append(a)

    def showsegments(self):
        for var in range(len(self.segments)-1,0,-1):
             x = self.segments[var-1].xcor()
             y = self.segments[var-1].ycor()
             self.segments[var].goto(x,y)
        if len(self.segments)>0:
            y = self.ycor()
            x = self.xcor()
            self.segments[0].goto(x,y)

             

class Segment(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("gray")
        self.shape("square")
        self.penup()
        self.speed(0)
        



class Food(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("red")
        self.shape("circle")
        self.penup()
        self.speed(0)
    def random_location(self):
        self.goto(random.randint(-270,270),random.randint(-270,270))
        
        
        
#declartion of food
Food_1 = Food()
Food_2 = Food()

# random location for food
Food_1.random_location()
Food_2.random_location()

#declarate players
Player_1 = HeadOfTurtle()
Player_2 = HeadOfTurtle()

#declarate a segment for each player
# Player_1_s = Segment()
# Player_2_s = Segment()


wn.listen()
wn.onkey(Player_1.up,"Up")
wn.onkey(Player_1.down,"Down")
wn.onkey(Player_1.left,"Left")
wn.onkey(Player_1.right,"Right")
wn.onkey(Player_1.stop,"m")

wn.onkey(Player_2.up,"w")
wn.onkey(Player_2.down,"s")
wn.onkey(Player_2.right,"d")
wn.onkey(Player_2.left,"a")
wn.onkey(Player_2.stop,"n")









while True:
    wn.update()

    
    Player_1.meetfood(Food_1)
    Player_1.meetfood(Food_2)
    Player_1.showsegments()

    Player_2.meetfood(Food_1)
    Player_2.meetfood(Food_2)
    Player_2.showsegments()

  
    Player_1.move()
    Player_2.move()



    time.sleep(0.1)
wn.mainloop()