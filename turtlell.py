import turtle
muju = turtle.Turtle()
# my_start = (0, 0)
muju.penup()
muju.goto(0,0)

muju.pendown()
muju.left(65)
muju.forward(200)
muju.right(135)
muju.forward(200)


def curve():
    muju.right(170)
    muju.forward(80)
    for i in range(90):
        # Defining step by step curve motion
        muju.left(1)
        muju.forward(1)
curve()
# muju.right(155)
# muju.forward(150)
turtle.done()




