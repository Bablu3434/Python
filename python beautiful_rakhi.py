import turtle
import math

# ---------------- SCREEN SETUP ----------------
screen = turtle.Screen()
screen.setup(1200, 700)
screen.bgcolor("#FFF8E7")
screen.title("Beautiful Rakhi using Python")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# ---------------- HELPER FUNCTION ----------------
def circle(x, y, radius, color, outline=None):
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()

    if outline:
        pen.pencolor(outline)
    else:
        pen.pencolor(color)

    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()


# ---------------- RED RAKHI THREAD ----------------
pen.pensize(10)
pen.pencolor("#9B111E")

pen.penup()
pen.goto(-580, 0)
pen.pendown()
pen.goto(580, 0)

# Extra thread lines
for y in [-12, -6, 6, 12]:
    pen.penup()
    pen.goto(-580, y)
    pen.pendown()
    pen.goto(580, y)


# ---------------- GOLDEN BEADS ----------------
for x in [-380, -350, -320, 320, 350, 380]:
    circle(x, 0, 14, "#D4AF37", "#8B6508")
    circle(x - 3, 4, 5, "#FFF1A8")


# ---------------- PEARLS ----------------
for x in [-270, -240, 240, 270]:
    circle(x, 0, 18, "#FDF5E6", "#D8C7A3")
    circle(x - 5, 6, 5, "white")


# ---------------- RED GEM BEADS ----------------
for x in [-205, -165, 165, 205]:
    circle(x, 0, 20, "#B11226", "#7A0010")
    circle(x - 6, 7, 6, "#FF5A5F")


# ---------------- CENTER FLOWER PETALS ----------------
center_x = 0
center_y = 0

for i in range(16):
    angle = i * 22.5
    rad = math.radians(angle)

    x = center_x + 95 * math.cos(rad)
    y = center_y + 95 * math.sin(rad)

    # Petal
    circle(x, y, 28, "#D4AF37", "#8B6508")

    # White stone inside petal
    inner_x = center_x + 100 * math.cos(rad)
    inner_y = center_y + 100 * math.sin(rad)

    circle(inner_x, inner_y, 10, "#FFFDF5", "#D4AF37")


# ---------------- OUTER GOLDEN RING ----------------
circle(0, 0, 105, "#D4AF37", "#8B6508")

# White decorative ring
circle(0, 0, 88, "#FFF8E7", "#D4AF37")

# Ruby stone ring
for i in range(10):
    angle = i * 36
    rad = math.radians(angle)

    x = 65 * math.cos(rad)
    y = 65 * math.sin(rad)

    circle(x, y, 15, "#B11226", "#7A0010")

    # Shine effect
    circle(x - 4, y + 5, 4, "#FF6B6B")


# ---------------- INNER GOLD RING ----------------
circle(0, 0, 48, "#D4AF37", "#8B6508")

# ---------------- WHITE STONES ----------------
for i in range(12):
    angle = i * 30
    rad = math.radians(angle)

    x = 36 * math.cos(rad)
    y = 36 * math.sin(rad)

    circle(x, y, 6, "white", "#C9A227")


# ---------------- CENTER RED RUBY ----------------
circle(0, 0, 25, "#A50021", "#6E0016")

# Ruby shine
circle(-8, 9, 7, "#FF4D6D")

# Small center golden stone
circle(0, 0, 8, "#FFD700")


# ---------------- SIDE DECORATIVE GOLD RINGS ----------------
for x in [-130, 130]:
    circle(x, 0, 26, "#D4AF37", "#8B6508")
    circle(x, 0, 16, "#B11226", "#7A0010")
    circle(x - 4, 5, 5, "#FF5A5F")


# ---------------- TEXT ----------------
pen.penup()
pen.goto(-180, 250)
pen.pendown()
pen.pencolor("#9B111E")

pen.write(
    "Happy Raksha Bandhan",
    align="left",
    font=("Arial", 30, "bold")
)

# ---------------- DECORATIVE DOTS ----------------
for x, y in [
    (-450, 150), (-400, -180),
    (450, 150), (400, -180),
    (-300, 220), (300, 220)
]:
    circle(x, y, 5, "#D4AF37")


turtle.done()