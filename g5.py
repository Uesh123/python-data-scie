from random import randint
from turtle import color
import pgzrun

HEIGHT = 500
WIDTH = 500
score=0
speed=3
music.play('op')
player= Actor('character_0000', topleft=(WIDTH//2,HEIGHT//2))
item= Actor('character_0008', pos=(300,500))

def draw():
    screen.fill('black')
    player.draw()
    item.draw()
    screen.draw.text(f'SCORE : {score}', topleft=(10,500-30), color='white') 

def update():
    global score
    if keyboard.right:
        player.x +=speed
    if keyboard.left:
        player.x -=speed
    if keyboard.up:
        player.y -=speed
    if keyboard.down:
        player.y +=speed

    if player.x >WIDTH:
        player.x=0
    if player.x <0:
        player.x=WIDTH
    if player.y >HEIGHT:
        player.y=0
    if player.y <0:
        player.y=HEIGHT
    if player.colliderect(item):
        score +=1
        item.x = randint(0,HEIGHT)
        item.y = randint(0,WIDTH)
        sounds.sound1.play()

pgzrun.go()