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
        playerCount=1
        super().__init__(playerCount, matchingLogic, BejeweledTileFactory(), timer=Timer(self.gui))

    def start(self):
        self.board.createBoard()
        if self.timer:
            self.timer.startTimer()
        if len(self.players) > 1:
            self.gui.drawBoard(self.board.grid, self.playerTurn)
        else:
            self.gui.drawBoard(self.board.grid)
        running = True
        gameFinished = False

        while (running):
            coordinates, direction = self.controller.getInput()
            if coordinates == (-1, 0) or coordinates == (-2, -2):
                running = False
                self.timer.resetTimer()

            elif not gameFinished and coordinates != (-1, -1):
                coordinates = self.gui.getTileCoords(
                    coordinates[0], coordinates[1])
                print(coordinates, direction)

                if coordinates is not None and self.board.isValidSwap(coordinates, direction):
                    self.board.swapTile(coordinates, direction)
                    if self.moveCount != None:
                         self.moveCount -= 1
                         self.gui.drawBoard(self.board.grid, self.playerTurn)
                    else: 
                         self.gui.drawBoard(self.board.grid)

                    isEmpty = False
                    while (not isEmpty):
                        tiles = set()
                        for matchLogic in self.matchingLogic:
                            tiles.update(
                                matchLogic.checkMatch(self.board.grid))
                        if not tiles:
                            isEmpty = True
                        else:
                            self.players[self.playerTurn].increaseScore(
                                len(tiles))
                            self.board.updateBoard(tiles, self.gui, self.playerTurn)

                    if len(self.players) > 1:
                        if self.playerTurn == 1:
                            self.playerTurn = 0
                        else:
                            self.playerTurn = 1

                    # Updates player turn
                    self.board.updateBoard(set(), self.gui, self.playerTurn)

            if self.timer != None:
                if self.timer.getRemainingTime() <= 0:
                    winner_score = self.players[0].getScore()
                    winner = -1
                    self.gui.drawFinalScore(winner_score, winner)
                    gameFinished = True

