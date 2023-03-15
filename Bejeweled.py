import HorizontalMatch
import VerticalMatch
from Game import Game
import Timer
import BejeweledTileFactory


class Bejeweled(Game):
    def __init__(self, playerCount):
        matchingLogic = [HorizontalMatch(), VerticalMatch()]
        timer = Timer(180)
        gems = ["red square", "yellow rhombus", "green circle", "blue diamond", "purple triangle", "white ball"]
        super().__init__(playerCount, matchingLogic, BejeweledTileFactory(gems), timer=timer)

    def resetGame(self):
        self.playerTurn = 0
        self.board.createBoard()
        for player in self.players:
            player.resetScore()

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
