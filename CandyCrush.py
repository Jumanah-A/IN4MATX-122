from HorizontalMatch import HorizontalMatch
from VerticalMatch import VerticalMatch
from Game import Game
from Timer import Timer
from CandyCrushTileFactory import CandyCrushTileFactory
import time

class CandyCrush(Game):
    def __init__(self, playerCount, gui):
        self.gui = gui
        horizontal = HorizontalMatch()
        vertical = VerticalMatch()
        matchingLogic = [horizontal, vertical]
        candies = ["red bean", "orange oval", "yellow drop",
                   "green square", "blue ball", "purple star"]
        super().__init__(playerCount, matchingLogic,
                         CandyCrushTileFactory(candies), moveCount=4,
                         timer = Timer(self.gui))

    def resetGame(self):
        self.playerTurn = 0
        self.board.createBoard()
        for player in self.players:
            player.resetScore()
            # delete this later
            self.timer.resetTimer()

    def start(self):
        self.board.createBoard()
        if self.timer:
            self.timer.startTimer()
        if len(self.players) > 1:
            self.gui.drawBoard(self.board.grid, self.playerTurn)
        else:
            self.gui.drawBoard(self.board.grid)
        running = True


        while (running):
            coordinates, direction = self.controller.getInput()
            # stop the game
            if coordinates == (-1, 0) or coordinates == (-2, -2):
                running = False
                self.timer.resetTimer()

            elif coordinates != (-1, -1):
                coordinates = self.gui.getTileCoords(
                    coordinates[0], coordinates[1])
                print(coordinates, direction)

                if self.board.isValidSwap(coordinates, direction):
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
                self.board.updateBoard(tiles, self.gui, self.playerTurn)

            if self.moveCount <= 0:
                winner_score = 0
                winner = ''
                # if two players
                if len(self.players) > 1:
                    if self.players[0].getScore() > self.players[1].getScore():
                        # Player 1 Wins
                        winner_score = self.players[0].getScore()
                        winner = 'Player1'
                    elif self.players[0].getScore() < self.players[1].getScore():
                        # Player 2 Wins
                        winner_score = self.players[1].getScore()
                        winner = 'Player2'
                    else:
                        # Draw
                        winner_score = self.players[0].getScore()
                        winner = ''
                else:
                    # if only 1 player
                    winner_score = self.players[0].getScore()
                    winner = -1
                self.gui.drawFinalScore(winner_score, winner)



            # Remove this from Candy Crush and put it into Bejeweled once Candy Crush is finished
            if self.timer != None:
                if self.timer.getRemainingTime() <= 0:
                    #running = False
                    winner_score = self.players[0].getScore()
                    winner = -1
                    self.gui.drawFinalScore(winner_score, winner)

