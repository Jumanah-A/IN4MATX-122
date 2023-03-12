from IMatch import IMatch

class HorizontalMatch(IMatch):
    def checkMatch(self, board):
        matches = []
        for row in range(len(board)):
            for col in range(len(board[row])):
                for x, y in self.checkForMatch(board, row, col):
                    matches.append([x, y])
                # if len(self.checkForMatch(board, row, col)) > 0:
                #     # Small issue: returns a 3D list; list of a list of coordinates
                #     # might be good to change this later for simplicity
                #     matches.append(self.checkForMatch(board, row, col))
        return matches

    def checkForMatch(self, board, row, col):
        startingTile = board[row][col]
        if startingTile == self.emptyTile:
            return []
        right = col+1
        left = col-1
        matchLocations = []
        matchLocations.append([row,col])

        # check right
        while right < len(board[row]) and board[row][right] == startingTile:
            matchLocations.append([row, right])
            right += 1

        # check left
        while left >= 0 and board[row][left] == startingTile:
            matchLocations.append([row, left])
            left -= 1

        if len(matchLocations) >= self.min_matching_length:
            return matchLocations
        else:
            return []