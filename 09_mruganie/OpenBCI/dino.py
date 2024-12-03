# -*- coding: utf-8 -*-

import pygame
import random
import datetime
import time
from pyOpenBCI import OpenBCIGanglion
import multiprocessing as mp
#from psychopy import event, visual
import filterlib as flt
import blink as blk

global mac_adress
mac_adress = 'e5:32:b4:53:55:ba'


def blinks_detector(quit_program, blink_det, blinks_num, blink):
    def detect_blinks(sample):
        smp = sample.channels_data[0]
        smp_flted = frt.filterIIR(smp, 0)
        #print(smp_flted)

        brt.blink_detect(smp_flted, -38000)
        # report it the new blink is spotted
        if brt.new_blink:
            if brt.blinks_num == 1:
                # First detected blink is in fact artifact from filter
                # settling. Correct blink number by subtracting 1.
                # First "blink" successfully detected - device is connected.
                connected.set()
                print('CONNECTED. Speller starts detecting blinks.')
            else:
                blink_det.put(brt.blinks_num)
                blinks_num.value = brt.blinks_num
                blink.value = 1
                print('BLINK!')


        if quit_program.is_set():
            print('Disconnect signal sent...')
            board.stop_stream()

    if __name__ == '__main__':
        # filtering in real time object creation
        frt = flt.FltRealTime()

        # blink detection in real time object creation
        brt = blk.BlinkRealTime()

        board = OpenBCIGanglion(mac=mac_adress)
        board.start_stream(detect_blinks)

quit_program = mp.Event()
blink = mp.Value('i', 0)
blink_det = mp.Queue()
blinks_num = mp.Value('i', 0)
connected = mp.Event()

proc_blink_det = mp.Process(
    name='proc_',
    target=blinks_detector,
    args=(quit_program,  blink_det, blinks_num, blink,)
    )

proc_blink_det.start()
print('subprocess started')

#stałe
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 300
ROAD_HEIGHT = 250
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 25
DINO_POS_X = 70
DINO_POS_Y = ROAD_HEIGHT - 30
CACTUS_POS_Y = ROAD_HEIGHT - 30

pygame.init()
gameDisplay = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

#dźwięki
jumpSound = pygame.mixer.Sound("sounds/jump.wav")
dieSound = pygame.mixer.Sound("sounds/die.wav")
checkpointSound = pygame.mixer.Sound("sounds/checkPoint.wav")

#grafiki
road1 = pygame.image.load("graphics/road.png")
road2 = pygame.image.load("graphics/road.png")

dino_list = []
dino_list.append(pygame.image.load("graphics/dino.png")) #0
dino_list.append(pygame.image.load("graphics/dino_run1.png")) #1
dino_list.append(pygame.image.load("graphics/dino_run2.png")) #2
dino_list.append(pygame.image.load("graphics/dino_error.png")) #3
run_indx = 1

cactus_list = []
cactus_list.append(pygame.image.load("graphics/cactus1.png")) #0
cactus_list.append(pygame.image.load("graphics/cactus2.png")) #1
cactus_list.append(pygame.image.load("graphics/cactus3.png")) #2
cactus_list.append(pygame.image.load("graphics/cactus4.png")) #3


road1_pos_x = 0
road2_pos_x = 600

speed_was_up = True
clear_game = True
game_on = False
lost_game = True
dino_jump = False
jump_height = 7
points = 0

frames_since_cactus = 0
gen_cactus_time = 50 #moment wygenerowania pierwszego kaktusa

#napisy
font = pygame.font.Font('freesansbold.ttf', 18)
points_font = pygame.font.Font('freesansbold.ttf', 12)
startScreen = font.render('WCISNIJ SPACJE ABY ZACZAC', True, BLACK, WHITE)
startScreenRect = startScreen.get_rect()
startScreenRect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2-50)

gra_trwa = True
while gra_trwa:
    if blink.value == 1:
        if dino_jump == False:
            game_on = True
            dino_jump = True
            jumpSound.play()
            blink.value = 0
        if lost_game == True:
            time.sleep(1)
            clear_game = True
            lost_game = False
            blink.value = 0
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit_program.set()
                gra_trwa = False
            if event.key == pygame.K_SPACE and dino_jump == False:
                game_on = True
                dino_jump = True
                jumpSound.play()
            if lost_game == True and event.key == pygame.K_SPACE:
                time.sleep(1)
                clear_game = True
                lost_game = False

    #ustawienia początkowe
    if clear_game == True:
        FPS = 25
        cactus_pos_x = []
        curr_cactus = []
        speed = 10
        points = 0
        clear_game = False

    #początkowy ekran
    gameDisplay.fill(WHITE)
    gameDisplay.blit(road1, (road1_pos_x, ROAD_HEIGHT))
    if game_on == False:
        gameDisplay.blit(startScreen, startScreenRect)

    #przegrany ekran
    if game_on == True and lost_game == True:
        gameDisplay.blit(startScreen, startScreenRect)
        lostScreen = font.render('LICZBA PUNKTOW: ' + str(points), True, BLACK, WHITE)
        lostScreenRect = lostScreen.get_rect()
        lostScreenRect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2-25)
        gameDisplay.blit(lostScreen, lostScreenRect)

    #zwiększanie prędkości gry
    if speed_was_up == False and points%5 == 0:
        checkpointSound.play()
        FPS += 5
        speed_was_up = True
    if points%5 == 1:
        speed_was_up = False

    #wyświetlanie punktów
    if game_on == True:
        pointsDisplay = points_font.render('PUNKTY: ' + str(points), True, BLACK, WHITE)
        pointsRect = pointsDisplay.get_rect()
        pointsRect.center = (SCREEN_WIDTH-100, 10)
        gameDisplay.blit(pointsDisplay, pointsRect)


    #dino biegnie, jedna animacja powinna trwać 3 klatki
    if game_on == True and dino_jump == False and lost_game == False:
        if run_indx <= 3:
            dino = gameDisplay.blit(dino_list[1], (DINO_POS_X, DINO_POS_Y))
            run_indx += 1
        elif run_indx < 6:
            dino = gameDisplay.blit(dino_list[2], (DINO_POS_X, DINO_POS_Y))
            run_indx += 1
        else:
            dino = gameDisplay.blit(dino_list[2], (DINO_POS_X, DINO_POS_Y))
            run_indx = 1
    elif game_on == False:
        dino = gameDisplay.blit(dino_list[0], (DINO_POS_X, DINO_POS_Y))

    #dino skacze
    if game_on == True and dino_jump == True:
        if jump_height >= -7:
            going_up = 1
            if jump_height < 0:
                going_up = -1
            DINO_POS_Y -= (jump_height ** 2) * 0.8 * going_up
            jump_height -= 1
        else:
            dino_jump = False
            jump_height = 7
        dino = gameDisplay.blit(dino_list[0], (DINO_POS_X, DINO_POS_Y))

    #przewijanie drogi
    if game_on == True:
        frames_since_cactus += 1
        road1_pos_x -= speed
        if road1_pos_x <= -SCREEN_WIDTH:
            gameDisplay.blit(road2, (road2_pos_x, ROAD_HEIGHT))
            road2_pos_x -= speed
            if road2_pos_x == 0:
                road2_pos_x = 600
                road1_pos_x = 0

    #przeszkody
    if frames_since_cactus == gen_cactus_time:
        gen_cactus_time = random.randint(20, 50) #nowa przeszkoda generowana jest raz na 20 do 50 klatek
        gen_cactus_img = random.randint(0, 3)
        frames_since_cactus = 0
        curr_cactus.append([gen_cactus_img, SCREEN_WIDTH]) #każdy kaktus ma [swój obrazek, swoją pozycję x]

    for i in range(len(curr_cactus)):
        if curr_cactus[i][0] == 0 or curr_cactus[i][0] == 3: #obniżenie położenia Y mniejszych kaktusów
            lower = 12
        else: lower = 0
        cactus = gameDisplay.blit(cactus_list[curr_cactus[i][0]], (curr_cactus[i][1], CACTUS_POS_Y+lower))
        curr_cactus[i][1] -= speed
        #punkty
        if curr_cactus[i][1] == 0:
            points += 1
        #zderzenie
        if dino.colliderect(cactus):
            speed = 0
            if lost_game == False:
                dieSound.play()
            lost_game = True
            dino = gameDisplay.blit(dino_list[3], (DINO_POS_X, DINO_POS_Y))
            #informacja o momencie zderzenia
            #print(str(datetime.datetime.now().time()) + " punkty: " + str(points))


    pygame.display.update()
    clock.tick(FPS)

proc_blink_det.join()
print('Terminated.')
