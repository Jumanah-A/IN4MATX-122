from IMatch import IMatch

class AdjacentGroupMatch(IMatch):
    def checkMatch(self, board):
        matches = []
        for row in range(len(board)):
            for col in range(len(board[row])):
                for x, y in self.checkForMatch(board, row, col):
                    matches.append((x, y))
        return matches

    def checkForMatch(self, board, row, col):
        def checkForMatchesH(board, row, col, matchesSet, sTile):
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]):
                return matchesSet
            else:
                if board[row][col] == sTile and (row, col) not in matchesSet:
                    matchesSet.add((row, col))
                    # check left
                    checkForMatchesH(board, row, col-1, matchesSet, sTile)
                    # check right
                    checkForMatchesH(board, row, col+1, matchesSet, sTile)
                    # check top
                    checkForMatchesH(board, row-1, col, matchesSet, sTile)
                    # check bottom
                    checkForMatchesH(board, row+1, col, matchesSet, sTile)

        matches = set()
        startingTile = board[row][col]
        if startingTile == self.emptyTile:
            return set()

        checkForMatchesH(board, row, col, matches, startingTile)

        if len(matches) >= self.min_matching_length:
            return matches
        else:
            return set()

if __name__ == "__main__":
    print("matching tests")
    grid = [[1, 1, 3, 4],
            [1, 1, 2, 4],
            [3, 1, 4, 4],
            [1, 1, 1, 1]]
    matches = [AdjacentGroupMatch()]
    coordinates = []
    for row in grid:
        print(row)
    print("-"*20)
    for match in matches:
        for x, y in match.checkMatch(grid):
            coordinates.append([x, y])
    for x, y in coordinates:
        grid[x][y] = 9
    for row in grid:
        print(row)