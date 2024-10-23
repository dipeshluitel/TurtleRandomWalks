import turtle as t
import random as r
walk = t.Turtle()
screen = t.Screen()
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"]
angles = [0, 90, 180, 270]

for _ in range(400):
    walk.pensize(15)
    walk.pencolor(r.choice(colors))
    walk.forward(r.randint(15, 30))
    walk.setheading(r.choice(angles))

screen.exitonclick()

