import pygame
from Snake import Snake, edge
from Food import Food
import numpy

initialBody = [(100, 100), (100, 90), (100, 80)]
SnakeOne = Snake(100, 110, 4, initialBody, (100, 70))
foodlist = []
timer = 0


class Arena:

    def __init__(self, xNodes, yNodes):
        self.xNodes = xNodes
        self.yNodes = yNodes
        self.isGameStarted = False

    def movesnake(self, direction):

        SnakeOne.move(direction)


    def mainarena(self, win, direction):

        global foodlist
        randpos = numpy.random.randint(low=1, high=29, size=2) * 10
        if numpy.random.randint(low=0, high=100) < 5:
            newfood = Food(edge + randpos[0], edge + randpos[1])
            newfood.draw(win)
            newfood.init = True
            foodlist.append(newfood)

        self.isGameStarted = True

        SnakeOne.draw(win, direction)

        for food, val in enumerate(foodlist):
            if (SnakeOne.xPos, SnakeOne.yPos) == (foodlist[food].xPos, foodlist[food].yPos):
                foodlist[food].Eaten = True
                SnakeOne.HasEaten = True
                del foodlist[food]

        for a in range(len(SnakeOne.posHistory)):
                if (SnakeOne.xPos, SnakeOne.yPos) == SnakeOne.posHistory[a]:
                    pygame.quit()
                    pass
                    # pygame.quit()


