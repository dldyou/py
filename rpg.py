import pygame
import sys
from random import *
import time
from math import *

pygame.init()

#font
font_size60 = pygame.font.SysFont("arial", 60)
font_size50 = pygame.font.SysFont("arial", 50)
font_size40 = pygame.font.SysFont("arial", 40)
font_size30 = pygame.font.SysFont("arial", 30)
font_size20 = pygame.font.SysFont("arial", 20)
font_size10 = pygame.font.SysFont("arial", 10)

#color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#screen
screenX = 1000
screenY = 600
margin = 10
screenX2 = 400
scr = pygame.display.set_mode([screenX + screenX2, screenY])
# scr = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#title
pygame.display.set_caption("RPG V0.1")

#toggle
run = True
paused = False
move = None

#tick
tick = 60
clock = pygame.time.Clock()

#player
px = screenX / 2
py = screenY / 2
psize = 15
pspeedF = 3
pspeed = pspeedF
plv = 1

hpFull = 100
hpRemain = hpFull
hpRegen = 5

expFull = 10
expNow = 1000000
time = 0

pattackFullTimeF = 60 * 1
pattackFullTime = pattackFullTimeF
pattackRemainTime = 0
pattackDmgF = 30
pattackDmg = pattackDmgF
pattackDistance = 50
pattackRange = 30
pattackPos_x = 0
pattackPos_y = 0
pattackFlag = False
pattackedFlag = False

pskillCool_q = 60 * 5
pskillRemainCool_q = 0
skillQTime = 1
qt = 0

pskillCool_w = 60 * 23
pskillRemainCool_w = 0
skillWTime = 6
skillW_range = 150
wt = 0

pskillCool_e = 60 * 15
pskillRemainCool_e = 0
skillETime = 3
et = 0
skillE_range = 130
skillEtick = 0.2
skillE_dmg_multiple = 1.25
skillE = False

pskillCool_r = 60 * 40
pskillRemainCool_r = 0
skillRTime = 7
rt = 0

pStatRemain = 0

#enemy
epos = []
edir = []
elv = []
ehpFull = []
ehpRemain = []
ehpRegen = []
eattack = [] 
eattackFullTimeF = 60 * 0.5
eattackRemainTime = []
esize = 20
espeed = 0.5
enemyRespawnTime_full = 60 * 1.5
enemyRespawnTime_remain = enemyRespawnTime_full
enemyRespawnFlag = True

enemyDirChangeTime_full = 60 * 1
enemyDirChangeTimt_remain = enemyDirChangeTime_full
enemyDirChangeFlag = False
enemyEntity = 0
enemyEntity_max = 15

firstHitFlag = False
#enemy


#mouse
mouseX = 0
mouseY = 0

#game(main)
while run:
    clock.tick(tick)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    mpressed_left, mpressed_middle, mpressed_right = pygame.mouse.get_pressed()
    cursorX, cursorY = pygame.mouse.get_pos()
    
    #game running
    if not paused:
        hpRegen = plv
        scr.fill(WHITE)
        time += 1
        if time == 60:
            time = 0
            #hp regen
            if hpRemain + hpRegen <= hpFull:
                hpRemain += hpRegen
            else:
                hpRemain = hpFull
        while expNow >= expFull:
            expNow -= expFull
            plv += 1
            expFull = round(expFull * 1.12 + 10)
            pattackDmgF += 1 + round(plv / 3) + round(plv / 5) * 3 + round(plv / 10) * 5 + round(plv / 100) * 25
            pattackDmg = pattackDmgF
            hpFull += (round(plv / 5) + 1) * 10
            hpRemain = hpFull
        if hpRemain <= 0:
            if expNow == 0:
                if hpFull - 3 * plv >= 10:
                    hpFull -= 3 * plv
            expNow = 0
            hpRemain = hpFull
        #text
        textLv = font_size30.render('LV : ' + str(plv), True, BLACK)
        textExp = font_size10.render('Exp : ' + str(expNow) + ' / ' + str(expFull), True, BLACK)
        textHp = font_size10.render(' Hp : ' + str(hpRemain) + ' / ' + str(hpFull), True, BLACK)
        #attack
        if keys[pygame.K_a]:
            mx, my = pygame.mouse.get_pos()
            difx = mx - px
            dify = my - py
            dif = sqrt(pow(difx, 2) + pow(dify, 2))
            if dif != 0:
                cost = difx / dif
                sint = dify / dif

                pattackPos_x = px + pattackDistance * cost
                pattackPos_y = py + pattackDistance * sint
            if pattackRemainTime == pattackFullTime:
                pygame.draw.circle(scr, RED, [pattackPos_x, pattackPos_y], pattackRange, 0)
            else:
                pygame.draw.circle(scr, BLACK, [pattackPos_x, pattackPos_y], pattackRange, 2)
        if pattackRemainTime != pattackFullTime:
            pattackRemainTime += 1
        if mpressed_left: 
            mx, my = pygame.mouse.get_pos()
            if pattackRemainTime > 0.5 * pattackFullTime and mx < screenX:
                difx = mx - px
                dify = my - py
                dif = sqrt(pow(difx, 2) + pow(dify, 2))

                if dif != 0:
                    dmg = round(pattackDmg * pattackRemainTime / pattackFullTime)
                    if pattackRemainTime == pattackFullTime:
                        dmg += plv * 3 + round(dmg / 5)

                    cost = difx / dif
                    sint = dify / dif

                    pattackPos_x = px + pattackDistance * cost
                    pattackPos_y = py + pattackDistance * sint

                    print(dmg)
                    pygame.draw.circle(scr, BLACK, [pattackPos_x, pattackPos_y], pattackRange, 0)
                    pattackRemainTime = 0
                    pattackFlag = True
        #enemyRespawn
        if enemyRespawnFlag == False:
            if enemyRespawnTime_remain != 0:
                enemyRespawnTime_remain -= 1
            else:
                enemyRespawnTime_remain = enemyRespawnTime_full
                enemyRespawnFlag = True
        else:
            if enemyEntity != enemyEntity_max:
                enemyRespawnFlag = False
                #enemyRespawn
                enemySpawnX = 0
                enemySpawnY = 0
                enemy_player_dif = 0
                #safe zone
                while enemy_player_dif < psize + esize + 20:
                    enemySpawnX = randrange(screenX - esize * 2 - 10) + esize + 5
                    enemySpawnY = randrange(screenY - esize * 2 - 10) + esize + 5
                    difx = enemySpawnX - px
                    dify = enemySpawnY - py
                    enemy_player_dif = sqrt(pow(difx, 2) + pow(dify, 2))
                epos.append([enemySpawnX, enemySpawnY])
                edir.append(randrange(361))
                lv_range = 10 + round(plv / 5) * 6
                elv.append(randrange(lv_range) + 1)
                lv = elv[enemyEntity]
                hp = lv * (lv * 2 + 5) + randrange(lv * 3)
                ehpFull.append(hp)
                ehpRemain.append(hp)
                ehpRegen.append(lv + round(lv / 10) * 5 + round(lv / 20) * 10 + round(lv / 50) * 50)
                eattack.append(lv * 4 + randrange(round(lv / 2) + 1) + 15 * round(lv / 5))
                eattackRemainTime.append(eattackFullTimeF)
                enemyEntity += 1
        #enemyMoveDirChange 
        if enemyDirChangeFlag == False:
            if enemyDirChangeTimt_remain != 0:
                enemyDirChangeTimt_remain -= 1
            else:
                enemyDirChangeTimt_remain = enemyDirChangeTime_full
                enemyDirChangeFlag = True
        else:
            for i in range(enemyEntity):
                if ehpRemain[i] + ehpRegen[i] <= ehpFull[i]:
                    ehpRemain[i] += ehpRegen[i]
                else:
                    ehpRemain[i] = ehpFull[i]
                isChangeDir = randrange(100)
                if isChangeDir % 2 == 0:
                    edir[i] = randrange(361)
            enemyDirChangeFlag = False
        #enemy
        dead = 0
        for i in range(enemyEntity):
            enemyDeadFlag = False
            idx = i - dead
            ex, ey = epos[idx]
            difx = px - ex
            dify = py - ey
            dif = sqrt(pow(difx, 2) + pow(dify, 2))

            if eattackRemainTime[idx] != 0:
                eattackRemainTime[idx] -= 1
            
            if dif < esize * 5:
                if dif > (psize + esize) / 1.3:
                    evx = espeed * difx / dif * 4
                    evy = espeed * dify / dif * 4
                if dif < psize + esize: #enemy attack player
                    if eattackRemainTime[idx] == 0:
                        hpRemain -= eattack[idx]
                        knockbackX = pspeed * difx / dif * 5
                        knockbackY = pspeed * dify / dif * 5
                        if (px + knockbackX > 0) and (px + knockbackX < screenX):
                            px += knockbackX
                        if (py + knockbackY > 0) and (py + knockbackY < screenY):
                            py += knockbackY
                        eattackRemainTime[idx] = eattackFullTimeF
            else:
                evx = espeed * cos(edir[idx])
                evy = espeed * sin(edir[idx])
            
            if skillE == True:
                if dif < skillE_range + esize:
                    if et % (60 * skillEtick) == 0:
                        vx = -espeed * difx / dif * 10
                        vy = -espeed * dify / dif * 10
                        skillE_dmg = round(pattackDmg * skillE_dmg_multiple)        
                        if ex + vx - esize > 0 and ex + vx + esize < screenX:
                            ex += vx
                        if ey + vy - esize > 0 and ey + vy + esize < screenY:
                            ey += vy
                        ehpRemain[idx] -= skillE_dmg
                        font_pdmgShow = font_size20.render(repr(skillE_dmg), True, BLACK)
                        scr.blit(font_pdmgShow, (ex - 15, ey - 60))
                        firstHitFlag = True
                        textInfo = font_size20.render('LV: ' + repr(elv[idx]) + ' HP: ' + repr(ehpRemain[idx]) + ' / ' + repr(ehpFull[idx]) + ' ATK: ' + repr(eattack[idx]), True, BLACK)
            if wt != 0:
                if dif < skillW_range + esize:
                    evx = 0
                    evy = 0
                    if dif > esize + psize + 15:
                        vx = espeed * difx / dif * 5
                        vy = espeed * dify / dif * 5
                        if ex + vx - esize > 0 and ex + vx + esize < screenX:
                            ex += vx
                        if ey + vy - esize > 0 and ey + vy + esize < screenY:
                            ey += vy
                    else:
                        vx = -espeed * difx / dif * 10
                        vy = -espeed * dify / dif * 10
                        if ex + vx - esize > 0 and ex + vx + esize < screenX:
                            ex += vx
                        if ey + vy - esize > 0 and ey + vy + esize < screenY:
                            ey += vy
                    firstHitFlag = True
                    textInfo = font_size20.render('LV: ' + repr(elv[idx]) + ' HP: ' + repr(ehpRemain[idx]) + ' / ' + repr(ehpFull[idx]) + ' ATK: ' + repr(eattack[idx]), True, BLACK)
            difx2 = pattackPos_x - ex
            dify2 = pattackPos_y - ey
            dif2 = sqrt(pow(difx2, 2) + pow(dify2, 2))

            if (dif2 <= pattackRange + esize) and pattackFlag:
                evx = -evx * 20
                evy = -evy * 20
                ehpRemain[idx] -= dmg
                font_pdmgShow = font_size20.render(repr(dmg), True, BLACK)
                scr.blit(font_pdmgShow, (ex - 15, ey - 60))
                firstHitFlag = True
                textInfo = font_size20.render('LV: ' + repr(elv[idx]) + ' HP: ' + repr(ehpRemain[idx]) + ' / ' + repr(ehpFull[idx]) + ' ATK: ' + repr(eattack[idx]), True, BLACK)
            if ehpRemain[idx] <= 0:
                exp_multiple = 1
                exp_multiple = elv[idx] / plv
                if exp_multiple > 2:
                    exp_multiple = 2
                elif exp_multiple < 0.5:
                    exp_multiple = 0.5
                expP = round(elv[idx] * (elv[idx] + 1) * exp_multiple) 
                if elv[idx] >= 50:
                    expP *= 10
                if elv[idx] >= 100:
                    expP *= 10
                expNow += expP
                
                ehpRemain.pop(idx)
                eattack.pop(idx)
                ehpFull.pop(idx)
                ehpRegen.pop(idx)
                edir.pop(idx)
                epos.pop(idx)
                elv.pop(idx)
                dead += 1
                enemyDeadFlag = True
                firstHitFlag = False
            if not (ex + evx < esize or ex + evx > screenX - esize):
                ex += evx
            if not (ey + evy < esize or ey + evy > screenY - esize):
                ey += evy
            if not enemyDeadFlag:
                epos[idx] = (ex, ey)
                
        pattackFlag = False
        enemyEntity -= dead
        #player move
        if mpressed_right: 
            move = True
            mouseX, mouseY = pygame.mouse.get_pos()
            if mouseX >= screenX:
                mouseX = screenX
            pygame.draw.circle(scr, RED, [mouseX, mouseY], 10, 0)
            
        if move:
            difx = mouseX - px
            dify = mouseY - py
            dif = sqrt(pow(difx, 2) + pow(dify, 2))
            
            if dif != 0:
                cost = difx / dif
                sint = dify / dif
                px += pspeed * cost
                py += pspeed * sint

            if dif < pspeed:
                px = mouseX
                py = mouseY
                move = False
        #skill
        if pskillRemainCool_q != 0:
            pskillRemainCool_q -= 1
        if pskillRemainCool_w != 0:
            pskillRemainCool_w -= 1
        if pskillRemainCool_e != 0:
            pskillRemainCool_e -= 1
        if pskillRemainCool_r != 0:
            pskillRemainCool_r -= 1
            
        if pskillRemainCool_q / 60 >= 0.5:
            textQ = font_size30.render(repr(round(pskillRemainCool_q / 60)), True, BLACK)
        else:
            textQ = font_size30.render(repr(round(pskillRemainCool_q / 6) / 10), True, BLACK)
        if pskillRemainCool_w / 60 >= 0.5:
            textW = font_size30.render(repr(round(pskillRemainCool_w / 60)), True, BLACK)
        else:
            textW = font_size30.render(repr(round(pskillRemainCool_w / 6) / 10), True, BLACK)
        if pskillRemainCool_e / 60 >= 0.5:
            textE = font_size30.render(repr(round(pskillRemainCool_e / 60)), True, BLACK)
        else:
            textE = font_size30.render(repr(round(pskillRemainCool_e / 6) / 10), True, BLACK)
        if pskillRemainCool_r / 60 >= 0.5:
            textR = font_size30.render(repr(round(pskillRemainCool_r / 60)), True, BLACK)
        else:
            textR = font_size30.render(repr(round(pskillRemainCool_r / 6) / 10), True, BLACK)
        
        if qt != 0:
            qt += 1
            if qt == 60 * skillQTime:
                pspeed = pspeedF
                qt = 0
        if wt != 0:
            wt += 1
            if wt == 60 * skillWTime:
                wt = 0
        if et != 0:
            et += 1
            if et == 60 * skillETime:
                skillE = False
                et = 0
        if rt != 0:
            rt += 1
            if rt == 60 * skillRTime:
                pattackFullTime = pattackFullTimeF
                pattackDmg = pattackDmgF
                rt = 0
            
        if keys[pygame.K_q] and pskillRemainCool_q == 0:
            print('skill Q')
            pspeed *= (2 + 0.01 * plv)
            qt += 1
            pskillRemainCool_q = pskillCool_q
        if keys[pygame.K_w] and pskillRemainCool_w == 0:
            print('skill W')
            wt += 1
            pskillRemainCool_w = pskillCool_w       
        if keys[pygame.K_e] and pskillRemainCool_e == 0:
            print('skill E')
            skillE = True
            et += 1
            pskillRemainCool_e = pskillCool_e
        if keys[pygame.K_r] and pskillRemainCool_r == 0:
            print('skill R')
            decreaseTime = 0.005 * plv
            dmgMultiple = 0.01 * plv
            if decreaseTime >= 0.95:
                decreaseTime = 0.95
            pattackFullTime = round(pattackFullTime * (1 - decreaseTime))
            
            pattackRemainTime = 0
            pattackDmg = round(pattackDmg * (1 + dmgMultiple) + round(plv / 2) * 50)
            rt += 1
            pskillRemainCool_r = pskillCool_r

    #pause & unpause
    if keys[pygame.K_KP_ENTER]:
        if not paused:
            paused = True
    elif keys[pygame.K_KP_0]:
        if paused:
            paused = False

    if keys[pygame.K_SPACE]:
        expNow += round(expFull / 10)
    #draw

    #enemy
    for i, (enemy_x, enemy_y) in enumerate(epos):
        circleC_e = 255 - 255 * eattackRemainTime[i] / eattackFullTimeF
        pygame.draw.circle(scr, (circleC_e, 0, 0), [enemy_x, enemy_y], esize, 0)
        pygame.draw.circle(scr, RED, [enemy_x, enemy_y], esize, 3)
        if not ehpRemain[i] == ehpFull[i]:
            pygame.draw.rect(scr, BLACK, [enemy_x - 26, enemy_y - 31, 51, 7], 2)
            pygame.draw.rect(scr, RED, [enemy_x - 25, enemy_y - 30, 50 * ehpRemain[i] / ehpFull[i], 5], 0)

    #player
    if skillE:
        pygame.draw.circle(scr, (255, 255, 0), [px, py], skillE_range, 3)
        if et % (60 * skillEtick) == 0:
            pygame.draw.circle(scr, (255, 255, 0), [px, py], skillE_range, 0)
    if wt != 0:
        pygame.draw.circle(scr, BLUE, [px, py], skillW_range, 3)
    circleC = 255 - 255 * pattackRemainTime / pattackFullTime
    if circleC != 0:
        pygame.draw.circle(scr, (circleC, circleC, circleC), [px, py], psize, 0)
    else:
        pygame.draw.circle(scr, BLUE, [px, py], psize, 0)
    
    if qt != 0:
        pygame.draw.circle(scr, (50, 50, 200), [px, py], psize + 2, 3)
    if rt == 0:
        pygame.draw.circle(scr, BLACK, [px, py], psize, 3)
    else:
        pygame.draw.circle(scr, GREEN, [px, py], psize, 3)
    if hpRemain != hpFull:
        pygame.draw.rect(scr, BLACK, [px - 31, py - 31, 62, 7], 2)
        pygame.draw.rect(scr, RED, [px - 30, py - 30, 60 * hpRemain / hpFull, 5], 0)
    #board2
    pygame.draw.rect(scr, WHITE, [screenX, 0, screenX2, screenY], 0)
    pygame.draw.rect(scr, BLACK, [screenX, 0, screenX2, screenY], 3)

    pygame.draw.rect(scr, (50, 255, 50), [screenX + 20, 60, (screenX2 - 40) * expNow / expFull, 15], 0)
    pygame.draw.rect(scr, BLACK, [screenX + 20, 60, screenX2 - 40, 15], 2)

    pygame.draw.rect(scr, RED, [screenX + 20, 80, (screenX2 - 40) * hpRemain / hpFull, 15], 0)
    pygame.draw.rect(scr, BLACK, [screenX + 20, 80, screenX2 - 40, 15], 2)

    pygame.draw.rect(scr, BLACK, [screenX + 20, 120, 80, 80], 2)
    pygame.draw.rect(scr, BLACK, [screenX + 110, 120, 80, 80], 2)
    pygame.draw.rect(scr, BLACK, [screenX + 200, 120, 80, 80], 2)
    pygame.draw.rect(scr, BLACK, [screenX + 290, 120, 80, 80], 2)

    pygame.draw.rect(scr, BLACK, [screenX + 20, 200, 80, 25], 2)
    pygame.draw.rect(scr, BLACK, [screenX + 110, 200, 80, 25], 2)
    pygame.draw.rect(scr, BLACK, [screenX + 200, 200, 80, 25], 2)
    pygame.draw.rect(scr, BLACK, [screenX + 290, 200, 80, 25], 2)
    
    if pskillRemainCool_q == 0:
        pygame.draw.rect(scr, (50, 50, 50), [screenX + 20, 120, 80, 80], 0)
    if pskillRemainCool_w == 0:
        pygame.draw.rect(scr, (50, 50, 50), [screenX + 110, 120, 80, 80], 0)
    if pskillRemainCool_e == 0:
        pygame.draw.rect(scr, (50, 50, 50), [screenX + 200, 120, 80, 80], 0)    
    if pskillRemainCool_r == 0:
        pygame.draw.rect(scr, (50, 50, 50), [screenX + 290, 120, 80, 80], 0)
    #text
    scr.blit(textLv, [screenX + 20, 20])
    scr.blit(textExp, [screenX + 20, 62])
    scr.blit(textHp, [screenX + 20, 82])

    if firstHitFlag:
        scr.blit(textInfo, [20, screenY - 30])

    scr.blit(textQ, textQ.get_rect(center=(screenX + 60, 160)))
    scr.blit(textW, textW.get_rect(center=(screenX + 150, 160)))
    scr.blit(textE, textE.get_rect(center=(screenX + 240, 160)))
    scr.blit(textR, textR.get_rect(center=(screenX + 330, 160)))
    
    q = font_size20.render('Q', True, BLACK)
    w = font_size20.render('W', True, BLACK)
    e = font_size20.render('E', True, BLACK)
    r = font_size20.render('R', True, BLACK)

    scr.blit(q, q.get_rect(center=(screenX + 60, 212)))
    scr.blit(w, w.get_rect(center=(screenX + 150, 212)))
    scr.blit(e, e.get_rect(center=(screenX + 240, 212)))
    scr.blit(r, r.get_rect(center=(screenX + 330, 212)))
    #screen update
    pygame.display.update()

#quit
pygame.quit()
