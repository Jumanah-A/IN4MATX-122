# IMatch interface

class IMatch:
    def __init__(self, min_matching_length = 3, emptyTile = 0):
        self.min_matching_length = min_matching_length
        self.emptyTile = emptyTile

    def checkMatch(self, board: list) -> list:
        """checks for matches across the whole board"""
        pass
