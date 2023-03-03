# IMatch interface
class IMatch:
    def __init__(self, min_matching_length = 3):
        self.min_matching_length = min_matching_length

    def checkMatch(self, board: list) -> list:
        """checks for matches across the whole board"""
        pass