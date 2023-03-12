import HorizontalMatch
import VerticalMatch
import Game
import Timer
import BejeweledFactory


class Bejeweled(Game):
    def __init__(self, playerCount):
        matchingLogic = [HorizontalMatch(), VerticalMatch()]
        timer = Timer(180)
        super().__init__(playerCount, matchingLogic, BejeweledFactory(), timer=timer)
