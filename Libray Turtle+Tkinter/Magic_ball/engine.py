#importing important libraies
import turtle, random, time

class Paddle(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(1,5)
        self.goto(0,-380)
        self.score = 0
        self.speedy = 20

    def left(self):
        x = self.xcor()
        self.setx(x-self.speedy)
    def right(self):
        x = self.xcor()
        self.setx(x+self.speedy)

        
class Block(turtle.Turtle):
    def __init__(self, strong = 0 ):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.penup()
        self.shape("square")
        self.color("white")
        self.strong = strong
        self.shapesize(0.9,0.9)
        self.goto(380,-280)

class Ball(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.9,0.9)
        self.goto(0,-350)
        self.x_speed = 6
        self.y_speed = 10
 
    def check_collision_with_paddle(self,paddle):

        x_p = paddle.xcor()
        y_p = paddle.ycor()
        s_p = paddle.shapesize()[1]

        x_b = self.xcor()
        y_b = self.ycor()

        if x_b>x_p-(s_p*20/2) and x_b <x_p+(s_p*20/2) and y_b==y_p+20 :
            self.y_speed*=-1


    def check_collision_with_block(self,mape):
        x = self.xcor()
        y = self.ycor()

        block = Block()
        block.color("black")
        
        for (x_b,y_b) in mape.blocks:
            
            if(     x_b >=x-20 and x_b<=x+20 and y_b<=y+20 and y_b>=y-20       ):
                block.goto(x_b,y_b)
                block.stamp()
                mape.blocks.remove((x_b,y_b))
                
                self.y_speed*=-1

        del block

    def check_collision_with_wall(self):
        x = self.xcor()
        y = self.ycor()
        if(x<-280 or x>280):
            self.x_speed*=-1
        
        if(y>390):
            self.y_speed*=-1

    def check_too_far(self):
        y = self.ycor()

        if y<-370:
            #self.goto(0,-350)
            self.y_speed*=-1
            time.sleep(1)

    def go(self):
        x = (self.xcor() +   self.x_speed)
        y = (self.ycor() +   self.y_speed)
        self.goto(x,y)

class Map():
    def __init__(self):
        self.level = 1
        self.blocks = []
        
    def generate_map(self):

        block = Block()

        for i in range(-10,20):
            for j in range(-14,15):
                if random.randint(0,0) or (i+j)%2==0:
                    y = i*20
                    x = j*20
                    block.goto(x,y)
                    block.stamp()
                    self.blocks.append( (x,y) )

        block.goto(1000,1000)
        del block




#environment
#generating screen
wn = turtle.Screen()
wn.setup(600,800)
wn.delay(0)
wn.bgcolor("black")


desk = Paddle()
maps = Map()
maps.generate_map()
ball = Ball()

wn.listen()

wn.onkeypress(desk.left,"a")
wn.onkeypress(desk.right,"d")



time.sleep(1)

while True:
   
    ball.go()

    ball.check_collision_with_wall()
    ball.check_collision_with_paddle(desk)
    ball.check_too_far()
    ball.check_collision_with_block(maps)

    time.sleep(0.1)


wn.mainloop()