import random, time, pygame, sys, copy, pygame
from CandyCrush import CandyCrush
from Bejeweled import Bejeweled
from Menu import Menu

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

class GUI:
    def __init__(self):
        self.pygame = pygame
        self.pygame.init()
        self.DISPLAYSURF = self.pygame.display.set_mode((1000, 600))
        self.BOARDRECTS = []

    def main(self):
        # Load the images
        GEMIMAGES = []
        for i in range(1, NUMGEMIMAGES+1):
            gemImage = pygame.image.load('assets/gem%s.png' % i)
            if gemImage.get_size() != (GEMIMAGESIZE, GEMIMAGESIZE):
                gemImage = pygame.transform.smoothscale(gemImage, (GEMIMAGESIZE, GEMIMAGESIZE))
            GEMIMAGES.append(gemImage)

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

    def startCandyCrush1P(self):
        # game = CandyCrush(1)
        # game.start()
        pass

    def startCandyCrush2P(self):
        # game = CandyCrush(2)
        # game.start()
        pass

    def startBejeweled(self):
        # game = Bejeweled(1)
        # game.start()
        pass

    def drawBoard(board):
        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT):
                self.pygame.draw.rect(self.DISPLAYSURF, GRIDCOLOR, self.BOARDRECTS[x][y], 1)
                gemToDraw = board[x][y]
                self.DISPLAYSURF.blit(GEMIMAGES[gemToDraw], self.BOARDRECTS[x][y])

    def drawCondition(num):
        scoreImg = BASICFONT.render(str(num), 1, SCORECOLOR)
        scoreRect = scoreImg.get_rect()
        scoreRect.bottomleft = (10, WINDOWHEIGHT - 6)
        self.DISPLAYSURF.blit(scoreImg, scoreRect)

    def getTileCoords(mouseX, mouseY):
    # See if the mouse click was on the board
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if self.BOARDRECTS[x][y].collidepoint(mouseX, mouseY):
                return {'x': x, 'y': y}
    return None # Click was not on the board.

    def highlightSpace(mouseX, mouseY):
        self.pygame.draw.rect(self.DISPLAYSURF, HIGHLIGHTCOLOR, self.BOARDRECTS[x][y], 4)

if __name__ == '__main__':
    gui = GUI()
    gui.main()
