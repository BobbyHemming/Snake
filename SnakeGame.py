import pygame
from Arena import Arena
from Button import Button

timer = 0
startButton = Button(110, 50, 100, 30, "dark", "Start Game")
highscoreButton = Button(110, 100, 100, 30, "dark", "High Score")

# TODO: Build a scoring function and initialise it in the menu screen if the USER clicks "High Score" button.

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
                try:
                    if startButton.isOver(mousePos):
                        win.fill((0, 0, 0))
                        main()
                except:
                    print("Error: Game won't start")

        pygame.display.update()


def end_game():
    pass



def redrawwindow(win, direction):

    pygame.draw.rect(win, (0, 0, 255), (0, 0, width, height), 20)
    newArena.mainarena(win, direction)

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
# pygame.display.flip()

menu_screen()


