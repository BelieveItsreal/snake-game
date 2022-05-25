import time
from snake import Snake
from food import Food
from turtle import Turtle, Screen, forward, screensize
from scoreboard import Scoreboard

screen = Screen()
food = Food()
scoreboard = Scoreboard()

screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()

    #detech collison with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collion with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() <- 290:
        game_is_on = False
        scoreboard.game_over()

    #Detect collion with tail
    #if head collide with any part of segement
    #trigger game over

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)< 10:
            game_is_on = False
            scoreboard.game_over()
















screen.exitonclick()