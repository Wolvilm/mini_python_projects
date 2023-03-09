from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Gameover(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

    #Display the 'GAME OVER' graphic
    def show_game_over(self):
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

