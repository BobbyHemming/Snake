import numpy as np


def sethighscore(score):

    list = np.loadtxt("highscores.txt")

    for a in len(list):
        if score > list[a]:
            list.append(score)
            list.sort(reverse=True)
            del list[-1]
            np.savetxt("highscores.txt", list)
            break

    return list



