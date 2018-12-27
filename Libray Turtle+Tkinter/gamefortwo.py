
import engine
import turtle
import time
import random

class gamefortwo(engine.Snake,engine.Food,engine.Obstacle,engine.Segment):
       
    wn = turtle.Screen()
    wn.setup(600, 600)
    wn.title("SNAKE")
    #turtle.colormode(255)
    wn.bgcolor("green")
    #wn.bgpic("obrazek.gif")
    wn.delay(0)
    #wn.tracer(1)
    
    
    obstacles = []
    
    #generate_obstacles(5)
    
    
    snakenumber1 = engine.Snake()
    snakenumber2 = engine.Snake()
    
    # snakenumber2.goto(100,100)
    # snakenumber2.color("pink")
    
    food1 = engine.Food()
    #speed = Speed_buff()
    
    wn.listen()
    wn.onkey(snakenumber1.up, "Up")
    wn.onkey(snakenumber1.down, "Down")
    wn.onkey(snakenumber1.left, "Left")
    wn.onkey(snakenumber1.right, "Right")
    
    wn.onkey(snakenumber2.up, "w")
    wn.onkey(snakenumber2.down, "s")
    wn.onkey(snakenumber2.left, "a")
    wn.onkey(snakenumber2.right, "d")
    
    while snakenumber1.not_eaten and snakenumber2.not_eaten:
    
    
        snakenumber1.check_distance_food(food1)
        #snakenumber1.check_speed_buff(speed)
        snakenumber1.snake_moving()
        snakenumber1.check_collison_with_self()
        snakenumber1.thruu_the_wall()
    
        for obstacle in obstacles:
    
            snakenumber1.check_collision_with_obstacle(obstacle)
    
        # snakenumber2.check_distance_food(food1)
        # snakenumber2.snake_moving()
        # snakenumber2.check_collison_with_self()
        # snakenumber2.thruu_the_wall()
    
        time.sleep(0.14)
    
    wn.mainloop()