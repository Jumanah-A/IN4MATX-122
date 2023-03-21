import random
import time
import sys
import copy
import pygame
from CandyCrush import CandyCrush
from Bejeweled import Bejeweled
from Menu import Menu

FPS = 30  # frames per second to update the screen
WINDOWWIDTH = 1000  # width of the program's window, in pixels
WINDOWHEIGHT = 600  # height in pixels

BOARDWIDTH = 5  # how many columns in the board
BOARDHEIGHT = 5  # how many rows in the board
GEMIMAGESIZE = 64  # width & height of each space in pixels

# NUMGEMIMAGES is the number of gem types. You will need .png image
# files named gem0.png, gem1.png, etc. up to gem(N-1).png.
NUMGEMIMAGES = 7
assert NUMGEMIMAGES >= 5  # game needs at least 5 types of gems to work

# NUMMATCHSOUNDS is the number of different sounds to choose from when
# a match is made. The .wav files are named match0.wav, match1.wav, etc.
NUMMATCHSOUNDS = 6

MOVERATE = 25  # 1 to 100, larger num means faster animations
DEDUCTSPEED = 0.8  # reduces score by 1 point every DEDUCTSPEED seconds.

#             R    G    B
LIGHTBLUE = (227, 230, 246)
BLUE = (38, 150, 190)
RED = (255, 100, 100)
BLACK = (0,   0,   0)
BROWN = (85,  65,   0)
PURPLE = (118, 86, 149)
HIGHLIGHTCOLOR = PURPLE  # color of the selected gem's border
BGCOLOR = LIGHTBLUE  # background color on the screen
GRIDCOLOR = BLUE  # color of the game board
GAMEOVERCOLOR = BLACK  # color of the "Game over" text.
GAMEOVERBGCOLOR = LIGHTBLUE  # background color of the "Game over" text.
SCORECOLOR = BLACK  # color of the text for the player's score

# The amount of space to the sides of the board to the edge of the window
# is used several times, so calculate it once here and store in variables.
XMARGIN = int((WINDOWWIDTH - GEMIMAGESIZE * BOARDWIDTH) / 2)
YMARGIN = int((WINDOWHEIGHT - GEMIMAGESIZE * BOARDHEIGHT) / 2)

# constants for direction values
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

EMPTY_SPACE = -1  # an arbitrary, nonpositive value
ROWABOVEBOARD = 'row above board'  # an arbitrary, noninteger value


class GUI:
    def __init__(self):
        self.pygame = pygame
        self.pygame.init()
        self.currentGame = None
        self.DISPLAYSURF = self.pygame.display.set_mode((1000, 600))
        self.BOARDRECTS = []
        self.ClickContinueTextSurf= None
        self.BASICFONT = pygame.font.Font('freesansbold.ttf', 24)

    def main(self):
        pygame.display.set_caption('INF122 FINAL PROJECT')
        DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        # Load the images

        # Create pygame.Rect objects for each board space to
        # do board-coordinate-to-pixel-coordinate conversions.
        for x in range(BOARDWIDTH):
            self.BOARDRECTS.append([])
            for y in range(BOARDHEIGHT):
                r = pygame.Rect((XMARGIN + (x * GEMIMAGESIZE),
                                 YMARGIN + (y * GEMIMAGESIZE),
                                 GEMIMAGESIZE,
                                 GEMIMAGESIZE))
                self.BOARDRECTS[x].append(r)

        # DISPLAYSURF = self.pygame.display.set_mode((1000, 600))
        menu = Menu(self)
        menu.mainloop(self.DISPLAYSURF)

    def displayScore(self, turn=-1):
        # initialze score text object
        # font = pygame.font.Font(None, 36)
        # HARD CODED PLAYER FOR NOW
        player_text = ""
        if turn==0:
            player_text = "Player1"
        elif turn == 1:
            player_text = "Player2"

        score_text = self.BASICFONT.render(f'Player1 Score: {self.currentGame.players[0].score}', True, (255, 255, 255))
        self.DISPLAYSURF.blit(score_text, (10, 10))

        # maybe change this later
        if turn != -1 and len(self.currentGame.players) >= 2:
            score_text2 = self.BASICFONT.render(f'Player2 Score: {self.currentGame.players[1].score}', True, (255, 255, 255))
            self.DISPLAYSURF.blit(score_text2, (800, 10))
            turn_text = self.BASICFONT.render(f'Turn: {player_text}', True, (255, 255, 255))
            self.DISPLAYSURF.blit(turn_text, (400, 40))

    def displayTimer(self, timer):
        timer_text = self.BASICFONT.render(f'Time Remaining: {timer.getRemainingTime()}', True, (255, 255, 255))
        position = (400, 50)
        if timer.rect is not None:
            print("Overwrite rectangle")
            self.DISPLAYSURF.fill((0, 0, 0), rect=timer.rect)
        else:
            print("No overwrite")
            timer.rect = timer_text.get_rect(topleft=position)
        self.DISPLAYSURF.blit(timer_text, position)
        pygame.display.update(timer.rect)

    def displayMoveCount(self):
        # initialze score text object
        # font = pygame.font.Font(None, 36)
        # HARD CODED PLAYER FOR NOW
        score_text = self.BASICFONT.render(f'Total Moves: {self.currentGame.moveCount}', True, (255, 255, 255))
        self.DISPLAYSURF.blit(score_text, (400, 10))


    def startCandyCrush1P(self):
        # self.DISPLAYSURF = self.pygame.display.set_mode((1000, 600))
        game = CandyCrush(1, self)
        self.currentGame = game
        game.start()

    def startCandyCrush2P(self):
        game = CandyCrush(2, self)
        self.currentGame = game
        game.start()

    def startBejeweled(self):
        # FIX LATER
        # self.DISPLAYSURF = self.pygame.display.set_mode((1000, 600))
        game = Bejeweled(self)
        self.currentGame = game
        game.start()

    def drawBoard(self, board, turn=-1):
        self.DISPLAYSURF = self.pygame.display.set_mode((1000, 600))

        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT):
                self.pygame.draw.rect(
                    self.DISPLAYSURF, GRIDCOLOR, self.BOARDRECTS[x][y], 1)
                tileToDraw = board[x][y]
                tileColor = tileToDraw.color
                tileShape = tileToDraw.shape
                asset = pygame.image.load('assets/' + tileColor + '.png')
                self.DISPLAYSURF.blit(asset, self.BOARDRECTS[x][y])
        self.displayScore(turn)
        self.displayMoveCount()
        self.displayTimer(self.currentGame.timer)
        pygame.display.update()

    # def drawCondition(self, num):
    #     scoreImg = BASICFONT.render(str(num), 1, SCORECOLOR)
    #     scoreRect = scoreImg.get_rect()
    #     scoreRect.bottomleft = (10, WINDOWHEIGHT - 6)
    #     self.DISPLAYSURF.blit(scoreImg, scoreRect)

    def getTileCoords(self, mouseX, mouseY):
        # See if the mouse click was on the board
        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT):
                if self.BOARDRECTS[x][y].collidepoint(mouseX, mouseY):
                    return (y, x)
        return None  # Click was not on the board.

    # def highlightSpace(self, mouseX, mouseY):
    #     self.pygame.draw.rect(
    #         self.DISPLAYSURF, HIGHLIGHTCOLOR, self.BOARDRECTS[x][y], 4)

    def drawFinalScore(self, score, player=-1):
        if player==-1:
            self.clickContinueTextSurf = self.BASICFONT.render('Final Score: %s! Press space to return to menu' % (score), 1, GAMEOVERCOLOR, GAMEOVERBGCOLOR)
        elif player != '':
            self.clickContinueTextSurf = self.BASICFONT.render('Winner: %s, Score: %s! Press space to return to menu' % (player, score), 1, GAMEOVERCOLOR, GAMEOVERBGCOLOR)
        else: 
            self.clickContinueTextSurf = self.BASICFONT.render('Tie! Press space to return to menu', 1, GAMEOVERCOLOR, GAMEOVERBGCOLOR)
        clickContinueTextRect = self.clickContinueTextSurf.get_rect()
        clickContinueTextRect.center = int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2)

        self.DISPLAYSURF.blit(self.clickContinueTextSurf, clickContinueTextRect)
        self.pygame.display.update()



if __name__ == '__main__':
    gui = GUI()
    gui.main()
