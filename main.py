from turtle import Screen

from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.down, key="Down")

game_is_on = True
count = 0
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collision with wall
    if (snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285 or
            snake.detect_collision_with_tail()):
        game_is_on = False
        scoreboard.game_over()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh_food()
        scoreboard.increment_score()
        snake.add_link()

screen.exitonclick()
