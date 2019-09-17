import pygame
import numpy
snakewidth = 10

timer = 0


class Food:

    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.timer = pygame.time.Clock()
        self.Eaten = False
        self.init = False

    def draw(self, win):
        global timer
        self.timer.tick()
        timer += self.timer.tick(100)

        randNumber = numpy.random.randint(low=0, high=5, size=3)
        randColour = (50 * randNumber[0], 50 * randNumber[1], 50 * randNumber[2])

        pygame.draw.rect(win, (150, 100, 250), (self.xPos, self.yPos, snakewidth, snakewidth), 0)

        if self.Eaten or timer > 8000:
            pygame.draw.rect(win, (0, 0, 0), (self.xPos-1, self.yPos-1, snakewidth, snakewidth), 0)
            self.Eaten = True

        pass

