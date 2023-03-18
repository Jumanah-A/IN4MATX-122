from HorizontalMatch import HorizontalMatch
from VerticalMatch import VerticalMatch
from Game import Game
from Timer import Timer
from CandyCrushTileFactory import CandyCrushTileFactory


class CandyCrush(Game):
    def __init__(self, playerCount, gui):
        self.gui = gui
        horizontal = HorizontalMatch()
        vertical = VerticalMatch()
        matchingLogic = [horizontal, vertical]
        candies = ["red bean", "orange oval", "yellow drop",
                   "green square", "blue ball", "purple star"]
        super().__init__(playerCount, matchingLogic,
                         CandyCrushTileFactory(candies), moveCount=40)

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
            self.gui.drawBoard(self.board.grid)
            coordinates, direction = self.controller.getInput()

            if coordinates == (-1, 0):
                running = False

            elif coordinates != (-1, -1):
                coordinates = self.gui.getTileCoords(coordinates[0], coordinates[1])
                swappedCoords = (coordinates[1], coordinates[0])
                if self.board.isValidSwap(coordinates, direction):
                    self.board.swapTile(coordinates, direction)

                    isEmpty = False
                    while (not isEmpty):
                        tiles = set()
                        for matchLogic in self.matchingLogic:
                            tiles.update(matchLogic.checkMatch(self.board.grid))
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
                if self.timer.getTime() <= 0:
                    running = False
            
