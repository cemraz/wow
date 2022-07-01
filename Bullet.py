import pygame
from pygame.sprite import Sprite

class Bulett(Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen = game.screen
        self.setting = game.setting
        self.color = self.setting.bullet_color

        #Создание снаряда в позиции
#        self.rect = pygame.Rect(0,0,self.setting.bullet_w,self.setting.bullet_h)

        self.img = pygame.image.load('Images/acorn.bmp')

#        self.img = pygame.image.load('Images/есть че.png')#Баксик вместо ореха

        self.rect = self.img.get_rect()
        self.rect.midtop = game.beaver.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.setting.bullet_speed #Устанавливает скорость поднятия по координате y
        self.rect.y = self.y #Перемещает картинку пули

    def draw_bullet(self):
#        pygame.draw.rect(self.screen,self.color,self.rect)
        pass

    def blitime(self):
        self.screen.blit(self.img,self.rect)
