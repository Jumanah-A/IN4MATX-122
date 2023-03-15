import Controller
import Board
import Player
import pygame, pygame_menu
from abc import ABC, abstractmethod

FPS = 30 # frames per second to update the screen
WINDOWWIDTH = 1000  # width of the program's window, in pixels
WINDOWHEIGHT = 600 # height in pixels

BOARDWIDTH = 8 # how many columns in the board
BOARDHEIGHT = 8 # how many rows in the board
GEMIMAGESIZE = 64 # width & height of each space in pixels

# NUMGEMIMAGES is the number of gem types. You will need .png image
# files named gem0.png, gem1.png, etc. up to gem(N-1).png.
NUMGEMIMAGES = 7
assert NUMGEMIMAGES >= 5 # game needs at least 5 types of gems to work

# NUMMATCHSOUNDS is the number of different sounds to choose from when
# a match is made. The .wav files are named match0.wav, match1.wav, etc.
NUMMATCHSOUNDS = 6

MOVERATE = 25 # 1 to 100, larger num means faster animations
DEDUCTSPEED = 0.8 # reduces score by 1 point every DEDUCTSPEED seconds.

#             R    G    B
LIGHTBLUE = (227, 230, 246)
BLUE      = (38, 150, 190)
RED       = (255, 100, 100)
BLACK     = (  0,   0,   0)
BROWN     = ( 85,  65,   0)
PURPLE     = (118,86,149)
HIGHLIGHTCOLOR = PURPLE # color of the selected gem's border
BGCOLOR = LIGHTBLUE # background color on the screen
GRIDCOLOR = BLUE # color of the game board
GAMEOVERCOLOR = RED # color of the "Game over" text.
GAMEOVERBGCOLOR = BLACK # background color of the "Game over" text.
SCORECOLOR = BLACK # color of the text for the player's score

# The amount of space to the sides of the board to the edge of the window
# is used several times, so calculate it once here and store in variables.
XMARGIN = int((WINDOWWIDTH - GEMIMAGESIZE * BOARDWIDTH) / 2)
YMARGIN = int((WINDOWHEIGHT - GEMIMAGESIZE * BOARDHEIGHT) / 2)

# constants for direction values
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

EMPTY_SPACE = -1 # an arbitrary, nonpositive value
ROWABOVEBOARD = 'row above board' # an arbitrary, noninteger value


class Game(ABC):
    def __init__(self, playerCount, matchingLogic, tileFactory, timer=None, moveCount=None):
        self.players = [Player() for i in range(playerCount)]
        self.playerTurn = 0
        self.matchingLogic = matchingLogic
        self.board = Board(tileFactory)
        self.timer = timer
        self.controller = Controller()
        self.moveCount = moveCount

    @abstractmethod
    def resetGame(self):
        self.playerTurn = 0
        self.board.createBoard()
        for player in self.players:
            player.resetScore()

    @abstractmethod
    def start(self):
        self.board.createBoard()
        running = True

        while (running):
            coordinates, direction = self.controller.getInput()

            if coordinates == (-1, 0):
                running = False

            elif coordinates != (-1, -1):
                if self.board.isValidSwap(coordinates, direction):
                    self.board.swapTile(coordinates, direction)

                    isEmpty = False
                    while (not isEmpty):
                        tiles = set()
                        for matchLogic in self.matchingLogic:
                            tiles.update(matchLogic.checkMatches(self.board))
                        if not tiles:
                            isEmpty = True
                        else:
                            self.players[self.playerTurn].increaseScore(
                                len(tiles))
                            self.board.updateBoard(tiles)

                if self.moveCount != None:
                    self.moveCount -= 1
                    if self.moveCount <= 0:
                        running = False

            if self.timer != None:
                if self.timer.getTime() <= 0:
                    running = False

if __name__ == '__main__':
    game = Game(1, 2,3)
    game.main()
