import turtle
kura = turtle.Turtle()

kura.speed(5)
kura.color("red")


def square(x, y):
    kura.forward(x)
    kura.left(y)
    kura.forward(x)
    kura.left(y)
    kura.forward(x)
    kura.left(y)
    kura.forward(x)

for a in range(4):
    square(100,90)
    kura.forward(50)

for b in range(4):
    square(200,90)
    kura.forward(50)

for c in range(2):
    kura.forward(200)
    kura.left(90)

for d in range(3):
    kura.forward(450)
    kura.left(90)

kura.forward(450)

kura.left(135)
kura.forward(637)
kura.right(135)
kura.forward(450)
kura.right(135)
kura.forward(637)
kura.left(180)
kura.forward(320)

for e in range(4):
    kura.circle(87)
    kura.left(90)

