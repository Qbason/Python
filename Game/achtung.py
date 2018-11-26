import turtle 
import random
import time


wn = turtle.Screen()
wn.setup(600,600)
wn.bgcolor("black")

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("white")
        self.shape("circle")
        self.speed_angle = 5
        self.speed_forward = 2
        #self.hideturtle()
        self.pensize(5)

    def angle_r(self):

        
        self.right(self.speed_angle)
        self.move()
        wn.update()

    def angle_l(self):
        
        
        self.left(self.speed_angle)
        self.move()
        wn.update()

    def move(self):
        self.forward(self.speed_forward)


Player_1 = Player()


wn.onkeypress(Player_1.angle_r,"Right")
wn.onkeypress(Player_1.angle_l,"Left")
wn.onkeypress(Player_1.move,"Up")
wn.listen()


wn.onclick(Player_1.goto)



wn.mainloop()