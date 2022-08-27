from turtle import pos
import pgzrun

HEIGHT = 500
WIDTH = 600

alieng3= Actor(('character_0003'), pos=(200,200))
alieng= Actor(('character_0000'), topleft=(50,50))
alieng1= Actor(('character_0001'), top=(100,100))
alieng2= Actor(('character_0002'), topright=(150,150))
alieng4= Actor(('character_0004'), topleft=(250,250))
alieng5= Actor(('character_0005'), bottomleft=(300,300))
alieng6= Actor(('character_0006'), bottomright=(350,350))
alieng7= Actor(('character_0007'), bottom=(400,400))
alieng8= Actor(('character_0008'), downleft=(450,450))
alieng9= Actor(('character_0009'), downright=(500,500))
alieng10= Actor(('character_0010'), down=(550,550))
def draw():
    screen.fill('white')
    alieng3.draw()
    alieng.draw()
    alieng1.draw()
    alieng2.draw()
    alieng4.draw()
    alieng5.draw()
    alieng6.draw()
    alieng7.draw()
    alieng8.draw()
    alieng9.draw()
    alieng10.draw()

def update():
    alieng3.y += 1
    if alieng3.y>HEIGHT:
        alieng3.y = 0


pgzrun.go()