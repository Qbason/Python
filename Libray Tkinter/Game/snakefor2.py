


#import the turtle
import turtle
import time
import random

wn = turtle.Screen()

width_wall = 600
heigth_wall = 600

wn.setup(width_wall,heigth_wall)
wn.bgcolor("green")
wn.title("Snake for 2 people")
wn.tracer(0)
wn.register_shape("head.gif")
wn.register_shape("body.gif")




class Snake(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("black")
        self.shape("square")
        self.penup()
        self.shape("head.gif")
        self.speed(0)
        self.goto(random.randint(-270,270),random.randint(-270,270))
        self.direction = "stop"
        self.segments = []
        self.snake_speed = 20

    def up(self):
        self.direction = "up"
        #self.left(180)
        
    def down(self):
        self.direction = "down"
        #self.right(180)
        
    def left(self):
        self.direction = "left"
        #print(self.left(90))

    def right(self):
        self.direction = "right"
        #self.right(90)

    def stop(self):
        self.direction = "stop"
        

    def move(self):
        speed = self.snake_speed
        
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

    def meetfood(self,nameoffood):

        if(self.distance(nameoffood)<20):

            nameoffood.goto(random.randint(-270,270),random.randint(-270,270))
            # Creating a body for our snake
            for var in range(0,nameoffood.amount,1):
                a = BodyofSnake()
                a.goto(1000,1000)
                self.snake_speed = self.snake_speed + nameoffood.snake_speed

                self.segments.append(a)


    def showsegments(self):
        for var in range(len(self.segments)-1,0,-1):
            x = self.segments[var-1].xcor()
            y = self.segments[var-1].ycor()
            self.segments[var].goto(x,y)
        
        if len(self.segments)>0:
            x = self.xcor()
            y = self.ycor()
            self.segments[0].goto(x,y)


    def check_collision_with_body(self):
        for var in self.segments:
            if var.distance(self) < 20:
                var.goto(1000,1000)
                index = self.segments.index(var)
                for var in range(len(self.segments),index,-1):
                    self.segments[index].goto(1000,1000)
                    del self.segments[index]

    def check_collision_with_other(self,second_snake):
        
        for var in second_snake.segments:
                if var.distance(self) < 20:
                    var.goto(1000,1000)
                    index = second_snake.segments.index(var)
                    for var in range(len(second_snake.segments),index,-1):
                        second_snake.segments[index].goto(1000,1000)
                        del second_snake.segments[index]

    def check_collision_with_wall(self):
        if self.xcor() > ((width_wall/2)-10) or self.xcor() < ((-1*width_wall/2)+10):
            for var in self.segments:
                var.goto(1000,1000)
            self.segments.clear()
            self.goto(0,0)
    

class BodyofSnake(turtle.Turtle):
    def __init__(self):
            turtle.Turtle.__init__(self)
            self.color("grey")
            self.shape("square")
            self.penup()
            self.speed(0)
            self.shape("body.gif")
            print("HELLO")


class Food(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("red")
        self.shape("circle")
        self.penup()
        self.goto(random.randint(-270,270),random.randint(-270,270))
        self.speed(0)
        self.amount = 1
        self.snake_speed = 0

        

        
Food_1 = Food()
Food_2 = Food()

Big_Food = Food()
Big_Food.color("yellow")
Big_Food.amount = 5
Big_Food.snake_speed = 1


Player_1 = Snake()
Player_1.color("brown")
Player_2 = Snake()
Player_2.color("orange")



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
    Player_1.meetfood(Big_Food)

    Player_1.showsegments()
    

    Player_2.meetfood(Food_1)
    Player_2.meetfood(Food_2)
    Player_2.meetfood(Big_Food)

    Player_2.showsegments()
    

    Player_1.move()
    Player_1.check_collision_with_body()
    


    Player_2.move()
    Player_2.check_collision_with_body()

    Player_1.check_collision_with_other(Player_2)
    Player_2.check_collision_with_other(Player_1)
    
    Player_1.check_collision_with_wall()



    time.sleep(0.1)
wn.mainloop()