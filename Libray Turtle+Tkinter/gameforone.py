
import engine
import turtle
import time
import random

class Score(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.hideturtle()
        self.goto(0,260)


    def show_score(self,snake,snake_map):
        score_snake = snake.score
        score_map = snake_map.points
        level = snake_map.level
        self.clear()
        self.write( "Level {} Score: {} To Reach: {}".format(level,score_snake,score_map), align="center", font=("Courier",24,"normal") )




class gameforone(engine.Snake,engine.Food,engine.Segment,engine.Maps):
    
    #Create screen
    wn = turtle.Screen()
    wn.setup(600, 600)
    wn.title("SNAKE SINGLEPLAYER")
    wn.bgcolor("green")
    #wn.bgpic("obrazek.gif")
    wn.delay(0)
    wn.fps = 0.1
    
    #create map
    snake_map = engine.Maps()
    #create snake
    snake = engine.Snake()
    #generate food
    food1 = engine.Food()
    #generate actual scrore
    score = Score()


    #control player
    wn.listen()
    wn.onkey(snake.up, "Up")
    wn.onkey(snake.down, "Down")
    wn.onkey(snake.left, "Left")
    wn.onkey(snake.right, "Right")
    
    
    while snake.not_eaten:
    
        snake.check_distance_food(food1,snake_map)

        if( snake.score >=snake_map.points ):
            snake.goto(0,0)
            snake.direction = "stop"

            snake.reset_snake()

            time.sleep(0.5)

            snake_map.level_up()
            snake.score = 0

            

        snake.snake_moving()
        snake.check_collison_with_self()
        snake.thruu_the_wall()

        snake.check_collision_with_obstacle(snake_map.obstacles)

        score.show_score(snake,snake_map)
       
    


        time.sleep(wn.fps)
    



    wn.mainloop()
