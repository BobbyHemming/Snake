import pygame
import numpy as np
from Arena import Arena
from Button import Button
from Snake import Snake
from Highscore import sethighscore
timer = 0
startButton = Button(110, 50, 100, 30, "dark", "Start Game")
highscoreButton = Button(110, 100, 100, 30, "dark", "High Score")
highscoreButton2 = Button(110, 40, 100, 30, "light", "High Score")
gameoverButton = Button(110, 50, 100, 30, "light", "Game Over!")
menuscreenButton = Button(110, 110, 100, 30, "dark", "Main Menu")
menuscreenButton2 = Button(110, 250, 100, 20, "dark", "Main Menu")

<<<<<<< HEAD

# TODO: Update highscore read and write function
# TODO: Build a scoring function and initialise it in the menu screen if the USER clicks "High Score" button.
=======
# TODO: *** DONE *** Game Over Sequence, but could use some tidy up at the end screen.
# TODO: Build a scoring function and initialise it in the menu screen if the USER clicks "High Score" button.


def redrawHSscreen(win):
    win.fill((0, 0, 0))
    menuscreenButton2.draw(win)
    highscoreButton2.draw(win)
    list = np.loadtxt("highscores.txt")
    ts = Button(110, 80, 100, 30, "light", "1. {}".format(int(list[2])))
    ss = Button(110, 110, 100, 30, "light", "2. {}".format(int(list[1])))
    ds = Button(110, 140, 100, 30, "light", "3. {}".format(int(list[0])))

    ts.draw(win)
    ss.draw(win)
    ds.draw(win)
    pygame.display.update()

def highscorescreen():
    running = True
    while running:
        redrawHSscreen(win)
        for event in pygame.event.get():
            mousePos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

            if event.type == pygame.MOUSEMOTION:

                if menuscreenButton2.isOver(mousePos):
                    menuscreenButton2.colour = "light"
                else:
                    menuscreenButton2.colour = "dark"


            if event.type == pygame.MOUSEBUTTONDOWN:
                if menuscreenButton2.isOver(mousePos):
                    menu_screen()

>>>>>>> Dev-highscore

def redrawMenuScreen(win):
    win.fill((0, 0, 0))
    startButton.draw(win)
    highscoreButton.draw(win)


def menu_screen():

    running = True

    while running:

        redrawMenuScreen(win)
        pygame.display.update()

        for event in pygame.event.get():
            mousePos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

            if event.type == pygame.MOUSEMOTION:

                if startButton.isOver(mousePos):
                    startButton.colour = "light"
                else:
                    startButton.colour = "dark"

                if highscoreButton.isOver(mousePos):
                    highscoreButton.colour = "light"
                else:
                    highscoreButton.colour = "dark"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if startButton.isOver(mousePos):
                    win.fill((0, 0, 0))
                    initialBody = [(100, 100), (100, 90), (100, 80)]
                    SnakeOne = Snake(100, 110, 4, initialBody, (100, 70))
                    main(SnakeOne)
                if highscoreButton.isOver(mousePos):
                    win.fill((0, 0, 0))
                    highscorescreen()

        pygame.display.update()


def redrawEndGameScreen(win):
    win.fill((0, 0, 0))
    gameoverButton.draw(win)
    menuscreenButton.draw(win)


def end_game():
    running = True
    global newArena
    newArena = Arena(30, 30)

    while running:
        redrawEndGameScreen(win)
        pygame.display.update()

        for event in pygame.event.get():
            mousePos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

            if event.type == pygame.MOUSEMOTION:

                if menuscreenButton.isOver(mousePos):
                    menuscreenButton.colour = "light"
                else:
                    menuscreenButton.colour = "dark"


            if event.type == pygame.MOUSEBUTTONDOWN:
                try:
                    if menuscreenButton.isOver(mousePos):
                        menu_screen()
                except:
                    print("Error: Game won't start")

    pass


def redrawwindow(win, direction, snake):

    pygame.draw.rect(win, (0, 0, 255), (0, 0, width, height), 20)
    newArena.mainarena(win, direction, snake)
    pygame.display.update()


def main(snake):
    running = True
    clock = pygame.time.Clock()
    direction = (0, 1)
    gamestate = True

    global timer

    while running:
        pygame.init()
        clock.tick()
        redrawwindow(win, direction, snake)
        pygame.time.wait(100)

        gamestate = newArena.eatenself(snake)
        score = newArena.score(snake)
        if not gamestate:
            print("Ended")
            print(score)
            sethighscore(score)
            end_game()
            break

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

        newArena.movesnake(direction, snake)


        timer += clock.tick(100)

width, height = 320, 320

newArena = Arena(30, 30)
win = pygame.display.set_mode((width, height))
# pygame.display.flip()

menu_screen()



