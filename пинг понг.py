from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Пинг пельмень')
background = transform.scale(image.load('aoa.png'),   (700, 500))
from random import randint
score = 0

game = True
while game:
    window.blit(background, (0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False

    


    display.update()
clock.tick(FPS)