# -*- coding: utf-8 -*-
"""colabTurtle class assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16PWftTiJUHgWmdsSu4aUoPXU2drDdXxR
"""

!pip install colabturtleplus

from ColabTurtlePlus.Turtle import *
clearscreen()
setup(1000, 1000)
shape("arrow")
pensize(3)
speed(10)
color('black', 'brown')
begin_fill()
forward(150)
right (90)
forward (150)
right (90)
forward(150)
right(90)
forward(150)
end_fill()
color('red', 'green')
begin_fill()
circle(100)
#end_fill
penup()
forward(50)
pendown()
begin_fill()
color('blue', 'pink')
#begin_fill
forward(300)
right(90)
forward(150)
right(90)
forward(300)
right(90)
forward(150)
end_fill()