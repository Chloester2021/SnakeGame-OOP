from turtle import *
import time
from snake import *
from food import *
from scoreboard import *

screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True 

while game_on: 
    screen.update()
    time.sleep(0.2)
    snake.move_snake()
    x = snake.head.xcor()
    y = snake.head.ycor()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase()
    
    if abs(x) > 280 or abs(y) > 280:
        scoreboard.resetscore()
        snake.reset_snake()


    for s in snake.all_snakes[1:]:
        if snake.head.distance(s) < 15:
            scoreboard.resetscore()
            snake.reset_snake()   


screen.exitonclick()