import turtle
import random
import time



#generate the screen

sc = turtle.Screen()
sc.setup(width = 600, height = 600)
sc.bgcolor("black")
sc.title("Floppy Bird  by Qba")
sc.tracer(0)

#generate a bird

bird = turtle.Turtle()
bird.color("yellow")
bird.penup()
bird.speed(0)
bird.shape('circle')
bird.goto(-240,0)

#gravity
def gravity():
    y = bird.ycor()
    bird.sety(y-10)



#go up bird
def up():
    y = bird.ycor()
    bird.sety(y + 80)

#columns

columns_d = []
columns_u = []

#generate columns
def generate_columns(where=300):
    
        #generate a vector up
        up = random.randint(-180,180)

        

        # generate proporties and object
        column_d = turtle.Turtle()
        column_d.shape("square")
        column_d.shapesize(20,5,0)
        column_d.penup()
        column_d.goto(where ,-300+up)
        column_d.color("green")
        column_d.speed(0)
        # append this colums to array
        columns_d.append(column_d)


        # generate proporties and object
        column_u = turtle.Turtle()
        column_u.shape("square")
        column_u.shapesize(20,5,0)
        column_u.penup()
        column_u.goto(where,300+up)
        column_u.color("green")
        column_u.speed(0)
        # append this colums to array
        columns_u.append(column_u)


# shapesize 30 - 600px



#move columns

def move_columns():

    for var in columns_d :
        x_c_d = var.xcor()
        var.setx(x_c_d-10)

    for var in columns_u :
        x_c_u = var.xcor()
        var.setx(x_c_u-10)
        
    
#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)

pen.write("Score: 0", align="center", font=("Courier",20,"normal"))




sc.listen()
sc.onkey(up,"Up")





delay = 0.08


#check distanse between left side and column
def check_distanse_l():
    for var in columns_d:
        if var.xcor()<-350:
            columns_u.pop(0)
            columns_d.pop(0)

#check distanse between right side and column
def check_distanse_r():
    if columns_d[-1].xcor() == 70:
        generate_columns()
    


#generate the first column
generate_columns(250)


#main score
score = 0

while True:

        sc.update()
        gravity()

        check_distanse_l()

        check_distanse_r()
        move_columns()
        pen.clear()
        pen.write("Score: {}".format(score),align="center",font=("Courier",20,"normal"))


        if(columns_d[0].xcor()==bird.xcor()):
            score = score + 1
        
        if bird.ycor() <= columns_d[0].ycor()+200:
            print(bird.ycor())
            print(columns_d[0].ycor()+600)
     

        time.sleep(delay)


sc.mainloop()
