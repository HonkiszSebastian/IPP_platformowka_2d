import pygame

#ekran
resolution = [400, 600]
FPS = 60
running = True

#zmienne gry
g = 0.1
odleglosc = 0
przesuniecie = 2

hp = 3

ruch = False
ostatnia = True
skok = 2

sekundnik = 0
typ_plat = 0

#zmienne lawy
lava_x = -10
lava_y = resolution[1] + 250
ldp = 0

#punkty
wynik = 0
punkty = 0

#Grafiki
background = pygame.image.load('images/background.png')
lava = pygame.image.load('images/lava.png')
ground = pygame.image.load('images/ground.png')
HP = pygame.image.load('images/hp.png')



