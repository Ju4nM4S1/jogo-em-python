import pygame 
from pygame.locals import *
from random import randrange 
from random import uniform

class Meteoro(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.sprites6 = []
                self.sprites6.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\meteoro3.png"))
                self.sprites6.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\meteoro2.png"))
                self.sprites6.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\meteoro1.png"))
                self.sprites6.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\meteoro.png"))
                self.atual = 0
                self.image = self.sprites6[self.atual]
                self.speed_x_meteoro = 1970
                self.speed_y_meteoro = randrange(0,920)
                self.speed = 5

                    
            def update(self):
                self.atual = self.atual + uniform(0.015, 0.030)
                if self.atual >= len(self.sprites6):
                    self.atual = 0


                self.image = self.sprites6[int(self.atual)]

            def process_events(self, events):
                self.speed_x_meteoro -= self.speed
                if self.speed_x_meteoro <= -120:
                    self.speed_x_meteoro = 1970
                    self.speed_y_meteoro = randrange(0,920)
                    self.speed = randrange(2,8)
                
                self.rect = self.image.get_rect()
                self.rect.topleft = self.speed_x_meteoro,self.speed_y_meteoro

            def GetPosition(self):
                return self.speed_x_meteoro