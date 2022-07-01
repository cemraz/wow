import pygame
from pygame.sprite import Sprite


class Squirrel(Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.screen_w = game.setting.screen_w
        self.setting = game.setting

        self.squirrel_speed = self.setting.squirrel_speed#Скорость премещения белки

        self.image = pygame.image.load('Images/squirrel.bmp')#Изображение белки
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
#        self.rect.top = self.screen_rect.top

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    #Рисует белку
    def blitime(self):
        self.screen.blit(self.image,self.rect)

    #Перемещение пришельца вправо
    def update(self):
        self.x += (self.squirrel_speed * self.setting.fleet_direction)
        self.rect.x = self.x


    #Определение,у края ли белка
    #Возвращает True если у края
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
