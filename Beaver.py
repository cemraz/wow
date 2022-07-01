import pygame


class Beaver():
    def __init__(self,game):
        '''Загружает бобра в начальную позицию'''
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.moving_right = False #Флаг перемещения вправо
        self.moving_left = False #Флаг перемещения влево

        self.beaver_speed = 10 # Скорость бобра

        #Загружаем фото бобра
        self.image = pygame.image.load('images/Beaver_run.bmp')
#        self.image = pygame.image.load('Images/есть че.png')#Баксик вместо ореха
#        self.image = pygame.image.load('images/acorn.bmp')
        self.rect = self.image.get_rect()


        #Стартовая позиция бобра
        self.center()


    def blitime(self):
        '''Рисует корабль в текущей позиции'''
        self.screen.blit(self.image,self.rect)

    def update(self):
        '''Перемещение и не выхождение за край бобра'''
        if self.moving_right and self.rect.right < self.screen_rect.right + 100: # self.rect.right возвращает координату х правого края бобра
            self.x += self.beaver_speed
        if self.moving_left and self.rect.left > -100:
            self.x -= self.beaver_speed

        self.rect.x = self.x

    #Перемещние бобра в центр экрана
    def center(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

