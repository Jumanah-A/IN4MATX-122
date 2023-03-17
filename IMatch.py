# IMatch interface

class IMatch:
    def __init__(self, min_matching_length = 3, no_matching_tiles = list()):
        self.min_matching_length = min_matching_length
        self.no_matching_tiles = no_matching_tiles

    def checkMatch(self, board: list) -> list:
        """checks for matches across the whole board"""
        pass
