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


    def show_score(self,snake,snake2,snake_map, points):
        score_snake = snake.score
        score_snake2 = snake2.score


        self.clear()
        self.write( " Get {} points to win".format(points), align="center", font=("Courier",13,"normal") )
        self.goto(0,-260)
        self.write( "Score Snake 1: {} | Score Snake 2: {}".format(score_snake,score_snake2), align="center", font=("Courier",13,"normal") )
        self.goto(0,260)

    def show_win(self,snake):
        name = snake.name
        self.clear()
        self.write( "Snake {} WON!".format(name), align="center", font=("Courier",21,"normal") )





def multiplayer():

 
    def check_snakes(snake1,snake2):


        los = random.randint(0,1)

        for segment in snake2.segments:
            if snake1.distance(segment)<20:
                snake1.end_game()
                #print("Głowa 1 uderzyła w ciało 2")

        if snake1.distance(snake2)<20:
            if(los == 1):
                snake1.end_game()

            else:
                snake2.end_game()
            

        for segment in snake1.segments:
            if snake2.distance(segment)<20:
                snake2.end_game()
                #print("Głowa 1 uderzyła w ciało 2")

        

    
    def check_who_won(snake1,snake2):
        if snake1.score>=value_to_win:
            score.show_win(snake1)
        if snake2.score>=value_to_win:
            score.show_win(snake2)
        

    #Create screen
    wn = turtle.Screen()
    wn.setup(600, 600)
    wn.title("SNAKE MULTIPLAYER")
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


    value_to_win=700


    #create map
    snake_map = engine.Maps()
    snake_map.level=5
    snake_map.generate_obstacles()
    #create snake
    snake = engine.Snake()
    snake.name = "UNO"
    snake.color("blue")
    snake.goto(0,90)
    

    snake2 = engine.Snake()
    snake2.name = "DOS"
    snake2.goto(0,-90)

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
    
  
    
    while snake.not_eaten and snake2.not_eaten:
    
        snake.check_distance_food(food1,snake_map)
        snake2.check_distance_food(food1,snake_map)

        snake.check_distance_food(food2,snake_map)
        snake2.check_distance_food(food2,snake_map)
        
        snake.check_distance_food(food3,snake_map)
        snake2.check_distance_food(food3,snake_map)

        snake.check_distance_food(food4,snake_map)
        snake2.check_distance_food(food4,snake_map)
        
        score.show_score(snake,snake2,snake_map,value_to_win)

        check_who_won(snake,snake2)    


        snake.snake_moving()
        snake2.snake_moving()


        snake.check_collison_with_self()
        snake2.check_collison_with_self()

        snake.thruu_the_wall()
        snake2.thruu_the_wall()

        snake.check_collision_with_obstacle(snake_map.obstacles)
        snake2.check_collision_with_obstacle(snake_map.obstacles)
         
        check_snakes(snake,snake2)
        
        
        time.sleep(snake_map.fps)
    



    wn.mainloop()

