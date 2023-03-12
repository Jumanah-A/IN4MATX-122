import EmptyTile
import Tile


class Board:
    # A grid as follows has 4 rows and 3 cols, with the top left tile (0, 0)
    # and bottom right tile (3, 2)
    # [
    #   [tile, tile, tile]
    #   [tile, tile, tile]
    #   [tile, tile, tile]
    #   [tile, tile, tile]
    # ]
    #
    def __init__(self, numRows: int, numCols: int) -> None:
        self.numRows = numRows
        self.numCols = numCols
        self.grid = []

    # ???
    def createBoard(self):
        self.grid = [[EmptyTile() for x in range(self.numCols)]
                     for y in range(self.numRows)]

    # Set grid to empty tiles.. or set to initial board state?
    def resetBoard(self):
        pass

    # Shift tiles down by calling gravity() and populates empty tiles with fillBoard()
    def updateBoard(self, setOfCoords):
        self.removeTiles(setOfCoords)
        self.applyGravity()
        self.fillBoard()

    # return bool
    def isValidSwap(self, tile: Tile, direction: str) -> bool:
        (x, y) = self.getTileCoords(tile)
        if ((direction == "left" and x == 0) or
                (direction == "right" and x == (self.col - 1)) or
                (direction == "up" and y == 0) or
                (direction == "down" and (y == self.row - 1))):
            return False
        else:
            return True

    # swaps tiles
    def swapTile(self, tile_coords, direction):
        grid = self.grid
        (x_1, y_1) = tile_coords
        (x_2, y_2) = (x_1, y_1)
        if direction == "left":
            x_2 -= 1
        elif direction == "right":
            x_2 += 1
        elif direction == "up":
            y_2 -= 1
        elif direction == "down":
            y_2 += 1
        else:
            print("Direction not valid")

        grid[y_1][x_1] = grid[y_2][x_2]
        grid[y_2][x_2] = tile

    def removeTiles(self, coords: set):
        # remove a set of tiles
        # consider passing in a set of coordinates, not tiles

        pass

    # uses tile factory to create a random tile
    def generateRandomTile():
        pass

    # shifts tiles down to replace empty space
    def applyGravity(self):
        grid = self.grid
        # start from col 0, col 1, col 2, etc
        for x in range(self.col):
            next_empty = -1  # represents the first empty index
            # start from the bottom of column, then work the way up
            for y in reversed(range(self.row)):
                if isinstance(grid[y][x], EmptyTile) and next_empty == -1:
                    next_empty = y

                if not isinstance(grid[y][x], EmptyTile) and next_empty != -1:
                    grid[next_empty][x] = grid[y][x]
                    grid[y][x] = EmptyTile()
                    next_empty -= 1

    def fillBoard(self):
        grid = self.grid
        for y in range(self.row):
            for x in range(self.row):
                if isinstance(grid[y][x], EmptyTile):
                    grid[y][x] = self.generateRandomTile()
