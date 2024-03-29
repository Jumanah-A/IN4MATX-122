import pygame
from pygame.locals import *


class Controller(object):
    # def getExitClicked(self):
    #     exitGame = False
    #     for event in pygame.event.get():
    #         if event.type == MOUSEBUTTONDOWN:
    #             exitGame= True
    #     return exitGame

    def getInput(self):
        clicked = False
        coordinates = (0, 0)
        direction = ""
        firstRun = True

        while (clicked or firstRun):
            firstRun = False
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        return (-2,-2), ""

                if event.type == QUIT:
                    return (-1, 0), ""

                if clicked == False and event.type == MOUSEBUTTONDOWN:
                    clicked = True
                    coordinates = (event.pos[0], event.pos[1])

                if clicked == True and event.type == MOUSEBUTTONUP:
                    clicked = False
                    coordinates = (0, 0)

                if clicked == True and event.type == MOUSEMOTION:
                    x_move = coordinates[0] - event.pos[0]
                    y_move = coordinates[1] - event.pos[1]

                    if abs(x_move) >= abs(y_move):
                        if x_move > 0:
                            direction = "left"
                        else:
                            direction = "right"
                    else:
                        if y_move > 0:
                            direction = "up"
                        else:
                            direction = "down"

                if direction != "":
                    return coordinates, direction

        return (-1, -1), ""
