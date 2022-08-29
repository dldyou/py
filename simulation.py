import pygame
import sys
from random import *
import time
from math import *

pygame.init() 

scrx, scry = 1000, 500
scr = pygame.display.set_mode([scrx, scry])
pygame.display.set_caption("simulation")

font = pygame.font.SysFont("arial", 15)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

tick = 60
timemultiple = 1.0
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(tick)
    scr.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if timemultiple < 10:
            timemultiple = round(((timemultiple*10)+1)/10, 1)
    if keys[pygame.K_DOWN]:
        if timemultiple > 1:
            timemultiple = round(((timemultiple*10)-1)/10, 1)
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
    # mpressed_left, mpressed_middle, mpressed_right = pygame.mouse.get_pressed()
    # cursorX, cursorY = pygame.mouse.get_pos()
    
    textTM = font.render("time x " + repr(timemultiple), True, BLACK)
    scr.blit(textTM, [20, 20])
    pygame.display.flip()
pygame.quit()