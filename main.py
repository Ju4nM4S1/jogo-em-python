import os, sys

dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)



import pygame 
from pygame.locals import *
from random import randrange 
from random import uniform
import time 
 

pygame.init()
yellow = (255, 255 ,0)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
whit = (255, 255, 255)
orange = (255, 140, 0)
pink = (255, 15 , 192)
cian = (0, 255, 255) 
X = 1920
Y = 950

font = pygame.font.SysFont("arial", 48, True, False)
scrn = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Sprites')

pygame.display.set_caption('image')
cenario1 = pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\estrelas 1.png")
cenario2 = pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\estrelas 2.png")
cenario3 = pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\estrelas 3.png")
cenario4 = pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\estrelas 4.png")
cenario5 = pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\estrelas 5.png")
cenario100 = pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\terra1.png")
cenario101 = pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\terra2.png")
cenario102 = pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\terra3.png")
cenario103 = pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\terra4.png")
cenario104 = pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\lua.png")
inicio = pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\inicio.png")
morte = pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\morte.png")
venceu = pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\venceu.png")
et = pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\et.png")
class Scnery():
    def __init__(self, size):
        self.size = size
        self.matrix = [[1,2,3,4,2,3,2,1,3,2],
                       [1,2,1,4,3,4,3,3,104,2],
                       [4,100,101,2,4,1,3,2,5,2],
                       [1,103,102,2,1,1,4,3,2,3],
                       [4,1,4,2,1,3,1,2,1,3],
                       ]
        
    def paint_row(self, screen ,row_number, row):
        for column_number,column in enumerate(row):
            x = column_number * self.size
            y = row_number * self.size
            cenario = cenario1
            if column == 2:
                cenario = cenario2
            elif column == 3:
                cenario = cenario3
            elif column == 4:
                cenario = cenario4
            
            elif column == 5:
                cenario = cenario5

            elif column == 100:
                cenario = cenario100

            elif column == 101:
                cenario = cenario101

            elif column == 102:
                cenario = cenario102

            elif column == 103:
                cenario = cenario103
            elif column == 104:
                cenario = cenario104
            screen.blit(cenario, (x , y))
                

            


    def paint(self, screen):
        for row_number, row in enumerate(self.matrix):
            self.paint_row(screen ,row_number, row)



class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_nave\\nave1.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_nave\\nave2.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_nave\\nave3.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_nave\\nave4.png"))
        self.sprites1 = []
        self.sprites1.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_nave1\\nave1.png"))
        self.sprites1.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_nave1\\nave2.png"))
        self.sprites1.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_nave1\\nave3.png"))
        self.sprites1.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_nave1\\nave4.png"))
        self.sprites2 = []
        self.sprites2.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_nave2\\nave1.png"))
        self.sprites2.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_nave2\\nave2.png"))
        self.sprites2.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_nave2\\nave3.png"))
        self.sprites2.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_nave2\\nave4.png"))
        self.sprites3 = []
        self.sprites3.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_nave3\\nave1.png"))
        self.sprites3.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_nave3\\nave2.png"))
        self.sprites3.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_nave3\\nave3.png"))
        self.sprites3.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_nave3\\nave4.png"))
        self.atual = 0
        self.speed_x_nave = 0.0
        self.speed_y_nave = 0.0
        self.image = self.sprites[self.atual]
        self.image = self.sprites1[self.atual]
        self.image = self.sprites2[self.atual]
        self.image = self.sprites3[self.atual]
        self.nave_status = 1
        self.speed_d_nave = 1
        self.speed_a_nave = 1
        self.speed_w_nave = 1
        self.speed_s_nave = 1
        self.hubble_status = 1
        self.speed = 0.0
        self.status = 1


    def update(self):
        self.atual = self.atual + 0.1
        if self.atual >= len(self.sprites):
            self.atual = 1
        if self.nave_status == 2:
            self.image = self.sprites[int(self.atual)]
        elif self.nave_status == 3:
            self.image = self.sprites1[int(self.atual)]
        elif self.nave_status == 1:
            self.image = self.sprites2[int(self.atual)]
        elif self.nave_status == 4:
            self.image = self.sprites3[int(self.atual)]
        
    def process_events(self, events):
        for e in events:
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_d:
                        self.speed_d_nave = 2
                        self.nave_status = 1
                    elif e.key == pygame.K_a:
                        self.speed_a_nave = 2
                        self.nave_status = 2
                    elif e.key == pygame.K_w:
                        self.speed_w_nave = 2
                        self.nave_status = 3
                    elif e.key == pygame.K_s:
                        self.speed_s_nave = 2
                        self.nave_status = 4
           

                elif e.type == pygame.KEYUP:
                    if e.key == pygame.K_d:
                            self.speed = 0.0
                            self.speed_d_nave = 1
                    elif e.key == pygame.K_a:
                            self.speed_a_nave = 1
                    elif e.key == pygame.K_w:
                            self.speed = 0.0
                            self.speed_w_nave = 1
                    elif e.key == pygame.K_s:
                            self.speed = 0.0
                            self.speed_s_nave = 1

        



        if self.speed_d_nave == 2 and self.speed_x_nave < 1735:
            if self.speed <= 5:
                self.speed += 0.1
            self.speed_x_nave += self.speed
 

        elif self.speed_d_nave == 1: 
            self.speed_x_nave += 0 

        if self.speed_a_nave == 2 and self.speed_x_nave > 0:
            if self.speed <= 5:
                self.speed += 0.1
            self.speed_x_nave -= self.speed
          

        elif self.speed_a_nave == 1: 
            self.speed_x_nave += 0

        if self.speed_w_nave == 2 and self.speed_y_nave > 0:
            if self.speed <= 5:
                self.speed += 0.1
            self.speed_y_nave -= self.speed
       

        elif self.speed_w_nave == 1: 
            self.speed_y_nave += 0

        if self.speed_s_nave == 2 and self.speed_y_nave < 770:
            if self.speed <= 5:
                self.speed += 0.1
            self.speed_y_nave += self.speed
  

        elif self.speed_s_nave == 1: 
            self.speed_y_nave += 0

        
        for i in events:
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_e and self.speed_x_nave >= 1496 and self.speed_x_nave <= 1758 and self.speed_y_nave >= 344 and self.speed_y_nave <= 606 :
                    if self.hubble_status == 1:
                        self.hubble_status = 2

                

                    elif self.hubble_status == 2:
                        self.hubble_status = 2

                if i.key == pygame.K_e and self.speed_x_nave >= 142 and self.speed_x_nave <= 626 and self.speed_y_nave >= 334 and self.speed_y_nave <= 818 and self.hubble_status == 2:
                    self.status = 2

        if self.hubble_status == 2:
            hubbles.draw(scrn)
        else: 
            pass
        
        if self.speed_x_nave >= 1496 and self.speed_x_nave <= 1758 and self.speed_y_nave >= 344 and self.speed_y_nave <= 606 :
            text = font.render("Pressione a tecla E para soltar o satelite", True, yellow)
            scrn.blit(text, (600, 475))

        if self.speed_x_nave >= 142 and self.speed_x_nave <= 626 and self.speed_y_nave >= 334 and self.speed_y_nave <= 818 and self.hubble_status == 2:
            text = font.render("Pressione a tecla E para voltar a terra", True, yellow)
            scrn.blit(text, (600, 475))

        
        self.rect = self.image.get_rect()
        self.rect.topleft = self.speed_x_nave,self.speed_y_nave
         
    def finish_mission(self):
        if self.status == 2:
            return True
        
    




class Meteoro(Nave, pygame.sprite.Sprite):
    def __init__(self):
        Nave.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.sprites6 = []
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


    def checkCollision(sprite1, sprite2):
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        if col == True:
            return True 

    def process_events(self, events):
        self.speed_x_meteoro -= self.speed
        if self.speed_x_meteoro <= -120:
            self.speed_x_meteoro = 1970
            self.speed_y_meteoro = randrange(0,920)
            self.speed = randrange(2,8)
                
             
        self.rect = self.image.get_rect()
        self.rect.topleft = self.speed_x_meteoro,self.speed_y_meteoro

class Hubble(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\hubble.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\hubble2.png"))
        self.atual = 0
        self.speed_x_hubble = 1632
        self.speed_y_hubble = 672

        self.image = self.sprites[self.atual]
            
    def update(self):
        self.atual = self.atual + 0.015
        if self.atual >= len(self.sprites):
            self.atual = 0


        self.image = self.sprites[int(self.atual)]

    def process_events(self, events):
        pass
            

            
        self.rect = self.image.get_rect()
        self.rect.topleft = self.speed_x_hubble,self.speed_y_hubble
            
class ET():
    def __init__(self):
        self.speed_x_et = 1970
        self.speed_y_et = randrange(100,820)
        self.speed = 5
        self.time = 0.0


    def process_events(self, events):
        self.time += 0.030
        if self.time >= 10.0:

            self.speed_x_et -= self.speed

            scrn.blit(et,(self.speed_x_et, self.speed_y_et))

class Lancamento(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_lançamento\\lançamento1.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_lançamento\\lançamento2.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_lançamento\\lançamento3.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_lançamento\\lançamento4.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_lançamento\\lançamento5.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_lançamento\\lançamento6.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_lançamento\\lançamento7.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_lançamento\\lançamento8.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_lançamento\\lançamento9.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_lançamento\\lançamento10.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_lançamento\\lançamento11.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_lançamento\\lançamento12.png"))

        self.atual = 0
        self.image = self.sprites[self.atual]
        self.x = 0
        self.y = 0

            
    def update(self):
        self.atual = self.atual + 0.08
        if self.atual >= len(self.sprites):
            self.atual = 0


        self.image = self.sprites[int(self.atual)]


    def process_events(self, events):           
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x , self.y

class Chegada_espaco(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_chegada_espaço\\chegada1.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_chegada_espaço\\chegada2.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_chegada_espaço\\chegada3.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_chegada_espaço\\chegada4.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_chegada_espaço\\chegada5.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_chegada_espaço\\chegada6.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_chegada_espaço\\chegada7.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_chegada_espaço\\chegada8.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_chegada_espaço\\chegada9.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_chegada_espaço\\chegada10.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_chegada_espaço\\chegada11.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_chegada_espaço\\chegada12.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_chegada_espaço\\chegada13.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_chegada_espaço\\chegada14.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\sprites_chegada_espaço\\chegada15.png"))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.x = 0
        self.y = 0

            
    def update(self):
        self.atual = self.atual + 0.08
        if self.atual >= len(self.sprites):
            self.atual = 0


        self.image = self.sprites[int(self.atual)]


    def process_events(self, events):           
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x , self.y

class retorno_espaco(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\pouso\\pouso1.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\pouso\\pouso2.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\pouso\\pouso3.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\pouso\\pouso4.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\pouso\\pouso5.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\pouso\\pouso6.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\pouso\\pouso7.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\pouso\\pouso8.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\pouso\\pouso9.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\pouso\\pouso10.png"))
        self.sprites.append(pygame.image.load("C:\\Users\\Usuário\Documents\\Juan M. Silva\mostracientifica\\images\\pouso\\pouso11.png"))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.x = 0
        self.y = 0

            
    def update(self):
        self.atual = self.atual + 0.08
        if self.atual >= len(self.sprites):
            self.atual = 0


        self.image = self.sprites[int(self.atual)]


    def process_events(self, events):           
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x , self.y


naves = pygame.sprite.Group()
hubbles = pygame.sprite.Group()
meteoros = pygame.sprite.Group()
lancamentos = pygame.sprite.Group()
chegadas_espacos = pygame.sprite.Group()
voltas = pygame.sprite.Group() 
nave = Nave()
hubble = Hubble()
meteoro1 = Meteoro()
meteoro2 = Meteoro()
meteoro3 = Meteoro()
lancamento = Lancamento()
chegada_espaco = Chegada_espaco()
volta = retorno_espaco()
et1 = ET()
naves.add(nave)
hubbles.add(hubble)
meteoros.add(meteoro1)
meteoros.add(meteoro2)
meteoros.add(meteoro3)
lancamentos.add(lancamento)
chegadas_espacos.add(chegada_espaco)
voltas.add(volta)

class Game():
    def __init__(self):
        self.game_status = 1
        self.tempo = 0.0
        self.tempo2 = 0.0
        self.tempo3 = 0.0
        self.tempo4 = 0.0
        self.status_dead = 1
        self.click = 0 
        self.points = 100
        

    def process_events(self, events):
        
        if self.status_dead == 1: 
            if self.game_status == 1:
                self.tempo += 0.1
                if self.tempo <= 11.0:
                    scrn.blit(inicio, (0 , 0))
            
            if self.tempo >= 10.0:
                self.game_status = 2


            if self.game_status == 2:
                self.tempo2 += 0.1
                if self.tempo2 <= 15.0:
                    lancamento.process_events(events)
                    lancamentos.draw(scrn)
                    lancamentos.update()

            if self.tempo2 >= 15.0:
                self.game_status = 3

            if self.game_status == 3:
                self.tempo3 += 0.1
                if self.tempo3 <= 19.0:
                    chegada_espaco.process_events(events)
                    chegadas_espacos.draw(scrn)
                    chegadas_espacos.update()

            if self.tempo3 >= 18.5:
                self.game_status = 4
                        
            if self.game_status == 4:
                Scnery.paint(scrn)
                nave.process_events(events)
                hubble.process_events(events)
                 
                meteoro1.process_events(events)
                meteoro2.process_events(events)
                meteoro3.process_events(events)

                if Meteoro.checkCollision(nave, meteoro1) == True:
                    self.status_dead = 2 

                if Meteoro.checkCollision(nave, meteoro2) == True:
                    self.status_dead = 2 

                if Meteoro.checkCollision(nave, meteoro3) == True:
                    self.status_dead = 2 

                et1.process_events(events)


                naves.draw(scrn)
                naves.update()
                hubbles.update()
        
        

                meteoros.draw(scrn)
                meteoros.update()

                for e in events:
                    if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_d:
                            self.click += 2 
                        elif e.key == pygame.K_a:
                            self.click += 2 
                        elif e.key == pygame.K_w:
                            self.click += 2 
                        elif e.key == pygame.K_s:
                            self.click += 2 
                
                print(self.click)
                
            if nave.finish_mission() == True:
                self.game_status = 5

            if self.game_status == 5:
                self.status_dead = 3


        
        
        elif self.status_dead == 2:
            scrn.blit(morte,(0,0))
            self.score = self.points - self.click
            img_score = font.render("Pontos: {}".format(self.score), True, yellow)
            scrn.blit(img_score, (810, 800))

        elif self.status_dead == 3:
            scrn.blit(venceu,(0,0))
            self.score = self.points - self.click + 50
            img_score = font.render("Pontos: {}".format(self.score), True, yellow)
            scrn.blit(img_score, (810, 800))

            
        
game = Game()
pygame.display.flip()
size = 1920 // 10
Scnery = Scnery(size)
clock = pygame.time.Clock()
status = True
while (status):
    clock.tick(30)
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
            status = False
    
    scrn.fill(black)
    game.process_events(events)


    pygame.display.update()
  
pygame.quit()