import random
from zmienne import *

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.luci = pygame.image.load('images/luciR.png')
        self.rect = self.luci.get_rect()
        self.player_speed = resolution[0]/200
        self.player_speed_y = 0
        self.x = resolution[0]/2 - self.rect[2]/2
        self.y = resolution[1] - self.rect[3] - 10
            
player = Player()

screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('* Luci Jump *')

#fonty
font_1 = pygame.font.Font('images/slkscr.ttf', 20) 
font_2 = pygame.font.Font('images/slkscre.ttf', 15) 
font_3 = pygame.font.Font('images/slkscre.ttf', 40) 

#funkcje polozenia
def position(x, y):
    screen.blit(player.luci, (x, y))

def position_lava(x, y):
    screen.blit(lava, (lava_x, lava_y))

#napisy
def napisy(text_pkt, text_lava, text_rekord, resolution):
    screen.blit(text_pkt, (2, 0))
    screen.blit(text_lava, (2, 25))
    screen.blit(text_rekord, (2, 45))

def plik(wynik, best):
    f = open("wyniki.txt", 'r+')
    best = int(best)
    if wynik > best:
        print('.: Gratulacje! Nowy rekord :.')
        wynik = str(int(wynik))
        f.truncate(0)
        f.write(wynik)
        f.close()
    
#bloki
class Bloki(pygame.sprite.Sprite):
    def __init__(self, x_b, y_b, szerokosc, wysokosc):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((szerokosc, wysokosc))
        self.rect = self.image.get_rect()
        self.rect.x = x_b
        self.rect.y = y_b
        self.image.fill((0,0,0))

#Tworzenie grup i blokow
p1 = Bloki((random.randrange(5, resolution[0], 1))-105, resolution[1]-80, 100, 3)
p2 = Bloki((random.randrange(5, resolution[0], 1))-105, resolution[1]-160, 100, 3)
p3 = Bloki((random.randrange(5, resolution[0], 1))-105, resolution[1]-240, 100, 3)
p4 = Bloki((random.randrange(5, resolution[0], 1))-105, resolution[1]-320, 100, 3)
p5 = Bloki((random.randrange(5, resolution[0], 1))-105, resolution[1]-400, 100, 3)
p6 = Bloki((random.randrange(5, resolution[0], 1))-105, resolution[1]-480, 100, 3)
p7 = Bloki((random.randrange(5, resolution[0], 1))-105, resolution[1]-560, 100, 3)

platformy = pygame.sprite.Group()

platformy.add(p1, p2, p3, p4, p5, p6, p7)

sprity = pygame.sprite.Group()

sprity.add(player, p1, p2, p3, p4, p5, p6, p7)

#clock
clock = pygame.time.Clock()

f = open("wyniki.txt", 'r+')
best = f.read()
f.close()

while running:
    clock.tick(FPS)

    screen.blit(background, (0, 0))
    screen.blit(ground, (0, resolution[1]-przesuniecie))
    platformy.draw(screen)

    text_pkt = font_1.render('Punkty: ' + str(punkty), 1, (0,0,0)) 
    text_lava = font_2.render('Lava: ' + str(ldp), 1, (0,0,0)) 
    text_rekord = font_2.render('Rekord: ' + str(best), 1, (0,0,0))
    text_przegrana = font_3.render('.: PRZEGRANA :.', 1, (0,0,0))

    #ustawienie hit-boxow
    player.rect.top = player.y
    player.rect.left = player.x

    #kamera
    if (player.rect.top < resolution[1]/2.5) and (player.player_speed_y <= 0):
        player.y = resolution[1]/2.5
        przesuniecie = 2000
        lava_y += abs(player.player_speed_y)
        ruch = True
        wynik += abs(player.player_speed_y) 
        for i in platformy:
            i.rect.y += abs(player.player_speed_y)

    #Przeniesienie platformy
    for i in platformy:
        if i.rect.y > resolution[1]:
            i.image = pygame.Surface((random.randrange(20, 100, 1), random.randrange(2,8,1)))
            i.rect = i.image.get_rect()
            i.rect.y = (random.randrange(11, 20, 1))-10
            i.rect.x = (random.randrange(5, resolution[0], 1))-5

            typ_plat = random.randrange(0, 10, 1)

            if typ_plat == 6:
                i.image.fill((36,0,0))

            elif typ_plat == 5:
                i.image.fill((43,29,14))

            elif typ_plat == 4:
                i.image.fill((82,54,26))

    #kolizje
    kolizja = pygame.sprite.spritecollide(player, platformy, False)
    
    if kolizja and (player.player_speed_y >= 0):
        player.player_speed_y = 0
        skok = 2
    else:
        player.player_speed_y += g

    if pygame.key.get_pressed() [pygame.K_a]:
        player.x -= player.player_speed
        player.luci = pygame.image.load('images/luciL.png')

    if pygame.key.get_pressed() [pygame.K_d]:
        player.x += player.player_speed
        player.luci = pygame.image.load('images/luciR.png')

    #Blokada gracza aby nie wychodzil za ekran
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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if skok > 1:
                    player.player_speed_y -= 4.9
                    skok -= 1
                    sekundnik = 0
                elif skok == 1 and sekundnik >= 29: #skok mozliwy po 1/2 sekundy
                    player.player_speed_y -= 4.0
                    skok -= 1
 
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    odleglosc = lava_y - (player.y + player.rect[3]) 

    #lava
    lava_y -= 0.8 + punkty/1000
    ldp = lava_y - resolution[1]
    ldp = round(ldp, 0)
    if ldp < 0:
        ldp = 0

    #pozycja po zmianie
    player.y += player.player_speed_y

    position(player.x,player.y)

    #zdobyty wynik - punkty
    if wynik < abs(player.y-resolution[1])-40:
        wynik = abs(player.y-resolution[1]-40)
    punkty = wynik/10
    punkty = round(punkty,0)

    position_lava(lava_x, lava_y)
    napisy(text_pkt, text_lava, text_rekord, resolution)
    sekundnik += 1

    #wyswietlenie serduszek
    for i in range(hp):
        screen.blit(HP, (resolution[0]- 22 - i*20, 2))

    #Przegrana
    if odleglosc <= 0 or player.y > resolution[1]:
        screen.blit(text_przegrana, (2, resolution[1]/2-30))
        if ostatnia == True:
            pygame.display.flip()    
            ostatnia = False
            print('Wynik koncowy: ', punkty)
            plik(punkty, best)
    else:    
        pygame.display.flip()  

pygame.quit()
