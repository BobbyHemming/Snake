import pygame
from Snake import Snake, edge
from Food import Food
import numpy

foodlist = []
timer = 0


class Arena:

    def __init__(self, xNodes, yNodes):
        self.xNodes = xNodes
        self.yNodes = yNodes
        self.isGameStarted = False

    def movesnake(self, direction, snake):

        snake.move(direction)


    def mainarena(self, win, direction, snake):

        global foodlist
        randpos = numpy.random.randint(low=1, high=29, size=2) * 10
        if numpy.random.randint(low=0, high=100) < 5:
            newfood = Food(edge + randpos[0], edge + randpos[1])
            newfood.draw(win)
            newfood.init = True
            foodlist.append(newfood)

        self.isGameStarted = True

        snake.draw(win, direction)

        for food, val in enumerate(foodlist):
            if (snake.xPos, snake.yPos) == (foodlist[food].xPos, foodlist[food].yPos):
                foodlist[food].Eaten = True
                snake.HasEaten = True
                del foodlist[food]


    def eatenself(self, snake):

        for a in range(len(snake.posHistory)):
                if (snake.xPos, snake.yPos) == snake.posHistory[a]:
                    print("End")
                    return False

        return True


    def score(self, snake):

        score = snake.length*10

        return score