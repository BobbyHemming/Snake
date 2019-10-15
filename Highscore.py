import numpy as np


def sethighscore(score):

    list = np.loadtxt("highscores.txt", delimiter=",")

    for a in range(3):
        if score > list[a]:
            list[a] = int(score)
            list.sort()
            print(list)
            list[2:0]
            np.savetxt("highscores.txt", list)
            break

    return list



