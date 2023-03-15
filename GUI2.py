import random, time, pygame, sys, copy, pygame, pygame_menu
import CandyCrush, Bejeweled

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
        self.surface = self.pygame.display.set_mode((1000, 600))

    def main(self):
        menu = Menu(self)
        menu.mainloop(self.surface)

    def startCandyCrush1P(self):
        game = CandyCrush(1)
        # game.start()
        pass

    def startCandyCrush2P(self):
        game = CandyCrush(2)
        # game.start()
        pass

    def startBejeweled(self):
        game = Bejeweled()
        pass

    def getTileCoords(mouseX,mouseY):
        pass

    def drawBoard(board):
        pass

    def drawCondition(num):
        pass



class Menu: 
    def __init__(self, GUI):
        my_theme = pygame_menu.themes.THEME_BLUE.copy()
        my_theme.title_font = pygame_menu.font.FONT_FRANCHISE
        my_theme.widget_font = pygame_menu.font.FONT_FRANCHISE
        self.menu = pygame_menu.Menu('INF122 FINAL PROJECT', 1000,600, theme=my_theme)

        self.menu.add.button('Play Candy Crush 1P', GUI.startCandyCrush1P)
        self.menu.add.button('Play Candy Crush 2P', GUI.startCandyCrush2P)
        self.menu.add.button('Play Bejeweled', GUI.startBejeweled)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)

    def mainloop(self, surface):
        self.menu.mainloop(surface)

if __name__ == '__main__':
    gui = GUI()
    gui.main()
