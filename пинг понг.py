from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Пинг пельмень')
background = transform.scale(image.load('aoa.png'),   (700, 500))
from random import randint
score = 0

class GameSprite(sprite.Sprite):
   #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
       # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = "right"

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

font.init()
font2 = font.SysFont("impact", 36)




class Player(GameSprite):
    def update(self): 
        keys = key.get_pressed() 
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < 40:
            self.rect.y += self.speed


def update_r(self):
    keys = key.get_pressed
    if keys[K_w] and slf.rect.y > 5:
        self.rect.y -= self.speed
    if keys[K_s] and slf.rect.y < 400:
        self.rect.y += self.speed



left_r = Player("lol.png",10, 10, 90, 100, 5)
right_r = Player("lol2.png", 600, 10, 90, 100, 5)
boll = GameSprite("gug.png", 200, 200, 100, 60, 2)




game = True
while game:
    window.blit(background, (0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False

        left_r.reset()
        left_r.update()
        right_r.reset()
        right_r.update()
        boll.reset()
        boll.update()



        display.update()
clock.tick(FPS)
