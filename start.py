import random
import sys
import pygame
from Setting import Setting
from  Beaver import Beaver
from Bullet import Bulett
from squirrel import Squirrel
from time import sleep
from GetStat import Stat
from GetStat import Background
from Button import ButtonPlay,ButtonEnd

class Game:
    """Класс для управления ресурсами и поведением игры."""
    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        self.setting = Setting()
        self.screen = pygame.display.set_mode((self.setting.screen_w, self.setting.screen_h))#Размер окна

#        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)#FULL SCREEN
#        self.setting.screen_w = self.screen.get_rect().width # Передает значения высоты и ширины в настройки
#        self.setting.screen_h = self.screen.get_rect().height

        pygame.display.set_caption("Дикие бобры")#Назвние окна

        self.stats = Stat(self)#Класс статистики

        self.but = ButtonPlay(self,'Нажмите ПРОБЕЛ для начала игры')
        self.beaver = Beaver(self)#Класс бобра
        self.bullets = pygame.sprite.Group()
        self.squirrels = pygame.sprite.Group()
        self._create_sq()#Создание первого флота белок
        self.bg = Background('Images/Beaver_BG.bmp',(0,0))
        pygame.font.init()
        self.font = pygame.font.SysFont('arial.ttf',32)
        self.text = self.font.render('Game Over',1,(255,0,0))

    # Создание пуль
    def _fire_bullet(self):#Создание пуль
        if len(self.bullets) < self.setting.bullets_allowed: # Ограничение кол-ва снарядов
            new_bullet = Bulett(self)
            self.bullets.add(new_bullet)

    # Действия при нажатии кнопок'''
    def _check_KEYDOWN(self,event): # Действия при нажатии кнопок'''

            if event.key == pygame.K_RIGHT:  # Нажатие кнопки влево
                self.beaver.moving_right = True

            elif event.key == pygame.K_LEFT:  # Нажатие кнопки влево
                self.beaver.moving_left = True

            elif event.key == pygame.K_SPACE and self.stats.game_active == True:
                self._fire_bullet()

            elif event.key == pygame.K_BACKSPACE:
                sys.exit()

            elif event.key== pygame.K_q:
                if self.beaver.x > 500:
                    self.beaver.x -= 500

            elif event.key == pygame.K_e:
                if self.beaver.rect.right < self.screen.get_width()-500:
                    self.beaver.x += 500

            elif event.key == pygame.K_SPACE and self.stats.game_active == False:
                self.start_new_game()

    def start_new_game(self):
        self.stats.reset_stats()
        self.stats.game_active = True
        pygame.mouse.set_visible(False)

    def _check_play_but(self,cord):
        if self.but.rect.collidepoint(cord):
            self.start_new_game()


    # Девствия при отжатии кнопок'''
    def _check_KEYUP(self,event): # Девствия при отжатии кнопок'''

            if event.key == pygame.K_RIGHT:  # Отжатие кнопки влево
                self.beaver.moving_right = False

            elif event.key == pygame.K_LEFT:  # Отжатие кнопки влево
                self.beaver.moving_left = False

    # Создание белки
    def _create_sq_one(self,squirell_num,row_number):
        sq = Squirrel(self) # Присваивание атрибута
        sq_width =sq.rect.width # Получение ширины белки
        sq_height = sq.rect.height # Получение высоты белки
        sq.x = sq_width + 2 * sq_width * squirell_num # Координата к относительно прошлой белки,squirell_num - кол-во по счету белки
        sq.rect.x = sq.x
        sq.rect.y = sq_height + 2 * sq_height * row_number
        self.squirrels.add(sq) # Добавление белки в группу

    # Поиск кол-ва рядов белок котороые влезут в экран
    def number_column_squirrel(self):
        sq = Squirrel(self)
        self.sq_height = sq.rect.height
#        av_space = self.setting.screen_h - sq_height - self.beaver.rect.height
        av_space = self.setting.screen_h - (self.sq_height * 3) - self.beaver.rect.height
        number_row = int(av_space // (2*self.sq_height))
        return number_row

    # Поиск кол-ва белок котороые влезут в ряд
    def number_row_squirrel(self):
        sq = Squirrel(self)
        self.sq_width = sq.rect.width
        av_space = self.setting.screen_w - (2 * self.sq_width)  # Резервация места с краю
        number_squirrel = int(av_space // (2 * self.sq_width))  # Кол-во белок что влезет в ряд на данном экране
        return number_squirrel

    # Создание ряда белок
    def _create_sq(self):#Создание стаи белок

        number_row_squirrel = self.number_row_squirrel() # Поиск кол-ва белок котороые влезут в ряд
        number_column_squirrel = self.number_column_squirrel() # Поиск кол-ва рядов которые влезут в экран

        #Создание белок
        for row_number in range(number_column_squirrel):
            for squirell_num in range(number_row_squirrel):
                self._create_sq_one(squirell_num,row_number)

    # Отслеживание событий клавиатуры и мыши.
    def _check_events(self):
            # Отслеживание событий клавиатуры и мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:#Закрывается при нажатие крестика
                    sys.exit()
                elif event.type == pygame.KEYDOWN:  # Нажатие
                    self._check_KEYDOWN(event)
                elif event.type == pygame.KEYUP:  # Прекращение Действий
                    self._check_KEYUP(event)
                elif event.type == pygame.MOUSEBUTTONDOWN and self.stats.game_active == False:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_but(mouse_pos)
                elif event.type == pygame.MOUSEBUTTONDOWN and self.stats.game_active == True:
                    self._fire_bullet()

    #Обновление экрана
    def _update_screen(self):
        '''Обновление экрана'''
        self.screen.fill(self.setting.bg_color)  # Выводится фон
        self.beaver.blitime()  # Выводится бобер
        for bullet in self.bullets.sprites():#Вывод пуль
            bullet.blitime()
        self.squirrels.draw(self.screen)#Вывод белки
        if self.stats.game_active == False:
            self.but.draw_button()
            but_end = ButtonEnd(self,f'Уничтожено {self.stats.sq_kill} белок')
            but_end.draw_button()


        pygame.display.flip()  # Отображение последнего прорисованного экрана.

    # Проверка попадений
    def check_colisions(self):
        colisions = pygame.sprite.groupcollide(self.bullets, self.squirrels, True,
                                               True)  # первое тру-будет ли снаярд исчезать
        if colisions !={}:
            self.stats.sq_kill +=1

    # Удаление снаярдов за краем экрана
    def remove_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    #Создание нового флота после уничтожения последней белки
    def next_rows(self):
        if not self.squirrels:
            self.bullets.empty()
            self._create_sq()
            if self.stats.sq_kill%10==0:
                self.setting.squirrel_speed += 0.2
                self.stats.level += 1

    #Движение пуль и удаление их за краем экрана,проверка попадания в белок,создание нового флота
    def _update_bullet(self):
        self.bullets.update()

        self.remove_bullets()#  Удаление снаярдов за краем экрана

        self.check_colisions()# Проверка попадений

        self.next_rows()# Создание нового флота после уничтожения последней белки

    #Обработка столкновения ! белок с бобром
    def _ship_hit(self):
        if self.stats.beavers_dead > 0:
            self.stats.beavers_dead -= 1  # Минус одна жизнь
            sleep(1)#Остановка игры на 1 сек

            self.squirrels.empty()#Очищаем белок
            self.bullets.empty()#Очищаем пули

            self.beaver.center()
        else:
            self.stats.game_active = False

    #Проверка добрались ли белки до низа экрана
    def _check_bottom(self):
        screen_rect = self.screen.get_height()
        for sq in self.squirrels.sprites():
            if sq.rect.bottom >= screen_rect:
                self._ship_hit()
                break


    #перемещение белок
    def _update_squirrel(self):
        self._check_fleet_edges()
        self.squirrels.update()

        if pygame.sprite.spritecollideany(self.beaver,self.squirrels):
            self._ship_hit()
        self._check_bottom()
#            if self.setting.beaver_limit == 0:
#                pass

    #Плавный спуск белок по краю
    def down_squirrels(self):
        for sq in self.squirrels.sprites():
            if sq.rect.y == sq.rect.y + 25:
                break
            self.setting.fleet_direction = 0
            sq.rect.y += 1

    #Проверка достигла ли белка края для смены направления
    def _check_fleet_edges(self):
        for sq in self.squirrels.sprites():
            if sq.check_edges() == True:
                self.change_fleet_direction()
#                self.down_squirrels()
                break

    #Смена направления ряда белок
    def change_fleet_direction(self):
        for sq in self.squirrels.sprites():
            sq.rect.y += self.setting.fleet_drop_speed
        self.setting.fleet_direction *= -1

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()#Отслеживание событий
            if self.stats.game_active:
                self.beaver.update()#Перемещение Бобра
                self._update_bullet()#Перемещние пуль
                self._update_squirrel()  # Перемещение белок
 #               if self.stats.game_active == False:
#                    self.screen.blit(self.bg.image,self.bg.rect)
            self._update_screen()#Обновление экрана



if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = Game()
    ai.run_game()
