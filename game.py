import pygame
import sys
from random import *
import time
import math

#base
pygame.init()

font = pygame.font.SysFont("arial", 20)
sfont = pygame.font.SysFont("arial", 10)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screenX = 1000
screenY = 600
margin = 10
tick = 60
screen = pygame.display.set_mode([screenX, screenY])

pygame.display.set_caption("TEST GAME")

run = True
flag = None
clock = pygame.time.Clock()

#PLAYER
px, py = 200, 150
psize = 15
pvF = 5
pv = pvF
lv = 0
ExpFull = 10
Exp = 0
score = 0

boostFull = 500
boostRemain = 500
boostCharge = 1
boostChargeF = 1
boostUse = 7.5
boostV = 2

boostReuseFlag = False
boostReuseTime = 2.5
boostReuseF = 60 * boostReuseTime
boostReuse = boostReuseF


hpFull = 1000
hpRemain = 1000
hpRegeneration = 0.2

ex = 0
ey = 0
esize = 10
ev = 6
edmg = 250
espawn = False

paused = False
#def

def enemySpawn():
    global espawn, ex, ey

    if espawn == False:
        espawn = True
        rnum = randrange(10)
        rnum2 = randrange(10)
        if rnum % 2 == 0:
            if rnum2 % 2 == 0:
                ex = 0
            else:
                ex = screenX
            ey = randrange(screenY - 100)
        else:
            if rnum2 % 2 == 0:
                ey = 0
            else:
                ey = screenY - 100
            ex = randrange(screenX)
def enemyMove():
    global esapwn, ex, ey, px, py, esize, psize, edmg, ev, hpRemain, espawn, boostReuseFlag
    difx = (px - ex)
    dify = (py - ey)
    dif = math.sqrt((difx * difx + dify * dify))

    X = 0
    Y = 0
    if difx != 0: 
        X = difx / dif
    if dify != 0:
        Y = dify / dif

    if dif + ev >= esize + psize:
        ex += ev * X
        ey += ev * Y
    else:
        hpRemain -= edmg
        if boostReuseFlag == True:
            hpRemain -= edmg
        espawn = False
def playerMove(x, y):
    global px, py, psize
    v = pv
    if x == -1 and y == 0:
        if px - psize - v >= margin:
            px -= v
    elif x == 1 and y == 0:
        if px + psize + v <= screenX - margin:
            px += v
    elif x == 0 and y == -1:
        if py - psize - v >= margin:
            py -= v
    elif x == 0 and y == 1:
        if py + psize + v <= screenY - margin - 100:
            py += v
    elif x == -1 and y == -1:
        if px - psize - v / math.sqrt(2) >= margin:
            px -= v / math.sqrt(2)
        if py - psize - v / math.sqrt(2) >= margin:
            py -= v / math.sqrt(2)
    elif x == -1 and y == 1:
        if px - psize - v / math.sqrt(2) >= margin: 
            px -= v / math.sqrt(2)
        if py + psize + v / math.sqrt(2) <= screenY - margin - 100:
            py += v / math.sqrt(2)
    elif x == 1 and y == -1:
        if px + psize + v / math.sqrt(2) <= screenX - margin: 
            px += v / math.sqrt(2)
        if py - psize - v / math.sqrt(2) >= margin:
            py -= v / math.sqrt(2)
    elif x == 1 and y == 1:
        if px + psize + v / math.sqrt(2) <= screenX - margin:
            px += v / math.sqrt(2)
        if py + psize + v / math.sqrt(2) <= screenY - margin - 100:
            py += v / math.sqrt(2)

def hpCheck():
    global hpRemain, boostRemain, boostFull, boostReuse, boostReuseF, boostReuseFlag
    if hpRemain <= 0:
        pygame.display.update()
        lvDown()
        hpRemain = hpFull
        boostRemain = boostFull
        boostReuse = boostReuseF
        boostReuseFlag = False
def lvUp():
    global hpRegeneration, hpFull, hpRemain, boostRemain, boostFull, pvF, Exp, ExpFull, lv, boostUse, boostCharge, boostV, boostChargeF
    
    if(Exp >= ExpFull):
        lv += 1
        Exp -= ExpFull
        ExpFull *= 1.15
        hpFull += abs(lv * 4)
        hpRemain = hpFull
        hpRegeneration += 0.005
        boostFull += 10
        boostRemain = boostFull
        boostUse -= 0.005
        boostChargeF += 0.002
        boostCharge = boostChargeF
        boostV += 0.002
        pvF += 0.005
def lvDown():
    global hpRegeneration, hpFull, hpRemain, boostRemain, boostFull, pvF, Exp, ExpFull, lv, boostUse, boostCharge, boostV, boostChargeF
    lv -= 1
    Exp = 0
    ExpFull *= 1 / 1.15
    hpFull -= abs((lv + 1) * 4)
    hpRemain = hpFull
    hpRegeneration -= 0.005
    boostFull -= 10
    boostRemain = boostFull
    boostUse -= 0.005
    boostChargeF += 0.002
    boostCharge = boostChargeF
    boostV -= 0.002
    pvF -= 0.005
#text
textBoost = font.render('BOOST', True, BLACK)
textHp    = font.render('HP   ', True, BLACK)

while run:
    clock.tick(tick)
    
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            run = False
    #key input
    keys = pygame.key.get_pressed()

    #if unpaused
    if not paused:
        #fill screen
        screen.fill(WHITE)
        #score
        score += 1
        textScore = font.render(repr(score), True, BLACK)
        #exp & lv
        Exp += 0.025
        lvUp()
        textExp = font.render('Exp : ' + repr(round(Exp)) + ' / ' + repr(round(ExpFull)), True, BLACK)
        textLv = font.render('Lv : ' + repr(lv), True, BLACK)
        #show status
        textHp2 = sfont.render(repr(round(hpRemain)) + ' / ' + repr(round(hpFull)), True, BLACK)
        textBoost2 = sfont.render(repr(round(boostRemain)) + ' / ' + repr(round(boostFull)), True, BLACK)
        textV = font.render('V : ' + repr(round(pv * 1000) / 1000) , True, BLACK)
        textHpgen = font.render(repr(round(hpRegeneration * 1000 * tick) / 1000) + ' / 1s', True, BLACK)
        textBoostgen = font.render(repr(round(boostCharge * 1000 * tick) / 1000) + ' / 1s', True, BLACK)
        #enemy spawn & move
        enemySpawn()
        if espawn == True:
            enemyMove()
        hpCheck()
        #charge boost
        if boostRemain + boostChargeF <= boostFull:
            if boostReuseFlag == False:
                boostCharge = boostChargeF
                boostRemain += boostCharge
            else:
                boostCharge = boostChargeF / 10
                boostRemain += boostCharge
        #hp gen
        if hpRemain + hpRegeneration <= hpFull:
            if boostReuseFlag == False:
                hpRemain += hpRegeneration
            else:
                hpRemain -= hpRegeneration
        #boostReuse
        if boostReuseFlag == False:
            if(keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]):
                if boostRemain >= boostUse:
                    boostRemain -= boostUse
                    pv = pvF * boostV
                else:
                    boostReuseFlag = True
            else:
                pv = pvF
        else:
            boostReuse -= 1
            pv = pvF / 2
            if boostReuse == 0:
                boostReuse = boostReuseF
                boostReuseFlag = False

        #player move
        if keys[pygame.K_a] and keys[pygame.K_w]:
            playerMove(-1, -1)
        elif keys[pygame.K_a] and keys[pygame.K_s]:
            playerMove(-1, 1)
        elif keys[pygame.K_d] and keys[pygame.K_w]:
            playerMove(1, -1)
        elif keys[pygame.K_d] and keys[pygame.K_s]:
            playerMove(1, 1)
        elif keys[pygame.K_a]:
            playerMove(-1, 0) 
        elif keys[pygame.K_d]:
            playerMove(1, 0)
        elif keys[pygame.K_w]:
            playerMove(0, -1)
        elif keys[pygame.K_s]:
            playerMove(0, 1)
        #board
        pygame.draw.rect(screen, BLACK, [margin, margin, screenX - margin * 2, screenY - margin * 2 - 100], 3)
        #player
        pygame.draw.circle(screen, BLACK, [px, py], psize, 3) 
        if boostReuseFlag == True:
            pygame.draw.circle(screen, BLACK, [px, py], psize, 0)
        #enemy
        pygame.draw.circle(screen, RED, [ex, ey], esize, 0)     
        #boost
        pygame.draw.rect(screen, BLACK, [100 -2, screenY - 40 - 2, 300 + 4, 30 + 4], 5)
        if boostReuseFlag == False:
            pygame.draw.rect(screen, BLUE, [100, screenY - 40, 300 * float(boostRemain / boostFull) , 30], 0)
        else:
            pygame.draw.rect(screen, BLACK, [100, screenY - 40, 300 * float(boostRemain / boostFull) , 30], 0)
        #hp
        pygame.draw.rect(screen, BLACK, [100 -2, screenY - 90 - 2, 300 + 4, 30 + 4], 5)
        pygame.draw.rect(screen, RED, [100, screenY - 90, 300 * float(hpRemain / hpFull), 30], 0)
        #exp
        pygame.draw.rect(screen, BLACK, [420 -1, screenY - 11, 550 + 2, 5 + 2], 2)
        pygame.draw.rect(screen, (0, 200, 0), [420, screenY - 10, 550 * float(Exp / ExpFull), 5], 0)
        #text
        screen.blit(textBoost, [20, screenY - 40])
        screen.blit(textBoost2, [100, screenY - 55])
        screen.blit(textBoostgen, [100, screenY - 35])
        screen.blit(textHp, [40, screenY - 90])
        screen.blit(textHp2, [100, screenY - 105])
        screen.blit(textHpgen, [100, screenY - 85])
        screen.blit(textExp, [420, screenY - 40])
        screen.blit(textScore, [20, 20])
        screen.blit(textLv, [420, screenY - 90])
        screen.blit(textV, [500, screenY - 90])
    #pause & unpause
    if keys[pygame.K_KP_ENTER]:
        if not paused:
            paused = True
    elif keys[pygame.K_KP_0]:
        if paused:
            paused = False
    #update
    pygame.display.update()

#quit
pygame.quit()