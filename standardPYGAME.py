import pygame
import sys
import random 
import time
import math

# pylint: disable=no-member
pygame.init()

# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# screen
# scr = pygame.display.set_mode([screenX, screenY])
scr = pygame.display.set_mode()
scrx, scry = 1920, 1080
pygame.display.set_caption("TEST FILE")

#toggle
run = True

#tick
tick = 60
clock = pygame.time.Clock()

def textout(text, x, y, size, color, center):
    font = pygame.font.SysFont("arial", size)
    textin = font.render(text, True, color)
    if center:
        scr.blit(textin, textin.get_rect(center=(x, y)))
    else:
        scr.blit(textin, (x, y))

while run:
    clock.tick(tick)
    scr.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
    # mpressed_left, mpressed_middle, mpressed_right = pygame.mouse.get_pressed()
    # cursorX, cursorY = pygame.mouse.get_pos()

    pygame.display.flip()
pygame.quit()


# 파이게임 이미지 관련 함수
# import pygame, sys
# from pygame.locals import *

# pygame.init()

# FPS = 30 # frames per second setting
# fpsClock = pygame.time.Clock()

# # set up the window
# DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
# pygame.display.set_caption('Animation')

# WHITE = (255, 255, 255)
# catImg = pygame.image.load('cat.png')
# catx = 10
# caty = 10
# direction = 'right'

# while True: # the main game loop
#     DISPLAYSURF.fill(WHITE)

#     if direction == 'right':
#         catx += 5
#         if catx == 280:
#             direction = 'down'
#     elif direction == 'down':
#         caty += 5
#         if caty == 220:
#             direction = 'left'
#     elif direction == 'left':
#         catx -= 5
#         if catx == 10:
#              direction = 'up'
#     elif direction == 'up':
#         caty -= 5
#         if caty == 10:
#             direction = 'right'

#     DISPLAYSURF.blit(catImg, (catx, caty))

#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()

#     pygame.display.update()
#     #fpsClock.tick(FPS)
