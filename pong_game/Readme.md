This is the pong game from the python course "100 days of code" with very little change.

In the Day 22 section, Dr. Angela made a note about a bug where the paddles controlled by the arrow keys do move continuously if the arrow keys are held down causing me to constantly have to tap to move.

I found that if we use


    turtle.onkeypress(my_function, "a")
    turtle.listen()


instead of the usual

    screen = turtle.Screen()
    screen.onkey(my_function, "a")
    screen.listen()


long pressing the arrow keys works.