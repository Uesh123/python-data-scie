from turtle import *

speed('fastest')
sides= int(input('how many side?'))
distance= int(input('how far do you want go?'))
fillcolor('blue')
begin_fill()
for i in range(sides):
    forward(distance)
    left(360/sides) 
end_fill()

mainloop()