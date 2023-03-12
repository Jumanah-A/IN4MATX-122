import HorizontalMatch
import VerticalMatch
import Game
import Timer
import CandyCrushFactory


class CandyCrush(Game):
    def __init__(self, playerCount):
        matchingLogic = [HorizontalMatch(), VerticalMatch()]
        super().__init__(playerCount, matchingLogic, CandyCrushFactory(), moveCount=40)
