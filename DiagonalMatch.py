from IMatch import IMatch
from VerticalMatch import VerticalMatch
from HorizontalMatch import HorizontalMatch

class DiagonalMatch(IMatch):
    def checkMatch(self, board):
        matches = []
        for row in range(len(board)):
            for col in range(len(board[row])):
                for x, y in self.checkForMatch(board, row, col):
                    matches.append((x, y))
        return matches

    def checkForMatch(self, board, row, col):
        startingTile = board[row][col]
        if startingTile == self.emptyTile:
            return []

        matches1 = []
        downRight = [row+1, col+1]
        topLeft = [row-1, col-1]
        matches1.append((row, col))

        # Logic Here
        while (downRight[0] < len(board) and downRight[1] < len(board[row])
            and board[downRight[0]][downRight[1]] == startingTile):
                matches1.append((downRight[0], downRight[1]))
                downRight[0] += 1
                downRight[1] += 1

        while topLeft[0] >= 0 and topLeft[1] >= 0 and board[topLeft[0]][topLeft[1]] == startingTile:
            matches1.append((topLeft[0], topLeft[1]))
            topLeft[0] -= 1
            topLeft[1] -= 1

        if len(matches1) < self.min_matching_length:
            matches1 = []

        matches2 = []
        topRight = [row-1, col+1]
        downLeft = [row+1, col-1]
        matches2.append((row, col))

        while topRight[0] >= 0 and topRight[1] < len(board[topRight[0]]) and board[topRight[0]][topRight[1]] == startingTile:
            matches2.append((topRight[0], topRight[1]))
            topRight[0] -= 1
            topRight[1] += 1

        while downLeft[0] < len(board) and downLeft[1] >= 0 and board[downLeft[0]][downLeft[1]] == startingTile:
            matches2.append((downLeft[0], downLeft[1]))
            downLeft[0] += 1
            downLeft[1] -= 1

        if len(matches2) < self.min_matching_length:
            matches2 = []

        return list(set().union(matches1, matches2))


if __name__ == "__main__":
    print("matching tests")
    grid = [[3, 4, 3, 1, 1],
            [4, 3, 1, 1, 1],
            [3, 4, 1, 1, 3],
            [2, 2, 1, 3, 3],
            [2, 3, 3, 3, 3]]
    matches = [DiagonalMatch()]
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