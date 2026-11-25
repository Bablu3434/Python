
import turtle as t
import math as m
import random as r
import time

# Screen setup
s = t.Screen()
s.setup(700, 700)
s.bgcolor("black")
s.title("Happy Princess Day")
s.tracer(0)

# Main drawing turtle
p = t.Turtle()
p.hideturtle()
p.penup()
p.speed(0)

# Heart drawing
def draw_heart(x, y, size, color):
    p.penup()
    p.goto(x, y)
    p.color(color)
    p.begin_fill()
    p.pendown()

    for angle in range(0, 360, 2):
        rad = m.radians(angle)
        hx = 16 * m.sin(rad) ** 3
        hy = (
            13 * m.cos(rad)
            - 5 * m.cos(2 * rad)
            - 2 * m.cos(3 * rad)
            - m.cos(4 * rad)
        )

        p.goto(
            x + hx * size / 16,
            y + hy * size / 16
        )

    p.end_fill()
    p.penup()

# Star drawing
def draw_star(x, y, size, color):
    p.goto(x, y)
    p.color(color)
    p.setheading(0)
    p.pendown()
    p.begin_fill()

    for i in range(5):
        p.forward(size)
        p.right(144)

    p.end_fill()
    p.penup()

# Crown drawing
def draw_crown():
    p.goto(-100, 150)
    p.color("gold")
    p.pensize(4)
    p.pendown()

    p.begin_fill()
    p.goto(-90, 210)
    p.goto(-40, 175)
    p.goto(0, 235)
    p.goto(40, 175)
    p.goto(90, 210)
    p.goto(100, 150)
    p.goto(-100, 150)
    p.end_fill()

    p.penup()
    p.pensize(1)

# Flower drawing
def draw_flower(x, y, color):
    for i in range(8):
        p.goto(x, y)
        p.setheading(i * 45)
        p.color(color)
        p.dot(18)

    p.goto(x, y)
    p.color("yellow")
    p.dot(12)

# Background stars
for i in range(70):
    x = r.randint(-330, 330)
    y = r.randint(-320, 320)
    size = r.randint(4, 9)

    draw_star(
        x,
        y,
        size,
        r.choice(["white", "pink", "gold", "violet"])
    )

# Main heart
draw_heart(-140, -90, 13, "#ff1493")

# Crown
draw_crown()

# Flowers
draw_flower(-230, -180, "hotpink")
draw_flower(230, -180, "violet")
draw_flower(-250, 100, "pink")
draw_flower(250, 100, "magenta")

# Princess Day text
p.goto(0, 60)
p.color("white")
p.write("Happy", align="center", font=("Arial", 30, "bold"))

p.goto(0, 10)
p.color("hotpink")
p.write("PRINCESS DAY", align="center", font=("Arial", 32, "bold"))

p.goto(0, -250)
p.color("gold")
p.write("You are Special!", align="center", font=("Arial", 20, "italic"))

# Animation
while True:
    s.update()

    # Heart glow effect
    p.clear()

    draw_heart(
        -140,
        -90,
        r.choice([12, 13, 14]),
        r.choice(["hotpink", "deeppink", "red"])
    )

    time.sleep(0.3)
