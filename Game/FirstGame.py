# _*_ coding:utf-8 _*_

import pygame
from sys import exit

pygame.init()

try:
    screen = pygame.display.set_mode((450,800), 0 , 32)
    pygame.display.set_caption("hello, world!")

    backgroud = pygame.image.load('back.jpg').convert()
    plane = pygame.image.load('plane.png').convert_alpha()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.blit(backgroud,(0,0))
        x,y = pygame.mouse.get_pos()

        x -=  plane.get_width()/2
        y -=  plane.get_height()/2

        screen.blit(plane, (x, y))
        pygame.display.update()
except Exception as e:
    print(e)
