from IMatch import IMatch

class VerticalMatch(IMatch):
    def checkMatch(self, board):
        matches = []
        for row in range(len(board)):
            for col in range(len(board[row])):
                for x, y in self.checkForMatch(board, row, col):
                    matches.append((x, y))
                # if len(self.checkForMatch(board, row, col)) > 0:
                #     # Small issue: returns a 3D list; list of a list of coordinates
                #     # might be good to change this later for simplicity
                #     matches.append(self.checkForMatch(board, row, col))
        return matches
    def checkForMatch(self, board, row, col):
        startingTile = board[row][col]
        if startingTile == self.emptyTile:
            return []
        up = row-1
        down = row+1
        matchLocations = []
        matchLocations.append((row,col))

        # check above
        while up >= 0 and board[up][col] == startingTile:
            matchLocations.append((up,col))
            up -= 1

        # check below
        while down < len(board) and board[down][col] == startingTile:
            matchLocations.append((down, col))
            down += 1

        if len(matchLocations) >= self.min_matching_length:
            return matchLocations
        else:
            return []


if __name__ == "__main__":
    print("matching tests")
    grid = [[0, 0, 0, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 0, 1, 3],
            [2, 2, 2, 0, 3],
            [0, 0, 0, 3, 3]]
    matches = [VerticalMatch()]
    coordinates = []
    for match in matches:
        for x, y in match.checkMatch(grid):
            coordinates.append([x, y])
    for x, y in coordinates:
        grid[x][y] = "M"
    for row in grid:
        print(row)