import turtle
import time
import random


class Snake(turtle.Turtle):

        def __init__(self):
            #snake = turtle.Turtle()
            turtle.Turtle.__init__(self)
            self.color("black")
            self.shape("circle")
            self.penup()
            self.goto(0, 0)
            self.speed(0)
            self.direction = "Up"
            self.howfargo = 20
            self.segments = []
            self.length_seg = 0
            self.not_eaten = True
            self.score = 0

        def move(self):
            if self.direction == "Up":
                y = self.ycor()
                self.sety(y + self.howfargo)

            if self.direction == "Down":
                y = self.ycor()
                self.sety(y - self.howfargo)

            if self.direction == "Left":
                x = self.xcor()
                self.setx(x - self.howfargo)

            if self.direction == "Right":
                x = self.xcor()
                self.setx(x + self.howfargo)

        #sprawdza dlugosc weza
        def check_length(self):
            self.length_seg = len(self.segments)

        ##Sterowanie wężem
        def up(self):
            self.check_length()
            if(self.length_seg==0 or (self.direction!="Down" and self.length_seg>0)):
                self.direction = "Up"

        def down(self):
            self.check_length()
            if (self.length_seg == 0 or (self.direction != "Up" and self.length_seg > 0)):
                self.direction = "Down"

        def right(self):
            self.check_length()
            if (self.length_seg == 0 or (self.direction != "Left" and self.length_seg > 0)):
                self.direction = "Right"

        def left(self):
            self.check_length()
            if (self.length_seg == 0 or (self.direction != "Right" and self.length_seg > 0)):
                self.direction = "Left"

        #Dodawanie kolejnej części ciała
        def add_segment(self):
            segment = Segment()
            self.segments.append(segment)

        #sprawdzanie odległości między jedzeniem (przekazywane przez argument)
        def check_distance_food(self, food,snake_map):

            if self.distance(food) < 20:
                    x = random.randint(-280, 280)
                    y = random.randint(-280, 280)
                    
                    obstacles = snake_map.obstacles 

                    for obstacle in obstacles:
                        x_food=food.xcor()
                        y_food=food.ycor()

                        x_obs=obstacle.xcor()
                        y_obs=obstacle.ycor()

                        x_obs_strech = obstacle.shapesize()[1]
                        y_obs_strech = obstacle.shapesize()[0]


                        if (x_food >=( (-x_obs_strech*10)+x_obs ) and x_food <= ( (x_obs_strech*10) ) + x_obs) and (y_food <=( (y_obs_strech *10)+y_obs ) and y_food >=( -(y_obs_strech*10) ) + y_obs):
                            print ("Te same kordy ! :O ")


                    if (x,y) in (self.xcor(),self.ycor()):
                        print ("Te same kordy ! :O ")
                        

                    food.goto(x, y)
                    self.add_segment()
                    self.score += food.value
                    

                    



        #Przemieszczanie się ciała
        def snake_moving(self):
            if len(self.segments) > 0:
                # rest of segments
                for i in range(len(self.segments) - 1, 0, -1):
                    x = self.segments[i - 1].xcor()
                    y = self.segments[i - 1].ycor()
                    self.segments[i].goto(x, y)

                # 0 segment to head
                x = self.xcor()
                y = self.ycor()
                self.segments[0].goto(x, y)
            #Przemieszczenie głowy
            self.move()

        #Sprawdzanie kolizji z obiektami
        def check_collision_with_obstacle(self,obstacles):

            for obstacle in obstacles:

                x_head=self.xcor()
                y_head=self.ycor()

                x_obs=obstacle.xcor()
                y_obs=obstacle.ycor()

                x_obs_strech = obstacle.shapesize()[1]
                y_obs_strech = obstacle.shapesize()[0]


                if (x_head >=( (-x_obs_strech*10)+x_obs ) and x_head <= ( (x_obs_strech*10) ) + x_obs) and (y_head <=( (y_obs_strech *10)+y_obs ) and y_head >=( -(y_obs_strech*10) ) + y_obs):

                    self.end_game()



        #Sprawdzenie kolizji z samym sobą
        def check_collison_with_self(self):
            for segment in self.segments:
                if self.distance(segment) < 20:
                    self.end_game()
        
        def reset_snake(self):
            self.direction = "stop"
            for segment in self.segments:
                segment.goto(1000, 1000)
            del self.segments[:]


        #Co się dzieje, gdy koniec gry
        def end_game(self):
            self.reset_snake()
            time.sleep(1)
            self.goto(0,0)
            #self.not_eaten = False

        

        #Przechodzenie przez ścianę
        def thruu_the_wall(self):
            if self.xcor() < -300 or self.xcor() > 300:
                x = self.xcor()
                self.setx(-x)

            if self.ycor() < -300 or self.ycor() > 300:
                y = self.ycor()
                self.sety(-y)

#Classa Segmentowa
class Segment(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.color("brown")
            self.shape("circle")
            self.penup()
            self.speed(0)
            self.goto(1000,1000)

#Classa zwykłego jedzenia
class Food(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("red")
        self.shape("circle")
        self.penup()
        self.speed(0)
        self.goto(50, 100)
        self.value = 5

#generowanie przeszkody

class Obstacle(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)

        self.color("black")
        self.shape("square")
        self.penup()

        
class Maps():
    
    def __init__(self):
        self.level = 0
        self.max_level = 10
        self.obstacles = []
        #assuming 1 level -> 5 length
        self.points = 10

    def toreach_points(self):
        
        #adding extra points whiches we have to get
        self.points = self.points + self.level * 10

    def level_up(self):
        self.level += 1
        self.toreach_points()
        self.delete_obstacles()
        self.generate_obstacles()

    

    def generate_obstacles(self):

        level = self.level

        for obs in range(0, level):
            obstacle = Obstacle()
            los = random.randint(0,1)

            if obs % 2 == 0:
                obstacle.shapesize(random.randint(1, 10), 1)

                if(los == 0):
                    obstacle.goto(random.randint(-300, -100), random.randint(-300, 300))
                else:
                    obstacle.goto(random.randint(100, 300), random.randint(-300, 300))

            else:

                obstacle.shapesize(1, random.randint(1, 10))

                if(los == 0):
                    obstacle.goto(  random.randint(-300, 300), random.randint(-300, -100)   )
                else:
                    obstacle.goto(  random.randint(-300, 300), random.randint(100, 300)     )
    
            
            self.obstacles.append(obstacle)
            


    def delete_obstacles(self):
        for obstacle in self.obstacles:
            obstacle.goto(1000,1000)
            del obstacle
    
    
    
    



    
 