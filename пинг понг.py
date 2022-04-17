from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Пинг пельмень')
background = transform.scale(image.load('aoa.png'),   (700, 500))
from random import randint
score = 0

class Player(GameSprite):
    def update(self): 
        keys = key.get_pressed() 
        if keys[K_LEFT] and self.rect.y > 10:
            self.rect.x -= self.speed

        if keys[K_RIGHT] and self.rect.y < 550:
            self.rect.x += self.speed





game = True
while game:
    window.blit(background, (0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False



    display.update()
clock.tick(FPS)
