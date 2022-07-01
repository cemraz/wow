import pygame.font

class ButtonPlay():
    def __init__(self,game,msg):
        pygame.font.init()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        #Назначение свой-ств кнопки
        self.width,self.height = 700,100
        self.button_color = game.setting.bg_color#(255,255,255)
        self.text_color = (0,0,0)
        self.font = pygame.font.SysFont(None,50)

        #Построение RECT и расположение по центру
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        self._give_msg(msg)

    def _give_msg(self,text):
        self.msg_image = self.font.render(text,True,self.text_color,self.button_color)
        self.image_rect = self.msg_image.get_rect()
        self.image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.image_rect)

class ButtonEnd():
    def __init__(self,game,msg):
        pygame.font.init()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        #Назначение свой-ств кнопки
        self.width,self.height = 700,70
        self.button_color = game.setting.bg_color#(255,255,255)
        self.text_color = (0,0,0)
        self.font = pygame.font.SysFont(None,50)

        #Построение RECT и расположение по центру
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.midtop = self.screen_rect.midtop

        self._give_msg(msg)

    def _give_msg(self,text):
        self.msg_image = self.font.render(text,True,self.text_color,self.button_color)
        self.image_rect = self.msg_image.get_rect()
        self.image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.image_rect)

