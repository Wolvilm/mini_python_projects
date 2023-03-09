import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from game_over import Gameover

window = Screen()
window.setup(width=1000, height=1000)
window.bgcolor("black")
window.title("Snake Game")
window.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
game_over = Gameover()

window.listen()
window.onkey(snake.up, "Up")
window.onkey(snake.down, "Down")
window.onkey(snake.left, "Left")
window.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    window.update()
    time.sleep((0.1))
    snake.move()

    #Detect collision with food and respawn food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect colision with wall
    if snake.head.heading() == 0 and snake.head.xcor() > 495:
        game_is_on = False
        game_over.show_game_over()
    if snake.head.heading() == 180 and snake.head.xcor() < -495:
        game_is_on = False
        game_over.show_game_over()
    if snake.head.heading() == 90 and snake.head.ycor() > 495:
        game_is_on = False
        game_over.show_game_over()
    if snake.head.heading() == 270 and snake.head.ycor() < -495:
        game_is_on = False
        game_over.show_game_over()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            game_is_on = False
            game_over.show_game_over()




















window.exitonclick()

