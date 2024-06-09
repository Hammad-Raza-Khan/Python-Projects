import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
    
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
t.pensize(2)
t.shape('turtle')
t.speed(0)

def making_colours():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g , b)
    return color


def speed(degree):
    angle = int(360 / degree)
    for _ in range(angle):
        t.color(making_colours())
        t.circle(100)
        t.setheading(t.heading() + degree)


speed(5)

s = t.Screen()
t.exitonclick()
