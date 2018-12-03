

import turtle
import random
import time



wn = turtle.Screen()
wn.setup(800,800)
wn.bgcolor("black")
wn.title("Witam w Achtungu")
wn.loop = True

turtle.delay(0)


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("white")
        self.pensize(5)
        self.angle = 5
        self.speed = 2
        self.hideturtle()
        self.cords = []
        
    def angle_r(self):
        self.right(self.angle)

    def angle_l(self):
        self.left(self.angle)

    def move(self):
        self.forward(self.speed)
        x = self.xcor()
        y = self.ycor()
        self.cords.append([x,y])
        print(len(self.cords))
    def check_collision(self):
        x = self.xcor()
        y = self.ycor()
        if([x,y] in self.cords):

            print("BOOM")

def stopgame():
    wn.loop = False

        
Player_1 = Player()


wn.listen()
wn.onkeypress(Player_1.angle_r, "Right")
wn.onkeypress(Player_1.angle_l, "Left")
wn.onkey(stopgame, "s")

while wn.loop:
    Player_1.check_collision()
    Player_1.move()

    time.sleep(0.08)

wn.mainloop()