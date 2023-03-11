from turtle import Turtle
PADDLE_WIDTH = 10
PADDLE_LEN = 1

class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LEN)
        self.setpos(coordinates)

    def go_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)

