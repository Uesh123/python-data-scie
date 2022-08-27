from tkinter import mainloop
from turtle import pencolor


from turtle import*
a=1
for i in range(a):
    pencolor('black')
    left(180)
    forward(20)
    circle(25, 160)
    forward(00)
    circle(-25, 160)
    forward(20)
    penup()
    goto(0, 0)
    left(180)
    pendown()
mainloop()