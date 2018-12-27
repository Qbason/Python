
import engine
import turtle
import time
import random

class Maps_Game(engine.Obstacle):
    
    def __init__(self):
        self.level = 0
        self.max_level = 10
        self.obstacles = []
        toreach()

    def toreach():
        #assuming 1 level -> 5 length
        self.points = 5
        #adding extra points whiches we have to get
        self.points = self.points + self.level * 5

    def level_up():
        self.level = +1
        delete_obstacles()
        generate_obstacles()

    def generate_obstacles():

        level = self.level

        for obs in range(0, level):
            obstacle = engine.Obstacle

            
            self.obstacles.append(obstacle)

    #     for i in range(0, howmany):
    #         obstacle = Obstacle()
    #         if i % 2 == 0:
    #             obstacle.shapesize(random.randint(1, 10), 1)
    #         else:
    #             obstacle.shapesize(1, random.randint(1, 10))
    
    #         obstacle.goto(random.randint(-300, 300), random.randint(-300, 300))
    
    #         obstacles.append(obstacle)

    #def delete_obstacle():


class gameforone(engine.Snake,engine.Food,engine.Segment):
       


    wn = turtle.Screen()
    wn.setup(600, 600)
    wn.title("SNAKE SINGLEPLAYER")
    wn.bgcolor("green")
    #wn.bgpic("obrazek.gif")
    wn.delay(0)
    wn.fps = 0.1
    
    
    obstacles = []
    


    snake = engine.Snake()
    #generate food numer 1
    food1 = engine.Food()

    #control player1
    wn.listen()
    wn.onkey(snake.up, "Up")
    wn.onkey(snake.down, "Down")
    wn.onkey(snake.left, "Left")
    wn.onkey(snake.right, "Right")
    
    
    while snake.not_eaten:
    
        snake.check_distance_food(food1)
        snake.snake_moving()
        snake.check_collison_with_self()
        snake.thruu_the_wall()
    
        # for obstacle in obstacles:
    
        #     snake.check_collision_with_obstacle(obstacle)
    


        time.sleep(wn.fps)
    



    wn.mainloop()
