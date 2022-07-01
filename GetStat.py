import pygame

class Stat():
    def __init__(self,game):
        self.setting = game.setting

        self.reset_stats()
        self.game_active = False
        self.sq_kill = 0
        self.level = 1
    def reset_stats(self):
        self.setting.beaver_limit = 1
        self.beavers_dead = self.setting.beaver_limit
        self.level = 1
        self.sq_kill = 0

from pygame.sprite import Sprite
class Background(Sprite):
    def __init__(self,img,loc):
        super().__init__()
        self.image = pygame.image.load(img)
        self.location = loc
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.right = loc

    def draw(self):
#        self.image.fill()
        self.image.blit(self.image,self.rect)




