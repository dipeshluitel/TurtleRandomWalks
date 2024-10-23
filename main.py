import turtle as t
import random as r


walk = t.Turtle()
t.colormode(255)
screen = t.Screen()


def random_color():
    red = r.randint(0, 255)
    g = r.randint(0, 255)
    b = r.randint(0, 255)
    walk.pencolor(red, g, b)


colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"]
angles = [0, 90, 180, 270]
walk.speed("fast")

for _ in range(200):
    walk.pensize(10)
    random_color()
    walk.forward(r.randint(15, 30))
    walk.setheading(r.choice(angles))

screen.exitonclick()
