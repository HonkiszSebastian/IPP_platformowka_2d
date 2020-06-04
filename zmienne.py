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
skok = 2
boost = 1
bonus = 0

plat8 = True

sekundnik = 0
typ_plat = 0

#zmienne lawy
lava_y = resolution[1] + 250
ldp = 0

#punkty
wynik = 0
punkty = 0

#Grafiki
tlo = pygame.image.load('images/tlo_1.png')
lava = pygame.image.load('images/lava.png')
lava_pos = pygame.image.load('images/pos.png')
ziemia = pygame.image.load('images/ground.png')
HP = pygame.image.load('images/hp.png')
tablica = pygame.image.load('images/tablica.png')
bat_r = pygame.image.load('images/bat_l.png')
bat_l = pygame.image.load('images/bat_r.png')
boost_img = pygame.image.load('images/boost.png')

luci_r = pygame.image.load('images/luciR.png')
luci_l = pygame.image.load('images/luciL.png')

prawo = True
przegrana = False
pomocnicza = False
wycisz = True