
class Setting():
    '''Настройки всей игры'''
    def __init__(self):
        #Размеры окна
        self.screen_w = 700
        self.screen_h = 1000

        self.bg_color = (230, 255, 230)#Цвет фона

        self.beaver_limit = 1#Разрешено смертей бобров

        self.squirrel_speed = 1.4
        # Параметры пули
        self.bullet_speed = 5
        self.bullet_w = 3
        self.bullet_h = 15
        self.bullet_color = (15,15,15)
        self.bullets_allowed = 5

        #Параметры белок
        self.fleet_drop_speed = 50
        #Направление движения: self.fleet_direction = 1 -вправо/// = -1 - влево
        self.fleet_direction = 1

