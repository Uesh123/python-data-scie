from re import T
from turtle import*
speed (0)
pencolor('red')
bgcolor('yellow')
val = 2
while True:
    forward(3 *val)
    left(360/6)
    circle(100,180)
    val +=1

mainloop()