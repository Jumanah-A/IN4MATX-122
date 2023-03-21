from HorizontalMatch import HorizontalMatch
from VerticalMatch import VerticalMatch
from Game import Game
from Timer import Timer
from BejeweledTileFactory import BejeweledTileFactory


class Bejeweled(Game):
    def __init__(self,gui):
        self.gui = gui
        horizontal = HorizontalMatch()
        vertical = VerticalMatch()
        matchingLogic = [horizontal, vertical]
        timer = Timer(180)
        playerCount=1
        gems = ["red square", "yellow rhombus", "green circle", "blue diamond", "purple triangle", "white ball"]
        super().__init__(playerCount, matchingLogic, BejeweledTileFactory(gems), timer=timer)

    def resetGame(self):
        self.playerTurn = 0
        self.board.createBoard()
        for player in self.players:
            player.resetScore()

    def start(self):
        self.board.createBoard()
        self.gui.drawBoard(self.board.grid)
        running = True

        while (running):
            coordinates, direction = self.controller.getInput()

            if coordinates == (-1, 0):
                running = False

            elif coordinates != (-1, -1):
                coordinates = self.gui.getTileCoords(
                    coordinates[0], coordinates[1])
                print(coordinates, direction)

                if self.board.isValidSwap(coordinates, direction):
                    self.board.swapTile(coordinates, direction)
                    self.gui.drawBoard(self.board.grid)

                    isEmpty = False
                    while (not isEmpty):
                        tiles = set()
                        for matchLogic in self.matchingLogic:
                            tiles.update(matchLogic.checkMatches(self.board.grid))
                        if not tiles:
                            isEmpty = True
                        else:
                            self.players[self.playerTurn].increaseScore(
                                len(tiles))
                            self.board.updateBoard(tiles, self.gui)

                if self.moveCount != None:
                    self.moveCount -= 1
                    if self.moveCount <= 0:
                        running = False

            if self.timer != None:
                if self.timer.getRemainingTime() <= 0:
                    running = False
