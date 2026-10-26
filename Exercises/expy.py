import turtle
turtle.mode('logo')

def draw_polygon(s, l):
    angle = 360 / s
    for i in range(s):
        turtle.fd(l)
        turtle.rt(angle)

draw_polygon(3, 100)

# Move over to avoid drawing on top of each other
turtle.up()
turtle.rt(90)
turtle.fd(150)
turtle.lt(90)
turtle.down()

# Shape 2: Pentagon
draw_polygon(5, 80)

# 4. Hold the canvas screen open
turtle.done()