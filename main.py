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
def bouquet(x,y):
    polygon(screen, (255, 204, 0), [[75+x, 450+y], [20+x, 410+y], [70+x, 380+y]])
    aalines(screen, (255, 204, 0), True, [[75+x, 450+y], [20+x, 410+y], [70+x, 380+y]])
    circle(screen, (85, 0, 0), (27+x, 395+y), 16)
    circle(screen, (255, 0, 0), (54+x, 380+y), 16)
    circle(screen, (255, 255, 255), (35+x, 370+y), 16)

def woman():
    polygon(screen, (255, 85, 221), [[450, 270], [360, 540], [540, 540]])
    aalines(screen, (255, 85, 221), True, [[450, 270], [360, 540], [540, 540]])
    circle(screen, (244, 227, 215), (450, 270), 50)
    #руки и ноги
    line(screen, (0, 0, 0), (430, 330), (340, 450), 1)
    line(screen, (0, 0, 0), (470, 330), (530, 370), 1)
    line(screen, (0, 0, 0), (530, 370), (600, 330), 1)
    line(screen, (0, 0, 0), (420, 540), (420, 660), 1)
    line(screen, (0, 0, 0), (480, 540), (480, 660), 1)
    line(screen, (0, 0, 0), (420, 660), (390, 661), 1)
    line(screen, (0, 0, 0), (480, 660), (510, 661), 1)
def ball():
    line(screen, (0, 0, 0), (595, 350), (620, 240), 1)
    polygon(screen, (255, 0, 0), [[620, 240], [600, 180], [650, 190]])
    aalines(screen, (255, 0, 0), True, [[620, 240], [600, 180], [650, 190]])
    circle(screen, (255, 0, 0), (615, 175), 15)
    circle(screen, (255, 0, 0), (640, 180), 15)


men()
bouquet(0,0)
woman()
ball()


pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()