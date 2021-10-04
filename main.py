##
## EPITECH PROJECT, 2021
## dvd_screensaver
## File description:
## main
##

import pygame
import sys

def fill(surface, color):
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))


pygame.init()

width, height = 1920, 1080
screen = pygame.display.set_mode((width, height))
logo = pygame.image.load('./img/dvd-logo.png').convert_alpha()
pygame.display.set_caption('Screensaver DVD')
clock = pygame.time.Clock()
speed = [10, 7]
rect = logo.get_rect()

colorTab = [(255, 0, 0, 255), (0, 255, 0, 255), (0, 0, 0, 255), (243, 229, 13, 255), (243, 13, 190, 255)]

i = 0
while 1:
    screen.fill((0,0,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if rect.left < 0:
        speed[0] = -speed[0]
        fill(logo, colorTab[i])
        i += 1
    if rect.right > width:
        speed[0] = -speed[0]
        fill(logo, colorTab[i])
        i += 1
    if rect.top < 0:
        speed[1] = -speed[1]
        fill(logo, colorTab[i])
        i += 1
    if rect.bottom > height:
        speed[1] = -speed[1]
        fill(logo, colorTab[i])
        i += 1
    rect.top += speed[1]
    rect.left += speed[0]

    if i == len(colorTab):
        i = 0
    screen.blit(logo, rect)
    clock.tick(60)
    pygame.display.update()