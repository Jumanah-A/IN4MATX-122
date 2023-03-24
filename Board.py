# import EmptyTile
from time import sleep
from Tile import Tile
from TileFactory import TileFactory
from EmptyTile import EmptyTile


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
    def __init__(self, numRows: int, numCols: int, tileFactory: TileFactory) -> None:
        self.numRows = numRows
        self.numCols = numCols
        self.tileFactory = tileFactory
        self.grid = []

    # Initializes new grid of random tiles
    def createBoard(self):
        self.grid = [[self.generateRandomTile() for _ in range(self.numCols)]
                     for _ in range(self.numRows)]

    # Shift tiles down by calling gravity() and populates empty tiles with fillBoard()
    def updateBoard(self, setOfCoords, gui, playerTurn=-1):
        if (setOfCoords):
            sleep(0.5)
            self.removeTiles(setOfCoords)
            gui.drawBoard(self.grid, playerTurn)

            sleep(0.5)
            self.applyGravity()
            gui.drawBoard(self.grid, playerTurn)

            sleep(0.5)
            self.fillBoard()
            gui.drawBoard(self.grid, playerTurn)

            sleep(0.5)
            gui.drawBoard(self.grid, playerTurn)

    # return bool
    def isValidSwap(self, tile_coords, direction: str) -> bool:
        (y, x) = tile_coords
        if ((direction == "left" and x == 0) or
                (direction == "right" and x == (self.numCols - 1)) or
                (direction == "up" and y == 0) or
                (direction == "down" and (y == self.numRows - 1))):
            return False
        else:
            return True

    # swaps tiles
    def swapTile(self, tile_coords, direction):
        grid = self.grid
        (y_1, x_1) = tile_coords
        (y_2, x_2) = (y_1, x_1)
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

        tile = grid[x_1][y_1]
        grid[x_1][y_1] = grid[x_2][y_2]
        grid[x_2][y_2] = tile

    def removeTiles(self, coords: set):
        # remove a set of tiles
        # consider passing in a set of coordinates, not tiles
        for (x, y) in coords:
            self.grid[x][y] = EmptyTile()

    # debugging function
    # def printBoard(self):
    #     for y in range(self.numRows):
    #         for x in range(self.numCols):
    #             tile = self.grid[y][x]
    #             if isinstance(tile, EmptyTile):
    #                 print("1", end="")
    #             else:
    #                 print(tile.color, end="")
    #         print("")

    # uses tile factory to create a random tile
    def generateRandomTile(self):
        return self.tileFactory.createRandomTile()

    # shifts tiles down to replace empty space
    def applyGravity(self):
        grid = self.grid
        # start from col 0, col 1, col 2, etc
        for x in range(self.numCols):
            next_empty = -1  # represents the first empty index
            # start from the bottom of column, then work the way up
            for y in reversed(range(self.numRows)):
                if isinstance(grid[x][y], EmptyTile) and next_empty == -1:
                    next_empty = y

                if not isinstance(grid[x][y], EmptyTile) and next_empty != -1:
                    grid[x][next_empty] = grid[x][y]
                    grid[x][y] = EmptyTile()
                    next_empty -= 1

    def fillBoard(self):
        grid = self.grid
        for y in range(self.numRows):
            for x in range(self.numCols):
                if isinstance(grid[x][y], EmptyTile):
                    grid[x][y] = self.generateRandomTile()
