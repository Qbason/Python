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


    def show_score(self,snake,snake2,snake_map):
        score_snake = snake.score
        score_snake2 = snake2.score

        score_map = snake_map.points

        you_need_snake = score_map - score_snake
        you_need_snake2 = score_map - score_snake2

        level = snake_map.level
        self.clear()
        self.write( "Score Snake 1: {} You need: {}".format(score_snake,you_need_snake), align="center", font=("Courier",13,"normal") )
        self.goto(0,-260)
        self.write( "Score Snake 2: {} You need: {}".format(score_snake2,you_need_snake2), align="center", font=("Courier",13,"normal") )
        self.goto(0,-280)
        self.write( "Level: {} ".format(level), align="center", font=("Courier",13,"normal") )
        self.goto(0,260)

    def show_win(self,snake):
        name = snake.name
        self.clear()
        self.write( "Snake {} WON!".format(name), align="center", font=("Courier",21,"normal") )



def multiplayer():
    
    #Create screen
    wn = turtle.Screen()
    wn.setup(600, 600)
    wn.title("SNAKE MULTIPLAYER")
    wn.bgcolor("green")
    #wn.bgpic("obrazek.gif")
    wn.delay(0)
    
    
    #create map
    snake_map = engine.Maps()
    #create snake
    snake = engine.Snake()
    snake.name = "UNO"

    snake2 = engine.Snake()
    snake.name = "DOS"

    #generate food
    food1 = engine.Food()
    #buff foods
    food2 = engine.Food()
    food2.buff = "fast"
    food2.value = 7
    food2.color("pink")
    
    food3 = engine.Food()
    food3.buff = "slow"
    food3.value = 10
    food3.color("yellow")

    food4 = engine.Food()
    food4.buff = "double"
    food4.value = 20
    food4.color("orange")

    #generate actual scrore
    score = Score()


    #control player_1
    wn.listen()
    wn.onkey(snake.up, "Up")
    wn.onkey(snake.down, "Down")
    wn.onkey(snake.left, "Left")
    wn.onkey(snake.right, "Right")
    #control player_2
    wn.onkey(snake2.up, "w")
    wn.onkey(snake2.down, "s")
    wn.onkey(snake2.left, "a")
    wn.onkey(snake2.right, "d")
    
    def comparing_points(snake):
        if( snake.score >=snake_map.points ):
            snake.goto(0,0)
            snake.direction = "stop"

            snake.reset_snake()

            time.sleep(0.5)

            snake_map.level_up()
            snake.score = 0
            if ( snake_map.level == snake_map.max_level):
                snake.end_game()
                
                score.show_win(snake)
                snake.not_eaten = False

    
    while snake.not_eaten and snake2.not_eaten:
    
        snake.check_distance_food(food1,snake_map)
        snake2.check_distance_food(food1,snake_map)

        snake.check_distance_food(food2,snake_map)
        snake2.check_distance_food(food2,snake_map)
        
        snake.check_distance_food(food3,snake_map)
        snake2.check_distance_food(food3,snake_map)

        snake.check_distance_food(food4,snake_map)
        snake2.check_distance_food(food4,snake_map)

        score.show_score(snake,snake2,snake_map)

        comparing_points(snake)
        comparing_points(snake2)




        snake.snake_moving()
        snake2.snake_moving()


        snake.check_collison_with_self()
        snake2.check_collison_with_self()

        snake.thruu_the_wall()
        snake2.thruu_the_wall()

        snake.check_collision_with_obstacle(snake_map.obstacles)
        snake2.check_collision_with_obstacle(snake_map.obstacles)

        
        
        time.sleep(snake_map.fps)
    



    wn.mainloop()

