import time
import os
import random
from sense_hat import sense_hat
import pygame
from pygame.locals import *

barre = 3
pygame.init()

sense = SenseHat()
x = 1
y = 3
running = True
ySens = 1
xSens = 1

debutBarre = 0
finBarre = 3
score = 0

r = 250
v = 250
b = 250

fenetre = pygame.display.set_mode((640,480))

sense.clear()

for j in range(0,3):
    sense.set_pixel(0,j,250,250,250)

blanc = [248,248,248]

while running:
    if y == 7:
        ySens = -1
    if y == 0:
        ySens = 1

    if x == 7:
        xSens = -1

    if x == 0:
        sense.clear()
        sense.show_message('Perdu ! score %s' % score, scroll_speed = 0.06)

    if x == 1 and sense.get_pixel(0,y) == blanc:
        xSens = 1
        r = random.randint(0,250)
        v = random.randint(0,250)
        b = random.randint(0,250)
        score += 1
    if temps > 0.3:
        temps = temps - 0.1

    sense.set_pixel(x,y,0,0,0)
    y += ySens
    x += xSens
    sense.set_pixel(x,y,r,v,b)
    time.sleep(temps)


    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_DOWN:
            if finBarre != 8:
                for j in range(debutBarre,finBarre):
                    sense.set_pixel(0,j,0,0,0)
                debutBarre += 1
                finBarre += 1
                for j in range(debutBarre,finBarre):
                    sense.set_pixel(0,j,250,250,250)

        if event.type == KEYDOWN and event.key == K_UP:
            if debutBarre != 0:
                for j in range(debutBarre,finBarre):
                    sense.set_pixel(0,j,0,0,0)
                debutBarre -= 1
                finBarre -= 1
                for j in range(debutBarre,finBarre):
                    sense.set_pixel(0,j,250,250,250)