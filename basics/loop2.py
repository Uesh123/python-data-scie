from turtle import*

fillcolor('yellow')

colors= ['red', 'blue', 'black']
pensize(5)
for i in range(3):
    pencolor(colors[i]) #(color[i%3])to rpet the color
    forward(100)
    left(360/3)
    circle(40)

mainloop() # to hold the screen