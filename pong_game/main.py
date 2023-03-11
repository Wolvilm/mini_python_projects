import turtle
import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

window = Screen()
window.bgcolor("black")
window.screensize(canvwidth=1000, canvheight=1000)
window.title("Pong")
turtle.tracer(0)

right_paddle = Paddle((490, 0))
left_paddle = Paddle((-490, 0))
ball = Ball()
ball.move_ball()
scoreboard = Scoreboard()


window.listen()
window.onkey(right_paddle.go_up, "Up")
window.onkey(right_paddle.go_down, "Down")
window.onkey(left_paddle.go_up, "w")
window.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    window.update()
    ball.move_ball()

    #Detect collision with upper and lower walls
    if ball.ycor() > 500 or ball.ycor() < -500:
        ball.bounce_y_axis()

    #Detect collision with paddles
    if (ball.distance(right_paddle) < 90 and ball.xcor() > 460) or (ball.distance(left_paddle) < 90 and ball.xcor() < -460):
        ball.bounce_x_axis()


    #Detect right paddle miss
    if ball.xcor() > 497:
        ball.reset_position()
        scoreboard.l_point()

    #Detect left paddle miss
    if ball.xcor() < -497:
        ball.reset_position()
        scoreboard.r_point()





window.exitonclick()
