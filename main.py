import random
from zmienne import *

pygame.init()
pygame.mixer.init()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.luci = pygame.image.load('images/hitbox.png')
        self.rect = self.luci.get_rect()
        self.player_speed = resolution[0]/200
        self.player_speed_y = 0
        self.x = resolution[0]/2 - self.rect[2]/2
        self.y = resolution[1] - self.rect[3] - 10

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.bat = pygame.image.load('images/bat_l.png')
        self.rect = self.bat.get_rect()
        self.predkosc = 0.05
        self.predkosc_x = 0
        self.predkosc_y = 0
        self.x = resolution[0]/2
        self.y = -1000
        self.rect.x = self.x
        self.rect.y = self.y

#bloki
class Bloki(pygame.sprite.Sprite):
    def __init__(self, x, y, szerokosc, wysokosc):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((szerokosc, wysokosc))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill((0,0,0))

class Kula(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.k = pygame.image.load('images/KO.png')
        self.rect = self.k.get_rect()
        self.x = 0
        self.y = 610
        self.predkosc_x = 0
        self.predkosc_y = 0
        self.rect.x = self.x
        self.rect.y = self.y
    
player = Player()
bat_1 = Enemy()
k1 = Kula()
k2 = Kula()

screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('* Luci Jump *')

#napisy
font_1 = pygame.font.Font('images/slkscr.ttf', 20) 
font_2 = pygame.font.Font('images/slkscre.ttf', 15) 
font_3 = pygame.font.Font('images/slkscre.ttf', 40) 

pygame.mixer.music.load('images/st.mp3')

#funkcje polozenia
def position(x, y):
    screen.blit(player.luci, (x, y))

def position_luci(x, y):
    if prawo == True:
        screen.blit(luci_r, (x, y-25))
    else:
        screen.blit(luci_l, (x, y-25))

#pozycja nietoperzy
def enemy_pos():
    delta_x1 = bat_1.x - player.x
    delta_y1 = bat_1.y - player.y

    if delta_x1 > 0:
        bat_1.predkosc_x -= bat_1.predkosc
        if nietoperz == True:
            bat_1.bat = pygame.image.load('images/bat_2l.png')
        else:
            bat_1.bat = pygame.image.load('images/bat_l.png')
    elif delta_x1 < 0:
        bat_1.predkosc_x += bat_1.predkosc
        if nietoperz == True:
            bat_1.bat = pygame.image.load('images/bat_2r.png')
        else:
            bat_1.bat = pygame.image.load('images/bat_r.png')
    
    if delta_y1 > 0:
        bat_1.predkosc_y -= bat_1.predkosc
    elif delta_y1 < 0:
        bat_1.predkosc_y += bat_1.predkosc
    
    if bat_1.predkosc_x > 2:
        bat_1.predkosc_x = 2
    elif bat_1.predkosc_x < -2:
        bat_1.predkosc_x = -2
    if bat_1.predkosc_y > 2:
        bat_1.predkosc_y = 2
    if bat_1.predkosc_y < -2:
        bat_1.predkosc_y = -2

    bat_1.y += bat_1.predkosc_y
    bat_1.x += bat_1.predkosc_x

    bat_1.rect.x = bat_1.x
    bat_1.rect.y = bat_1.y
    
    screen.blit(bat_1.bat, (bat_1.x,bat_1.y))

#pozycja lawy
def position_lava():
    screen.blit(lava, (0, lava_y))
    screen.blit(lava_pos, (0, lava_y-550))

#pozycja kuli 
def kula_pozycja(y, g):

    if k1.y >= 1200:
        k1.y = 600 + y
        k1.x = (random.randrange(0, 400, 1))
        k1.predkosc_y = -(random.randrange(200, 300, 1))/40
        k1.predkosc_x = ((random.randrange(100, 300, 1))/100) - 1.5
    
    if k2.y >= 6000:
        k2.y = 600 + y
        k2.x = (random.randrange(0, 400, 1))
        k2.predkosc_y = -(random.randrange(250, 400, 1))/40
        k2.predkosc_x = ((random.randrange(100, 300, 1))/100) - 1.5

    k1.x = k1.x + k1.predkosc_x
    k1.y = k1.y + k1.predkosc_y
    k1.predkosc_y = k1.predkosc_y + g

    k2.x = k2.x + k2.predkosc_x
    k2.y = k2.y + k2.predkosc_y
    k2.predkosc_y = k2.predkosc_y + g

    k1.rect.x = k1.x
    k1.rect.y = k1.y

    k2.rect.x = k2.x
    k2.rect.y = k2.y

    screen.blit(k1.k, (k1.x,k1.y))
    screen.blit(k2.k, (k2.x,k2.y))

#wyswietlanie serduszek i boosta
def wyswietlanie_hp(hp, resolution):
    for i in range(hp):
        screen.blit(HP, (resolution[0]- 22 - i*20, 2))

def wyswietlanie_boost(b, resolution):
    for i in range(b):
        screen.blit(boost_img, (resolution[0]- 22 - i*20, 22))

#napisy
def napisy(text_pkt, text_lava, text_rekord, resolution):
    screen.blit(tablica, (0, 0))
    if wycisz == False:
        screen.blit(m_t, (150, 38))

    screen.blit(text_pkt_b, (1, -1))
    screen.blit(text_pkt, (2, 0))

    screen.blit(text_lava_b, (1, 44))
    screen.blit(text_lava, (2, 45))

    screen.blit(text_rekord_b, (1, 24))
    screen.blit(text_rekord, (2, 25))

#operacje na pliku
def plik(wynik, best):
    f = open("wyniki.txt", 'r+')
    best = int(best)
    if wynik > best:
        print('.: Gratulacje! Nowy rekord :.')
        wynik = str(int(wynik))
        f.truncate(0)
        f.write(wynik)
        f.close()

#przesuwanie sie tla
def tlo_cegly(pkt):
    if pkt < 40:
        pkt = 0
    else:
        pkt -= 40
    pkt_m = pkt % 245
    screen.blit(tlo, (0, -280+pkt_m))
    
#ruchoma platforma    
def plat_8():
    p8.image.fill((66,0,66)) 

def plat_9():
    p9.image.fill((0,33,19)) 

        
#grupy i bloki
p1 = Bloki((random.randrange(5, resolution[0], 1))-105, resolution[1]-80, 100, 3)
p2 = Bloki((random.randrange(5, resolution[0], 1))-105, resolution[1]-160, 100, 3)
p3 = Bloki((random.randrange(5, resolution[0], 1))-105, resolution[1]-240, 100, 3)
p4 = Bloki((random.randrange(5, resolution[0], 1))-105, resolution[1]-320, 100, 3)
p5 = Bloki((random.randrange(5, resolution[0], 1))-105, resolution[1]-400, 100, 3)
p6 = Bloki((random.randrange(5, resolution[0], 1))-105, resolution[1]-480, 100, 3)
p7 = Bloki((random.randrange(5, resolution[0], 1))-105, resolution[1]-560, 100, 3)
p8 = Bloki((random.randrange(5, resolution[0], 1))-100, 140, 100, 3)
p9 = Bloki((random.randrange(5, resolution[0], 1))-100, -500, 50, 3)

platformy = pygame.sprite.Group()
nietopyrki = pygame.sprite.Group()
kule = pygame.sprite.Group()

platformy.add(p1, p2, p3, p4, p5, p6, p7, p8, p9)
nietopyrki.add(bat_1)
kule.add(k1, k2)

sprity = pygame.sprite.Group()

sprity.add(player,bat_1, k1, k2, p1, p2, p3, p4, p5, p6, p7, p8, p9)

#clock
clock = pygame.time.Clock()

#odczytanie naklepszego wyniku z pliku
f = open("wyniki.txt", 'r+')
best = f.read()
f.close()

#dzwiek
pygame.mixer.music.play(-1, 0)

while running:
    clock.tick(FPS)
    
    tlo_cegly(punkty)
    
    screen.blit(ziemia, (0, resolution[1]-przesuniecie))
    platformy.draw(screen)

    text_pkt = font_1.render('Punkty: ' + str(punkty), 1, (0,0,0)) 
    text_pkt_b = font_1.render('Punkty: ' + str(punkty), 1, (255,255,255)) 

    text_lava = font_2.render('Lava: ' + str(ldp), 1, (0,0,0)) 
    text_lava_b = font_2.render('Lava: ' + str(ldp), 1, (255,255,255))

    text_rekord = font_2.render('Rekord: ' + str(best), 1, (0,0,0))
    text_rekord_b = font_2.render('Rekord: ' + str(best), 1, (255,255,255))

    text_przegrana = font_3.render('.: PRZEGRANA :.', 1, (0,0,0))

    #ustawienie hit-boxow
    player.rect.top = player.y
    player.rect.left = player.x

    #'kamera'
    if (player.rect.top < resolution[1]/2.5) and (player.player_speed_y <= 0):
        player.y = resolution[1]/2.5
        przesuniecie = 2000
        lava_y += abs(player.player_speed_y)
        bat_1.y += abs(player.player_speed_y)
        k1.y += abs(player.player_speed_y)
        k2.y += abs(player.player_speed_y)
        ruch = True
        wynik += abs(player.player_speed_y) 
        for i in platformy:
            i.rect.y += abs(player.player_speed_y)

    #kolizje
    kolizja = pygame.sprite.spritecollide(player, platformy, False)
    kolizja2 = pygame.sprite.spritecollide(player, nietopyrki, False)
    kolizja3 = pygame.sprite.spritecollide(player, kule, False)

    if kolizja3:
        k1.x = -1000
        k2.x = -1000
        hp -= 1

    if kolizja2:
        hp -= 1
        bat_1.x = (random.randrange(0, resolution[0], 1))
        bat_1.y = (random.randrange(0, 500, 1))-600
        if nietoperz == True:
            nietoperz = False
        else:
            nietoperz = True

    #nietoperz w lavie
    if (bat_1.y+15) >= lava_y:
        bat_1.x = (random.randrange(0, resolution[0], 1))
        bat_1.y = (random.randrange(0, 500, 1))-600
        if nietoperz == True:
            nietoperz = False
        else:
            nietoperz = True
    
    if kolizja and (player.player_speed_y >= 0):
        player.player_speed_y = 0
        skok = 2
    else:
        player.player_speed_y += g

    #przeniesienie platformy
    for i in platformy:
        if i.rect.y > resolution[1]:
            i.image = pygame.Surface((random.randrange(20, 100, 1), random.randrange(3,7,1)))
            i.rect = i.image.get_rect()
            i.rect.y = (random.randrange(11, 20, 1))-10
            i.rect.x = (random.randrange(5, resolution[0], 1))-5
            i.image.fill((0,0,0))
    plat_8()
    plat_9()

    p9.rect.y += 1

    if p8.rect.x -100 > resolution[0]:
        plat8 = False
    elif p8.rect.x < -300:
        plat8 = True

    if plat8 == True:
        p8.rect.x += (1+(punkty/1000))
    if plat8 == False:
        p8.rect.x -= (1+(punkty/1000))

    #sterowanie lewo/prawo
    if przegrana == False:
        if pygame.key.get_pressed() [pygame.K_a]:
            player.x -= player.player_speed
            prawo = False

        if pygame.key.get_pressed() [pygame.K_d]:
            player.x += player.player_speed
            prawo = True

    #Blokada gracza
    if player.x < 0:
        player.x = 0

    if player.x + player.rect[2] > resolution[0]:
        player.x = resolution[0] - player.rect[2]

    if ruch == False:
        if player.y > resolution[1] - (player.rect[3]+2):
            player.y = resolution[1] - (player.rect[3]+2)
            player.player_speed_y = 0
            skok = 2

    #Klawisze 
    for event in pygame.event.get():
        if przegrana == False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if skok > 1:
                        player.player_speed_y -= 4.9
                        skok -= 1
                        sekundnik = 0
                    elif skok == 1 and sekundnik >= 29: #skok mozliwy po 1/2 sekundy
                        player.player_speed_y -= 4.0
                        skok -= 1
                if event.key == pygame.K_SPACE:
                    if boost > 0:
                        boost -=1
                        player.player_speed_y = -7
                if event.key == pygame.K_p:
                    if pause == True:
                        pause = False
                    else:
                        pause = True

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if  event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            if wycisz == True:  
                pygame.mixer.music.pause()
                wycisz = False
            else:
                pygame.mixer.music.unpause()
                wycisz = True

    #lava
    odleglosc = lava_y - (player.y + player.rect[3]) 

    if przegrana == False:
        lava_y -= (0.65 + punkty/1000 + odleglosc/1000)
    ldp = lava_y - resolution[1]
    ldp = round(ldp, 0)
    ldp2 = ldp
    if ldp < 0:
        ldp = 0

    #pozycja po zmianie
    player.y += player.player_speed_y

    position(player.x,player.y)         #pozycja modelu hit-boxu

    position_luci(player.x,player.y)    #pozycja postaci (grafiki)
    enemy_pos()

    #zdobyty wynik - punkty
    if wynik < abs(player.y-resolution[1])-40:
        wynik = abs(player.y-resolution[1]-40)
    punkty = wynik/10
    punkty = round(punkty,0)

    kula_pozycja(ldp2, g)

    position_lava()
    napisy(text_pkt, text_lava, text_rekord, resolution)
    sekundnik += 1
    bonus += 1

    if bonus > 3000:
        bonus = 0
        boost += 1


    #wyswietlenie zasobow
    if przegrana == False:
        wyswietlanie_hp(hp, resolution)
        wyswietlanie_boost(boost, resolution)

    #Przegrana
    if odleglosc <= 0 or player.y > resolution[1]:
        przegrana = True
        hp = 0
        for i in platformy:
            i.kill()
        bat_1.kill()
        k1.kill()
        k2.kill()

    if hp <= 0:
        przegrana = True
        bat_1.kill()
        k1.kill()
        k2.kill()
        

    if przegrana == True:
        screen.blit(text_przegrana, (2, resolution[1]/2-30))
        player.player_speed_y = 0
        if pomocnicza == False:
            print('Wynik koncowy: ', punkty)
            plik(punkty, best)
            pomocnicza = True
    pygame.display.flip()        

pygame.quit()
