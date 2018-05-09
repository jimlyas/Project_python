import turtle

kura = turtle.Turtle()

kura.speed(25)
for a in range(36):
    kura.circle(100)
    kura.left(10)

kura.color('blue')
for b in range(45):
    kura.forward(100)
    kura.left(90)
    kura.forward(100)
    kura.left(90)
    kura.dot(10, 'green')
    kura.forward(100)
    kura.left(90)
    kura.forward(100)
    kura.left(2)

kura.color('red')
for z in range (36):
    kura.forward(140)
    kura.left(90)
    kura.forward(140)
    kura.left(90)
    kura.dot(10, 'red')
    kura.forward(140)
    kura.left(90)
    kura.forward(140)
    kura.left(100)

win = kura.getscreen()
win.exitonclick()