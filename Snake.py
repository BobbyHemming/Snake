import numpy
import pygame

snakesize = 10

width = 310
edge = 10

# End of Test 2

class Snake:

    def __init__(self, xPos, yPos, length, posHistory, lastPos):

        self.xPos = xPos
        self.yPos = yPos
        self.length = length
        self.posHistory = posHistory
        self.HasEaten = False
        self.lastPos = lastPos

    def move(self, direction):

        self.lastPos = self.posHistory[-1]

        if not self.HasEaten:
            del self.posHistory[-1]
        else:
            self.length += 1
            self.HasEaten = False

        self.posHistory.insert(0, (self.xPos, self.yPos))

        if edge < self.yPos < width - edge:
            self.yPos = self.yPos + direction[1]*snakesize
        elif self.yPos == edge:
            self.yPos = width - edge - 10
        elif self.yPos == width - edge:
            self.yPos = edge + 10

        if edge < self.xPos < width - edge - 5:
            self.xPos = self.xPos + direction[0]*snakesize
        elif self.xPos == edge:
            self.xPos = width - edge - 10
        elif self.xPos == width - edge:
            self.xPos = edge + 10

    def draw(self, win, direction):

        snakeColour = (0, 200, 0)
        patternColour = (0, 250, 0)

        pygame.draw.rect(win, snakeColour, (self.xPos+1, self.yPos+1, snakesize-2, snakesize-2), 0)
        if direction[0] == -1:
            pygame.draw.rect(win, patternColour, (self.xPos+1, self.yPos+4, 3, 1), 0)
            pygame.draw.rect(win, patternColour, (self.xPos+1, self.yPos+6, 3, 1), 0)
        elif direction[0] == 1:
            pygame.draw.rect(win, patternColour, (self.xPos+6, self.yPos+4, 1, 3), 0)
            pygame.draw.rect(win, patternColour, (self.xPos+6, self.yPos+6, 1, 3), 0)
        elif direction[1] == -1:
            pygame.draw.rect(win, patternColour, (self.xPos+4, self.yPos+1, 1, 3), 0)
            pygame.draw.rect(win, patternColour, (self.xPos+6, self.yPos+1, 1, 3), 0)
        elif direction[1] == 1:
            pygame.draw.rect(win, patternColour, (self.xPos+4, self.yPos+6, 1, 3), 0)
            pygame.draw.rect(win, patternColour, (self.xPos+6, self.yPos+6, 1, 3), 0)

        for n in range(self.length-1):
            pygame.draw.rect(win, snakeColour, (self.posHistory[n][0]+1, self.posHistory[n][1]+1, snakesize-2, snakesize-2), 0)
            pygame.draw.rect(win, (0, 250, 0), (self.posHistory[n][0]+2, self.posHistory[n][1]+2, snakesize-4, snakesize-4), 1)

        pygame.draw.rect(win, (0, 0, 0), (self.lastPos[0], self.lastPos[1], snakesize, snakesize), 0)







