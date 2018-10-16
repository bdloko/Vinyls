import turtle
from itertools import cycle

colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown'])
'''def draw_circle(size):
    turtle.pencolor(next(colors))
    turtle.circle(size)
    #draw_circle(size + 5)
    turtle.speed('fast')
turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
draw_circle(30)'''

def draw_circle1(size, angle, shift):
    while size < 150:
        turtle.pencolor(next(colors))
        turtle.circle(size)
        turtle.right(angle)
        turtle.forward(shift)
        draw_circle1(size + 2, angle + 1, shift + 1)
    if size == 150:
        turtle.clear()
    size = 180
    while size >= 30:
        turtle.pencolor(next(colors))
        turtle.circle(size)
        turtle.right(angle)
        turtle.forward(shift)
        draw_circle1(size - 2, angle, shift - 1)
        #draw_circle1(size + 2, angle + 1, shift + 1)
turtle.bgcolor('black')
turtle.speed(50)
turtle.pensize(4)
draw_circle1(30, 0, 1)