"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *

from freegames import vector

import math

def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def draw_circle(start, end):
    """Draw circle from start to end."""
   
    up()
    goto(start.x, start.y) #Puntos de inicio
    down()
    
    #Calcular radio del circulo
    r = math.sqrt(math.pow(end.x - start.x, 2) + math.pow(end.y - start.y, 2))

    begin_fill()
    #Dibujamos el circulo
    circle(r)
    end_fill()


def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    """Se calculan las medidas del rectángulo"""
    width = abs(end.x - start.x)
    height = abs(end.y - start.y)
    
    """Se dibuja el rectángulo"""
    for count in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)

    end:fill()


def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    """Se calculan las medidas del triángulo"""
    width = abs(end.x - start.x)
    height = abs(end.y - start.y)
    
    """Se dibuja el triángulo"""
    for count in range(3):
        forward(width)
        left(120)

    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
#Agregamos el color morado | Se tiene que presionar P en Mayusculas
onkey(lambda: color('purple'), 'P')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', draw_circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
