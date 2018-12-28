import turtle
import time
import random

body = "images\\body.gif"
head_up = "images\\up.gif"
head_down = "images\\down.gif"
head_left = "images\\left.gif"
head_right = "images\\right.gif"


class Snake(turtle.Turtle):

        def __init__(self):
            #snake = turtle.Turtle()
            turtle.Turtle.__init__(self)
            self.color("black")
            self.shape("circle")
            self.penup()
            self.goto(0, 0)
            self.speed(0)
            self.direction = "stop"
            self.howfargo = 20
            self.segments = []
            self.length_seg = 0
            self.not_eaten = True
            self.score = 0

        def move(self):
            if self.direction == "Up":
                y = self.ycor()
                self.sety(y + self.howfargo)
                #self.shape(head_up)

            if self.direction == "Down":
                y = self.ycor()
                self.sety(y - self.howfargo)
                #self.shape(head_down)

            if self.direction == "Left":
                x = self.xcor()
                self.setx(x - self.howfargo)
                #self.shape(head_left)

            if self.direction == "Right":
                x = self.xcor()
                self.setx(x + self.howfargo)
                #self.shape(head_right)

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
                    #x = random.randint(-280, 280)
                    #y = random.randint(-280, 280)
                        
                    if(food.buff == "fast"):
                        snake_map.fps = 0.08
                        

                    if(food.buff == "slow"):
                        snake_map.fps = 0.2
                        
                    if(food.buff == "double"):
                        self.add_segment()
                        

                    if(food.buff == None):
                        snake_map.fps = 0.15
                        

                    self.add_segment()
                    self.score += food.value

                    food.teleportation(snake_map.obstacles,self)

                    

                    
                    
                    

                    



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

                #kordy naszej głowy(środki!)
                x_head=self.xcor()
                y_head=self.ycor()

                    #cordy naszej przeszkody (środki)
                x_obs=obstacle.xcor()
                y_obs=obstacle.ycor()

                #JAK MOCNO ROZCIĄGA ILE KROTNIE!
                x_obs_strech = obstacle.shapesize()[1]
                y_obs_strech = obstacle.shapesize()[0]
              # DO POPRAWY prawdopodobnie te 20px czyli szerokość segmentu, głowy trzeba tu uwzględnić!!


                if (x_head >=( (-x_obs_strech*10)+x_obs ) and x_head <= ( (x_obs_strech*10) ) + x_obs) and (y_head <=( (y_obs_strech *10)+y_obs ) and y_head >=( -(y_obs_strech*10) ) + y_obs):

                    self.end_game()



        #Sprawdzenie kolizji z samym sobą
        def check_collison_with_self(self):
            for segment in self.segments:
                if self.distance(segment) < 20:
                    self.end_game()
        
        def reset_snake(self):
            self.score = 0
            self.direction = "stop"
            for segment in self.segments:
                segment.goto(1000, 1000)
            del self.segments[:]


        #Co się dzieje, gdy koniec gry
        def end_game(self):
            self.reset_snake()
            #time.sleep(1)
            self.goto(0,0)
            #self.not_eaten = False

        

        #Przechodzenie przez ścianę
        def thruu_the_wall(self):
            if self.xcor() < -290 or self.xcor() > 290:
                x = self.xcor()
                self.setx(-x)

            if self.ycor() < -290 or self.ycor() > 290:
                y = self.ycor()
                self.sety(-y)


#Classa Segmentowa
class Segment(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.color("brown")
            self.shape("images\\body.gif")
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
        self.goto(random.randint(-100,100),random.randint(-100,100))
        self.value = 5
        self.buff = None

    def teleportation(self,obstacles,snake):
        
        cords_x = {i for i in range(-280,280)}
        cords_y = {i for i in range(-280,280)}

        cords_x_s = set()
        cords_y_s = set()

        #dodawaj od wyjątków, gdzie nie może być jabłka(food'a) dopier gdy mamy chociaż dwa segmenty 
        if(len(snake.segments)>1):
            for segment in snake.segments:
                #szerokośc naszego segmentu to 20 z jednej z strony i 20 z drugiej 
                for i in range(-20,20):
                    #dodajemy do seta (tablicy) kordy gdzie są nasze segmenty (x)
                    cords_x_s.add( segment.xcor()+i )
                    #(y)
                    cords_y_s.add( segment.xcor()+i )

        #to samo co na górze tylko z przeszkodami
        for obstacle in obstacles:
            #ilukrotnie rozrzerzona jest przeszkoda
            x_obs_strech = obstacle.shapesize()[1]
            y_obs_strech = obstacle.shapesize()[0]
            #na tej podstawie dodaje do naszych kordów kolejne (x)
            for i in range(-x_obs_strech*10,x_obs_strech*10):
                cords_x_s.add( obstacle.xcor()+i )
            # --,-- (y) coś chyba z tym rozszerzeniem nie tak
            for i in range(-y_obs_strech*10,y_obs_strech*10):
                cords_y_s.add( obstacle.ycor()+i )
        #Pomocnicze
        print(cords_x - cords_x_s)
        #print(cords_y - cords_y_s)
        #do tuple bo choicee nie obsługuje indeksów (setów)
        x = random.choice(tuple(cords_x - cords_x_s))
        # znak minus oznacza, że odejmujemy jak na zbiorach MATMA!
        y = random.choice(tuple(cords_y - cords_y_s))
        self.goto(x,y)
        #coś wywala nam za dużo możliwości czyli w cords_x,y_s jest więcej niż w cords_x,y #
        #należy sprawdzić czemu wywaala nam za dużo cordów
        

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
        self.max_level = 8
        self.obstacles = []
        #assuming 1 level -> 5 length
        self.points = 10
        self.fps = 0.15

    def toreach_points(self):
        
        #adding extra points whiches we have to get
        self.points = self.points + self.level * 10

    def level_up(self):
        self.fps = 0.1
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
    
    
    
    



    
 