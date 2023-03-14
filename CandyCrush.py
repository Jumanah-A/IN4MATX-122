import HorizontalMatch
import VerticalMatch
import Game
import Timer
import CandyCrushTileFactory


class CandyCrush(Game):
    def __init__(self, playerCount):
        matchingLogic = [HorizontalMatch(), VerticalMatch()]
        candies = ["red bean", "orange oval", "yellow drop", "green square", "blue ball", "purple star"]
        super().__init__(playerCount, matchingLogic, CandyCrushTileFactory(candies), moveCount=40)
