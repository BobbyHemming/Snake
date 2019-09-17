import pygame
import numpy as np
import time
from Snake import Snake
from Arena import Arena

pygame.font.init()


timer = 0
# This is a comment checking whether source tree is working
# This is a test if this is in "Test" branch of master

def menu_screen(win):

    running = True

    while running:

        font = pygame.font.SysFont("comicsans", 30)
        win.fill((0, 0, 0))

        startgame = font.render("Start Game", 1, (200, 200, 200))
        win.blit(startgame, (width / 2 - startgame.get_width() / 2, 80))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                try:
                    win.fill((0, 0, 0))
                    pygame.time.wait(3000)
                    pygame.display.update()
                    main()
                    break
                except:
                    print("Error: Game won't start")

            #if event.type == pygame.MOUSEMOTION:
            mousepos = pygame.mouse.get_pos()
            if (width / 2 - startgame.get_width() / 2) <= mousepos[0] <= (width / 2 + startgame.get_width() / 2) and 60 <= mousepos[1] <= 100:
                startgamelight = font.render("Start Game", 1, (255, 255, 255))
                win.blit(startgamelight, (width / 2 - startgame.get_width() / 2, 80))

        pygame.display.update()



def redrawwindow(win, direction):

    pygame.draw.rect(win, (0, 0, 255), (0, 0, width, height), 20)
    newArena.mainarena(win, direction)

    # pygame.draw.rect(win, (1, 1, 240), (460, 20, 20, 10), 0)
    # textsurface = myfont.render('{}'.format(int(timer/1000)), False, (0, 240, 0))
    # win.blit(textsurface, (460, 20))

    pygame.display.update()


def main():
    running = True
    clock = pygame.time.Clock()
    direction = (0, 1)
    global timer

    while running:
        pygame.init()
        clock.tick()
        redrawwindow(win, direction)
        pygame.time.wait(100)

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            if event.type == pygame.MOUSEMOTION:
                mousepos = pygame.mouse.get_pos()

            if keys[pygame.K_UP]:
                if direction[1] != 1:
                    direction = (0, -1)
                    break
            elif keys[pygame.K_DOWN]:
                if direction[1] != -1:
                    direction = (0, 1)
                    break
            if keys[pygame.K_LEFT]:
                if direction[0] != 1:
                    direction = (-1, 0)
                    break
            elif keys[pygame.K_RIGHT]:
                if direction[0] != -1:
                    direction = (1, 0)
                    break
        newArena.movesnake(direction)

        timer += clock.tick(100)

width, height = 320, 320
newArena = Arena(30, 30)

win = pygame.display.set_mode((width, height))
pygame.display.flip()

menu_screen(win)


