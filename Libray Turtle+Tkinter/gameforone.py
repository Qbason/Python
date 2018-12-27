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
        self.write( "Level {} Score: {} To Reach: {}".format(level,score_snake,score_map), align="center", font=("Courier",21,"normal") )

    def show_win(self):
        self.clear()
        self.write( "YOU WON!", align="center", font=("Courier",21,"normal") )



def singleplayer():
    
    #Create screen
    wn = turtle.Screen()
    wn.setup(600, 600)
    wn.title("SNAKE SINGLEPLAYER")
    wn.bgcolor("green")
    #wn.bgpic("obrazek.gif")
    wn.delay(0)
    
    
    #create map
    snake_map = engine.Maps()
    #create snake
    snake = engine.Snake()
    #generate food
    food1 = engine.Food()
    #buff foods
    food2 = engine.Food()
    food2.buff = "fast"
    food2.value = 20
    food2.color("pink")
    
    food3 = engine.Food()
    food3.buff = "slow"
    food3.value = 20
    food3.color("yellow")

    food4 = engine.Food()
    food4.buff = "double"
    food4.value = 20
    food4.color("orange")

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
        snake.check_distance_food(food2,snake_map)
        snake.check_distance_food(food3,snake_map)
        snake.check_distance_food(food4,snake_map)
        score.show_score(snake,snake_map)

        if( snake.score >=snake_map.points ):
            snake.goto(0,0)
            snake.direction = "stop"

            snake.reset_snake()

            time.sleep(0.5)

            snake_map.level_up()
            snake.score = 0
            #print("Level:",snake_map.level)
            #print("Level_max:",snake_map.max_level)
            if ( snake_map.level == snake_map.max_level):
                snake.end_game()
                
                score.show_win()
                snake.not_eaten = False


        snake.snake_moving()
        snake.check_collison_with_self()
        snake.thruu_the_wall()

        snake.check_collision_with_obstacle(snake_map.obstacles)

        
        
        time.sleep(snake_map.fps)
    



    wn.mainloop()

