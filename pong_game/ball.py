from turtle import Turtle

PADDLE_WIDTH = 2
PADDLE_LEN = 2


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.turtlesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LEN)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y_axis(self):
        self.y_move *= -1

    def bounce_x_axis(self):
        self.x_move *= -1
        self.move_speed *= 0.95

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x_axis()


