<<<<<<< HEAD
import turtle
import math

# ---------- Screen setup ----------
screen = turtle.Screen()
screen.setup(width=900, height=850)
screen.title("Shri Krishna | Python Turtle Art")
screen.bgcolor("#fff8e7")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)


# ---------- Drawing functions ----------
def move(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()


def line(points, color, width=3):
    pen.color(color)
    pen.pensize(width)

    move(*points[0])

    for point in points[1:]:
        pen.goto(*point)


def polygon(points, fill, outline=None):
    pen.pensize(2)
    pen.color(outline or fill, fill)

    move(*points[0])
    pen.begin_fill()

    for point in points[1:]:
        pen.goto(*point)

    pen.goto(*points[0])
    pen.end_fill()


def ellipse(x, y, rx, ry, fill, outline=None):
    """Draw an ellipse centered at (x, y)."""
    points = []

    for angle in range(0, 361, 3):
        radians = math.radians(angle)
        points.append((
            x + rx * math.cos(radians),
            y + ry * math.sin(radians)
        ))

    polygon(points, fill, outline)


def curve(start, control, end, color, width=3):
    """Draw a quadratic Bezier curve."""
    points = []

    for step in range(61):
        t = step / 60

        x = (
            (1 - t) ** 2 * start[0]
            + 2 * (1 - t) * t * control[0]
            + t ** 2 * end[0]
        )

        y = (
            (1 - t) ** 2 * start[1]
            + 2 * (1 - t) * t * control[1]
            + t ** 2 * end[1]
        )

        points.append((x, y))

    line(points, color, width)


def text(x, y, message, size, color):
    move(x, y)
    pen.color(color)
    pen.write(
        message,
        align="center",
        font=("Arial", size, "bold")
    )


# ---------- Colours ----------
blue = "#65bce8"
dark_blue = "#243e69"
gold = "#edb936"
light_gold = "#ffe592"
hair = "#19243b"
red = "#c74749"


# ---------- Halo ----------
ellipse(0, 65, 245, 270, "#fff0bd")
ellipse(0, 65, 223, 248, "#ffe5a0")
ellipse(0, 65, 203, 228, "#fff4d4")

# Decorative dots around the halo
for angle in range(0, 360, 15):
    radians = math.radians(angle)

    x = 234 * math.cos(radians)
    y = 65 + 259 * math.sin(radians)

    ellipse(x, y, 3, 3, gold)


# ---------- Shoulders and clothing ----------
ellipse(0, -226, 172, 92, blue, dark_blue)

polygon(
    [
        (-174, -213),
        (-104, -178),
        (-45, -257),
        (72, -192),
        (173, -225),
        (155, -315),
        (-155, -315)
    ],
    "#f6c344",
    gold
)

curve(
    (-143, -240),
    (-30, -330),
    (139, -235),
    "#d38b25",
    5
)

# Neck
polygon(
    [(-49, -105), (49, -105), (49, -201), (0, -231), (-49, -201)],
    blue,
    dark_blue
)


# ---------- Hair behind the face ----------
ellipse(0, 37, 137, 173, hair)
ellipse(-108, -29, 33, 92, hair)
ellipse(108, -29, 33, 92, hair)


# ---------- Ears ----------
ellipse(-112, 1, 25, 42, blue, dark_blue)
ellipse(112, 1, 25, 42, blue, dark_blue)

curve((-120, 17), (-98, 29), (-111, -17), dark_blue, 3)
curve((120, 17), (98, 29), (111, -17), dark_blue, 3)


# ---------- Face ----------
ellipse(0, 24, 108, 143, blue, dark_blue)

# Soft cheek highlights
ellipse(-66, -24, 22, 11, "#83ccef")
ellipse(66, -24, 22, 11, "#83ccef")


# ---------- Hairline ----------
curve((-103, 90), (-62, 149), (0, 128), hair, 17)
curve((0, 128), (57, 156), (103, 90), hair, 17)


# ---------- Eyebrows ----------
curve((-77, 61), (-48, 79), (-20, 59), hair, 5)
curve((20, 59), (48, 79), (77, 61), hair, 5)


# ---------- Peaceful eyes ----------
curve((-78, 38), (-49, 13), (-20, 37), dark_blue, 4)
curve((20, 37), (49, 13), (78, 38), dark_blue, 4)

# Eyelashes
line([(-78, 38), (-85, 44)], dark_blue, 3)
line([(78, 38), (85, 44)], dark_blue, 3)


# ---------- Nose ----------
curve((3, 29), (-8, -3), (7, -10), "#3285b7", 3)
curve((-8, -13), (2, -21), (14, -12), dark_blue, 2)


# ---------- Smile ----------
curve((-31, -47), (0, -67), (32, -45), red, 4)
curve((-19, -57), (0, -69), (20, -56), "#459aca", 2)


# ---------- Vaishnava tilak ----------
curve((-17, 103), (-17, 61), (0, 54), "#fffbea", 5)
curve((17, 103), (17, 61), (0, 54), "#fffbea", 5)
line([(0, 100), (0, 72)], "#d7553c", 4)


# ---------- Earrings ----------
for x in (-119, 119):
    ellipse(x, -40, 9, 10, gold)
    ellipse(x, -63, 17, 21, gold, "#bd8522")
    ellipse(x, -63, 10, 14, "#fff8e7")
    ellipse(x, -86, 7, 10, "#d75c64")


# ---------- Crown ----------
polygon(
    [
        (-112, 117),
        (-120, 192),
        (- seventy if False else -70, 171),
        (-48, 226),
        (0, 190),
        (48, 226),
        (70, 171),
        (120, 192),
        (112, 117)
    ],
    gold,
    "#b57d22"
)

# Crown band
polygon(
    [(-111, 117), (-113, 148), (113, 148), (111, 117)],
    light_gold,
    "#b57d22"
)

# Crown jewels
for x in (-84, -42, 0, 42, 84):
    ellipse(x, 132, 7, 8, "#cf565a", "#b57d22")

ellipse(0, 175, 19, 23, "#fff1b0", "#b57d22")
ellipse(0, 175, 11, 15, "#209a8d")

line([(-96, 158), (-76, 170)], light_gold, 4)
line([(96, 158), (76, 170)], light_gold, 4)


# ---------- Peacock feather ----------
curve((43, 197), (83, 273), (108, 329), "#437c48", 5)

ellipse(106, 292, 39, 62, "#45975f", "#2b7450")

for offset in range(-24, 25, 8):
    curve(
        (103, 247),
        (106 + offset * 2, 283),
        (106 + offset, 330),
        "#8bc775",
        1
    )

ellipse(106, 294, 26, 38, "#b7cd61")
ellipse(106, 297, 19, 28, "#31aaa1")
ellipse(106, 299, 12, 19, "#265d94")
ellipse(106, 301, 6, 11, "#192b55")
ellipse(110, 308, 3, 5, "#ecffff")


# ---------- Necklace ----------
curve((-57, -173), (0, -249), (57, -173), gold, 5)

for angle in range(205, 336, 13):
    radians = math.radians(angle)

    x = 67 * math.cos(radians)
    y = -165 + 56 * math.sin(radians)

    ellipse(x, y, 5, 6, "#fff1b0", gold)

ellipse(0, -233, 13, 17, gold)
ellipse(0, -233, 7, 10, "#d45a61")


# ---------- Flute ----------
polygon(
    [(-180, -267), (173, -219), (176, -237), (-177, -285)],
    "#bd762c",
    "#805021"
)

line([(-176, -270), (172, -222)], "#f7d887", 3)

for x in (-131, -79, -27, 25, 77, 129):
    y = -276 + (x + 180) * 48 / 353
    ellipse(x, y, 4, 4, "#51371f")

# Gold bands on the flute
for x in (-162, 151):
    y = -267 + (x + 180) * 48 / 353
    line([(x, y), (x + 3, y - 18)], light_gold, 6)

# Hanging ornament
line([(150, -241), (158, -280), (151, -297)], gold, 3)
ellipse(151, -304, 7, 12, "#d55763")


# ---------- Footer ----------
text(0, -363, "SHRI KRISHNA", 25, "#856026")
text(0, -393, "Peace • Love • Devotion", 13, "#937946")

screen.update()
=======
import turtle
import math

# ---------- Screen setup ----------
screen = turtle.Screen()
screen.setup(width=900, height=850)
screen.title("Shri Krishna | Python Turtle Art")
screen.bgcolor("#fff8e7")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)


# ---------- Drawing functions ----------
def move(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()


def line(points, color, width=3):
    pen.color(color)
    pen.pensize(width)

    move(*points[0])

    for point in points[1:]:
        pen.goto(*point)


def polygon(points, fill, outline=None):
    pen.pensize(2)
    pen.color(outline or fill, fill)

    move(*points[0])
    pen.begin_fill()

    for point in points[1:]:
        pen.goto(*point)

    pen.goto(*points[0])
    pen.end_fill()


def ellipse(x, y, rx, ry, fill, outline=None):
    """Draw an ellipse centered at (x, y)."""
    points = []

    for angle in range(0, 361, 3):
        radians = math.radians(angle)
        points.append((
            x + rx * math.cos(radians),
            y + ry * math.sin(radians)
        ))

    polygon(points, fill, outline)


def curve(start, control, end, color, width=3):
    """Draw a quadratic Bezier curve."""
    points = []

    for step in range(61):
        t = step / 60

        x = (
            (1 - t) ** 2 * start[0]
            + 2 * (1 - t) * t * control[0]
            + t ** 2 * end[0]
        )

        y = (
            (1 - t) ** 2 * start[1]
            + 2 * (1 - t) * t * control[1]
            + t ** 2 * end[1]
        )

        points.append((x, y))

    line(points, color, width)


def text(x, y, message, size, color):
    move(x, y)
    pen.color(color)
    pen.write(
        message,
        align="center",
        font=("Arial", size, "bold")
    )


# ---------- Colours ----------
blue = "#65bce8"
dark_blue = "#243e69"
gold = "#edb936"
light_gold = "#ffe592"
hair = "#19243b"
red = "#c74749"


# ---------- Halo ----------
ellipse(0, 65, 245, 270, "#fff0bd")
ellipse(0, 65, 223, 248, "#ffe5a0")
ellipse(0, 65, 203, 228, "#fff4d4")

# Decorative dots around the halo
for angle in range(0, 360, 15):
    radians = math.radians(angle)

    x = 234 * math.cos(radians)
    y = 65 + 259 * math.sin(radians)

    ellipse(x, y, 3, 3, gold)


# ---------- Shoulders and clothing ----------
ellipse(0, -226, 172, 92, blue, dark_blue)

polygon(
    [
        (-174, -213),
        (-104, -178),
        (-45, -257),
        (72, -192),
        (173, -225),
        (155, -315),
        (-155, -315)
    ],
    "#f6c344",
    gold
)

curve(
    (-143, -240),
    (-30, -330),
    (139, -235),
    "#d38b25",
    5
)

# Neck
polygon(
    [(-49, -105), (49, -105), (49, -201), (0, -231), (-49, -201)],
    blue,
    dark_blue
)


# ---------- Hair behind the face ----------
ellipse(0, 37, 137, 173, hair)
ellipse(-108, -29, 33, 92, hair)
ellipse(108, -29, 33, 92, hair)


# ---------- Ears ----------
ellipse(-112, 1, 25, 42, blue, dark_blue)
ellipse(112, 1, 25, 42, blue, dark_blue)

curve((-120, 17), (-98, 29), (-111, -17), dark_blue, 3)
curve((120, 17), (98, 29), (111, -17), dark_blue, 3)


# ---------- Face ----------
ellipse(0, 24, 108, 143, blue, dark_blue)

# Soft cheek highlights
ellipse(-66, -24, 22, 11, "#83ccef")
ellipse(66, -24, 22, 11, "#83ccef")


# ---------- Hairline ----------
curve((-103, 90), (-62, 149), (0, 128), hair, 17)
curve((0, 128), (57, 156), (103, 90), hair, 17)


# ---------- Eyebrows ----------
curve((-77, 61), (-48, 79), (-20, 59), hair, 5)
curve((20, 59), (48, 79), (77, 61), hair, 5)


# ---------- Peaceful eyes ----------
curve((-78, 38), (-49, 13), (-20, 37), dark_blue, 4)
curve((20, 37), (49, 13), (78, 38), dark_blue, 4)

# Eyelashes
line([(-78, 38), (-85, 44)], dark_blue, 3)
line([(78, 38), (85, 44)], dark_blue, 3)


# ---------- Nose ----------
curve((3, 29), (-8, -3), (7, -10), "#3285b7", 3)
curve((-8, -13), (2, -21), (14, -12), dark_blue, 2)


# ---------- Smile ----------
curve((-31, -47), (0, -67), (32, -45), red, 4)
curve((-19, -57), (0, -69), (20, -56), "#459aca", 2)


# ---------- Vaishnava tilak ----------
curve((-17, 103), (-17, 61), (0, 54), "#fffbea", 5)
curve((17, 103), (17, 61), (0, 54), "#fffbea", 5)
line([(0, 100), (0, 72)], "#d7553c", 4)


# ---------- Earrings ----------
for x in (-119, 119):
    ellipse(x, -40, 9, 10, gold)
    ellipse(x, -63, 17, 21, gold, "#bd8522")
    ellipse(x, -63, 10, 14, "#fff8e7")
    ellipse(x, -86, 7, 10, "#d75c64")


# ---------- Crown ----------
polygon(
    [
        (-112, 117),
        (-120, 192),
        (- seventy if False else -70, 171),
        (-48, 226),
        (0, 190),
        (48, 226),
        (70, 171),
        (120, 192),
        (112, 117)
    ],
    gold,
    "#b57d22"
)

# Crown band
polygon(
    [(-111, 117), (-113, 148), (113, 148), (111, 117)],
    light_gold,
    "#b57d22"
)

# Crown jewels
for x in (-84, -42, 0, 42, 84):
    ellipse(x, 132, 7, 8, "#cf565a", "#b57d22")

ellipse(0, 175, 19, 23, "#fff1b0", "#b57d22")
ellipse(0, 175, 11, 15, "#209a8d")

line([(-96, 158), (-76, 170)], light_gold, 4)
line([(96, 158), (76, 170)], light_gold, 4)


# ---------- Peacock feather ----------
curve((43, 197), (83, 273), (108, 329), "#437c48", 5)

ellipse(106, 292, 39, 62, "#45975f", "#2b7450")

for offset in range(-24, 25, 8):
    curve(
        (103, 247),
        (106 + offset * 2, 283),
        (106 + offset, 330),
        "#8bc775",
        1
    )

ellipse(106, 294, 26, 38, "#b7cd61")
ellipse(106, 297, 19, 28, "#31aaa1")
ellipse(106, 299, 12, 19, "#265d94")
ellipse(106, 301, 6, 11, "#192b55")
ellipse(110, 308, 3, 5, "#ecffff")


# ---------- Necklace ----------
curve((-57, -173), (0, -249), (57, -173), gold, 5)

for angle in range(205, 336, 13):
    radians = math.radians(angle)

    x = 67 * math.cos(radians)
    y = -165 + 56 * math.sin(radians)

    ellipse(x, y, 5, 6, "#fff1b0", gold)

ellipse(0, -233, 13, 17, gold)
ellipse(0, -233, 7, 10, "#d45a61")


# ---------- Flute ----------
polygon(
    [(-180, -267), (173, -219), (176, -237), (-177, -285)],
    "#bd762c",
    "#805021"
)

line([(-176, -270), (172, -222)], "#f7d887", 3)

for x in (-131, -79, -27, 25, 77, 129):
    y = -276 + (x + 180) * 48 / 353
    ellipse(x, y, 4, 4, "#51371f")

# Gold bands on the flute
for x in (-162, 151):
    y = -267 + (x + 180) * 48 / 353
    line([(x, y), (x + 3, y - 18)], light_gold, 6)

# Hanging ornament
line([(150, -241), (158, -280), (151, -297)], gold, 3)
ellipse(151, -304, 7, 12, "#d55763")


# ---------- Footer ----------
text(0, -363, "SHRI KRISHNA", 25, "#856026")
text(0, -393, "Peace • Love • Devotion", 13, "#937946")

screen.update()
>>>>>>> origin/main
screen.exitonclick()