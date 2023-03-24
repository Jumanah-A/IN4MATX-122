#             R    G    B
LIGHTBLUE = (227, 230, 246)
BLUE = (38, 150, 190)
RED = (255, 100, 100)
BLACK = (0,   0,   0)
BROWN = (85,  65,   0)
PURPLE = (118, 86, 149)
WHITE = (255, 255, 255)
# HIGHLIGHTCOLOR = PURPLE  # color of the selected gem's border

class GUI_Design:
    def __init__(self):
        self.WINDOWWIDTH = 1000  # width of the program's window, in pixels
        self.WINDOWHEIGHT = 600  # height in pixels

        self.GEMIMAGESIZE = 64  # width & height of each space in pixels

        self.BGCOLOR = BLACK  # background color on the screen
        self.GRIDCOLOR = BLUE  # color of the game board
        self.GAMEOVERCOLOR = BLACK  # color of the "Game over" text.
        # background color of the "Game over" text.
        self.GAMEOVERBGCOLOR = LIGHTBLUE
        self.SCORECOLOR = WHITE  # color of the text for the player's score


    # Setters to Make TMGE more dynamic
    def setGemImageSize(self, new_size):
        self.GEMIMAGESIZE = new_size

    def setBGColor(self, new_bg_color):
        self.BGCOLOR = new_bg_color

    def setGridColor(self, new_grid_color):
        self.GRIDCOLOR = new_grid_color

    def setGameOverColor(self, new_game_over):
        self.GAMEOVERCOLOR = new_game_over

    def setGameOverBGColor(self, new_game_over):
        self.GAMEOVERBGCOLOR = new_game_over

    def setScoreColor(self, new_score_color):
        self.SCORECOLOR = new_score_color