import turtle
from itertools import cycle

colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown'])
def draw_circle(size, lft, rght):
    while size < 695:
        turtle.pencolor(next(colors))
        turtle.circle(size)
        turtle.right(rght + 1)
        turtle.left(lft - 2)
    #turtle.goto(0, -150)
    #turtle.setpos(0, -200)
        draw_circle(size + 5, lft, rght)
        print(size)
    if size == 695:
        turtle.clear()
    """    size = 30
        draw_circle(size)"""
turtle.bgcolor('black')
turtle.goto(0, 0)
turtle.speed(50)
#turtle.pensize(2)
draw_circle(30, 1, 1)