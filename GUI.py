import pygame
from CandyCrush import CandyCrush
from Bejeweled import Bejeweled
from Menu import Menu
from GUI_Design import GUI_Design

# constants for direction values
# UP = 'up'
# DOWN = 'down'
# LEFT = 'left'
# RIGHT = 'right'


class GUI:
    def __init__(self):
        # board width and board height will change upon current game being set
        self.BOARDWIDTH = 5  # how many columns in the board
        self.BOARDHEIGHT = 5  # how many rows in the board
        self.design = GUI_Design()

        # GUI Attributes
        self.pygame = pygame
        self.pygame.init()
        self.currentGame = None
        self.DISPLAYSURF = self.pygame.display.set_mode(
            (self.design.WINDOWWIDTH, self.design.WINDOWHEIGHT))
        self.BOARDRECTS = []
        self.clickContinueTextSurf = None
        self.BASICFONT = pygame.font.Font('freesansbold.ttf', 24)
        self.timer_rect = None

    def main(self):
        pygame.display.set_caption('INF122 FINAL PROJECT')
        # DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        # Load the images

        # The amount of space to the sides of the board to the edge of the window
        # is used several times, so calculate it once here and store in variables.
        XMARGIN = int(
            (self.design.WINDOWWIDTH - self.design.GEMIMAGESIZE * self.BOARDWIDTH) / 2)
        YMARGIN = int(
            (self.design.WINDOWHEIGHT - self.design.GEMIMAGESIZE * self.BOARDHEIGHT) / 2)

        # Create pygame.Rect objects for each board space to
        # do board-coordinate-to-pixel-coordinate conversions.
        for x in range(self.BOARDWIDTH):
            self.BOARDRECTS.append([])
            for y in range(self.BOARDHEIGHT):
                r = pygame.Rect((XMARGIN + (x * self.design.GEMIMAGESIZE),
                                 YMARGIN + (y * self.design.GEMIMAGESIZE),
                                 self.design.GEMIMAGESIZE,
                                 self.design.GEMIMAGESIZE))
                self.BOARDRECTS[x].append(r)

        # DISPLAYSURF = self.pygame.display.set_mode((1000, 600))
        menu = Menu(self)
        menu.mainloop(self.DISPLAYSURF)

    def displayScore(self, turn=-1):
        # initialze score text object
        # font = pygame.font.Font(None, 36)
        # HARD CODED PLAYER FOR NOW
        player_text = ""
        if turn == 0:
            player_text = "Player 1"
        elif turn == 1:
            player_text = "Player 2"

        score_text = self.BASICFONT.render(
            f'Player 1 Score: {self.currentGame.players[0].score}', True, self.design.SCORECOLOR)
        self.DISPLAYSURF.blit(score_text, (10, 10))

        # maybe change this later
        if turn != -1 and len(self.currentGame.players) >= 2:
            score_text2 = self.BASICFONT.render(
                f'Player 2 Score: {self.currentGame.players[1].score}', True, self.design.SCORECOLOR)
            self.DISPLAYSURF.blit(score_text2, (780, 10))
            turn_text = self.BASICFONT.render(
                f'Turn: {player_text}', True, self.design.SCORECOLOR)
            self.DISPLAYSURF.blit(turn_text, (400, 40))

    def displayTimer(self, timer, position=None):
        # cannot have instance variables as default parameters, so this is the work around
        if position is None:
            position = (self.design.WINDOWWIDTH/2, 10)

        timer_text = self.BASICFONT.render(
            f'Time Remaining: {timer.getRemainingTime()}', True, self.design.SCORECOLOR)
        position = (position[0]-timer_text.get_rect().width/2, position[1])
        if self.timer_rect:
            # print("Overwrite rectangle")
            self.DISPLAYSURF.fill(self.design.BGCOLOR, rect=self.timer_rect)
        else:
            # print("No overwrite")
            self.timer_rect = timer_text.get_rect(topleft=position)
        self.DISPLAYSURF.blit(timer_text, position)
        pygame.display.update(self.timer_rect)

    def displayMoveCount(self):
        # initialze score text object
        # font = pygame.font.Font(None, 36)
        # HARD CODED PLAYER FOR NOW
        score_text = self.BASICFONT.render(
            f'Total Moves: {self.currentGame.moveCount}', True, self.design.SCORECOLOR)
        self.DISPLAYSURF.blit(score_text, (400, 10))

    # private helper function
    def setGameAttributes(self, game):
        self.currentGame = game
        self.BOARDHEIGHT = self.currentGame.board.numRows
        self.BOARDWIDTH = self.currentGame.board.numCols

    def drawBoard(self, board, turn=-1):
        self.DISPLAYSURF = self.pygame.display.set_mode(
            (self.design.WINDOWWIDTH, self.design.WINDOWHEIGHT))
        self.DISPLAYSURF.fill(self.design.BGCOLOR)
        for x in range(self.BOARDWIDTH):
            for y in range(self.BOARDHEIGHT):
                self.pygame.draw.rect(
                    self.DISPLAYSURF, self.design.GRIDCOLOR, self.BOARDRECTS[x][y], 1)
                tileToDraw = board[x][y]
                tileColor = tileToDraw.color
                # tileShape = tileToDraw.shape
                if (isinstance(self.currentGame, CandyCrush)):
                    asset = pygame.image.load(
                        'assets/candies/' + tileColor + '.png')
                elif (isinstance(self.currentGame, Bejeweled)):
                    asset = pygame.image.load(
                        'assets/gems/' + tileColor + '.png')
                else:
                    asset = pygame.image.load('assets/' + tileColor + '.png')

                self.DISPLAYSURF.blit(asset, self.BOARDRECTS[x][y])
        self.displayScore(turn)
        if self.currentGame.moveCount is not None:
            self.displayMoveCount()

        pygame.display.update()

        if self.currentGame.timer:
            self.displayTimer(self.currentGame.timer)

    def getTileCoords(self, mouseX, mouseY):
        # See if the mouse click was on the board
        for x in range(self.BOARDWIDTH):
            for y in range(self.BOARDHEIGHT):
                if self.BOARDRECTS[x][y].collidepoint(mouseX, mouseY):
                    return (y, x)
        return None  # Click was not on the board.

    def drawFinalScore(self, score, player=-1):
        if player == -1:
            self.clickContinueTextSurf = self.BASICFONT.render(
                'Final Score: %s! Press space to return to menu' % (
                    score), 1, self.design.GAMEOVERCOLOR,
                self.design.GAMEOVERBGCOLOR)
        elif player != '':
            self.clickContinueTextSurf = self.BASICFONT.render('Winner: %s, Score: %s! Press space to return to menu' % (
                player, score), 1, self.design.GAMEOVERCOLOR, self.design.GAMEOVERBGCOLOR)
        else:
            self.clickContinueTextSurf = self.BASICFONT.render(
                'Tie! Press space to return to menu', 1, self.design.GAMEOVERCOLOR, self.design.GAMEOVERBGCOLOR)
        clickContinueTextRect = self.clickContinueTextSurf.get_rect()
        clickContinueTextRect.center = int(
            self.design.WINDOWWIDTH / 2), int(self.design.WINDOWHEIGHT / 2)

        self.DISPLAYSURF.blit(self.clickContinueTextSurf,
                              clickContinueTextRect)
        self.pygame.display.update()


if __name__ == '__main__':
    gui = GUI()
    gui.main()
