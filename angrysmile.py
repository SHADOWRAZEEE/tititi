import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))


rect(screen, (217, 217, 217), (0, 0, 500, 500))

def angrysmile():

    circle(screen, (255, 255, 0), (250, 250), 100)
    circle(screen, (0, 0, 0), (250, 250), 100, 1)


    circle(screen, (255, 0, 0), (200, 235), 25)
    circle(screen, (0, 0, 0), (200, 235), 25, 1)
    circle(screen, (0, 0, 0), (200, 235), 10)

    polygon(screen, (0, 0, 0), [(230, 230), (235, 223), (152, 180), (147, 187)])
    aalines(screen, (0, 0, 0), True, [(230, 230), (235, 223), (152, 180), (147, 187)], 1000)

    circle(screen, (255, 0, 0), (300, 235), 15)
    circle(screen, (0, 0, 0), (300, 235), 15, 1)
    circle(screen, (0, 0, 0), (300, 235), 8)

    polygon(screen, (0, 0, 0), [(280, 230), (275, 223), (347, 190), (350, 197)])
    aalines(screen, (0, 0, 0), True, [(280, 230), (275, 223), (347, 190), (350, 197)], 1000)


    polygon(screen, (0, 0, 0), [(200, 310), (200, 290), (300, 290), (300, 310)])


angrysmile()

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()