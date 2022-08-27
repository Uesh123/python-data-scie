from turtle import*
speed ('fastest')
bgcolor('black')
pencolor('red')
val = 1
for i in range(5):
    for i in range(5):
        forward(350)
        left(360/5)
        circle(40)
        for i in range(5):
            forward(val*50)
            left(360/5)
            circle(100,180)
            val +=1
mainloop()
