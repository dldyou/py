import pygame
import sys
import random 
import time
import math

# pylint: disable=no-member
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
scrx, scry = 500, 600
scr = pygame.display.set_mode([scrx, scry])
# scr = pygame.display.set_mode()
pygame.display.set_caption("TEST FILE")

#toggle
run = True
paused = False

#tick
tick = 100
clock = pygame.time.Clock()

def textout(text, x, y, size, color, center):
    font = pygame.font.SysFont("arial", size)
    textin = font.render(text, True, color)
    if center:
        scr.blit(textin, textin.get_rect(center=(x, y)))
    else:
        scr.blit(textin, (x, y))

class ball():
    live = True
    score = 0
    cooltimef = 25
    cooltime = cooltimef
    size = 20
    x, y = scrx / 2, scry / 2
    vxf, vyf = 3, 0
    vx, vy = vxf, vyf

    def move(self): 
        if self.cooltime != 0:
            self.cooltime -= 1
        self.x += self.vx
        self.y += self.vy

        if self.x - self.size <= 0 or self.x + self.size >= scrx:
            self.vx = round(-self.vx)
            self.score += 1
        self.vy += 0.3

        if self.y - self.size <= 0 or self.y + self.size >= scry:
            self.live = False
    def jump(self):
        if self.cooltime == 0:
            self.vy = -8
            self.cooltime = self.cooltimef
    def standard(self):
        self.x, self.y = scrx / 2, scry / 2
        self.vx, self.vy = self.vxf, self.vyf
        self.score = 0
        self.live = True
        self.cooltime = self.cooltimef
b1 = ball()
b2 = ball()

b1.vx *= -1
b1.x -= b1.size
b2.x += b2.size
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
    if b1.live and b2.live:
        b1.move()
        b2.move()
        print(b1.live, b2.live)
        if keys[pygame.K_KP_ENTER]:
            b1.jump()
        if keys[pygame.K_LCTRL]:
            b2.jump()
        pygame.draw.circle(scr, BLACK, (b1.x, b1.y), b1.size, 0)
        pygame.draw.circle(scr, RED, (b2.x, b2.y), b2.size, 0)
        textout(repr(b2.score), scrx / 3, 30, 50, RED, 1)
        textout(repr(b1.score), scrx / 3 * 2, 30, 50, BLACK, 1)
    else:
        text = "status"
        if not b1.live and not b2.live:
            text = "DRAW"
        elif b1.live:
            text = "BLACK WIN"
        elif b2.live:
            text = "RED WIN"
        textout(text, scrx / 2, scry / 2, 100, BLACK, 1)
        if keys[pygame.K_SPACE]:
            b1.standard()
            b2.standard()
            b1.vx *= -1
            b1.x -= b1.size
            b2.x += b2.size
    pygame.display.flip()
pygame.quit()