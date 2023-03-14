import HorizontalMatch
import VerticalMatch
import Game
import Timer
import BejeweledTileFactory


class Bejeweled(Game):
    def __init__(self, playerCount):
        matchingLogic = [HorizontalMatch(), VerticalMatch()]
        timer = Timer(180)
        gems = ["red square", "yellow rhombus", "green circle", "blue diamond", "purple triangle", "white ball"]
        super().__init__(playerCount, matchingLogic, BejeweledTileFactory(gems), timer=timer)
