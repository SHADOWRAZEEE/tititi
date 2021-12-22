import pygame
from pygame.draw import *
from pygame.transform import *

pygame.init()

FPS = 30
width, height = int(input()), int(input())

screen = pygame.display.set_mode((width, height))
#ФОН
rect(screen, (170, 238, 255), (0, 0, width, height))
rect(screen, (55, 200, 113), (0, height//2, width, height))


def men():
    #мужчина
    surf = pygame.Surface((700, 800), pygame.SRCALPHA) #тело
    ellipse(surf, (167, 147, 172), (100, 195, 120, 230))
    surf = rotate(surf, 0)
    screen.blit(surf, (50, 100))
    #голова
    circle(screen, (244, 227, 215), (210, 260), 50)
    #руки и ноги
    line(screen, (0, 0, 0), (175, 320), (70, 450), 1)
    line(screen, (0, 0, 0), (245, 320), (340, 450), 1)
    line(screen, (0, 0, 0), (190, 515), (140, 660), 1)
    line(screen, (0, 0, 0), (235, 510), (265, 660), 1)
    line(screen, (0, 0, 0), (140, 660), (110, 662), 1)
    line(screen, (0, 0, 0), (265, 660), (295, 662), 1)
def bouquet(x,y,r):
    polygon(screen, (255, 204, 0), [[75+x, 450+y], [20+x, 410+y], [70+x, 380+y]])
    aalines(screen, (255, 204, 0), True, [[75+x, 450+y], [20+x, 410+y], [70+x, 380+y]])
    circle(screen, (85, 0, 0), (27+x, 395+y), r*16)
    circle(screen, (255, 0, 0), (54+x, 380+y), r*16)
    circle(screen, (255, 255, 255), (35+x, 370+y), r*16)

def woman(x,y):
    polygon(screen, (255, 85, 221), [[450+x, 270+y], [360+x, 540+y], [540+x, 540+y]])
    aalines(screen, (255, 85, 221), True, [[450+x, 270+y], [360+x, 540+y], [540+x, 540+y]])
    circle(screen, (244, 227, 215), (450+x, 270+y), 50)
    #руки и ноги
    line(screen, (0, 0, 0), (430+x, 330+y), (340+x, 450+y), 1)
    line(screen, (0, 0, 0), (470+x, 330+y), (530+x, 370+y), 1)
    line(screen, (0, 0, 0), (530+x, 370+y), (600+x, 330+y), 1)
    line(screen, (0, 0, 0), (420+x, 540+y), (420+x, 660+y), 1)
    line(screen, (0, 0, 0), (480+x, 540+y), (480+x, 660+y), 1)
    line(screen, (0, 0, 0), (420+x, 660+y), (390+x, 661+y), 1)
    line(screen, (0, 0, 0), (480+x, 660+y), (510+x, 661+y), 1)
def ball(x,y,u):
    surf = pygame.Surface((1500, 1000), pygame.SRCALPHA)
    line(surf, (0, 0, 0), (595-x, 350+y), (620-x, 240+y), 1)
    surf = rotate(surf,u)
    screen.blit(surf, (0, 0))
    polygon(screen, (255, 0, 0), [[620-x, 240+y], [600-x, 180+y], [650-x, 190+y]])
    aalines(screen, (255, 0, 0), True, [[620-x, 240+y], [600-x, 180+y], [650-x, 190+y]])
    circle(screen, (255, 0, 0), (615-x, 175+y), 15)
    circle(screen, (255, 0, 0), (640-x, 180+y), 15)


men()
bouquet(0,0,1)
woman(0,0)
ball(0,0,0)
woman(400,0)



pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()