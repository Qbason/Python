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
        self.write( "Level {} Score: {} To Reach: {}".format(level,score_snake,score_map), align="center", font=("Arial",21,"italic") )

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
    
    pic_food1 = "images\\food.gif"
    pic_food2 = "images\\boost.gif"
    pic_food3 = "images\\slowdown.gif"
    pic_food4 = "images\\double.gif"
    body = "images\\body.gif"
    head_up = "images\\up.gif"
    head_down = "images\\down.gif"
    head_left = "images\\left.gif"
    head_right = "images\\right.gif"

    
    wn.register_shape(pic_food1)
    wn.register_shape(pic_food2)
    wn.register_shape(pic_food3)
    wn.register_shape(pic_food4)
    wn.register_shape(head_up)
    wn.register_shape(head_down)
    wn.register_shape(head_left)
    wn.register_shape(head_right)
    wn.register_shape(body)
    


    #create map
    snake_map = engine.Maps()
    #create snake
    snake = engine.Snake()

    #generate food default
    food1 = engine.Food()
    food1.shape(pic_food1)


    #buff foods
    food2 = engine.Food()
    food2.buff = "fast"
    food2.value = 10
    food2.color("pink")
    food2.shape(pic_food2)
    
    food3 = engine.Food()
    food3.buff = "slow"
    food3.value = 7
    food3.color("yellow")
    food3.shape(pic_food3)

    food4 = engine.Food()
    food4.buff = "double"
    food4.value = 18
    food4.color("orange")
    food4.shape(pic_food4)

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
            food1.teleportation(snake_map.obstacles,snake)
            food2.teleportation(snake_map.obstacles,snake)
            food3.teleportation(snake_map.obstacles,snake)
            food4.teleportation(snake_map.obstacles,snake)
            

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


