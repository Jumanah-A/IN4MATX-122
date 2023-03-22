from Tile import Tile
from TileFactory import TileFactory
import random


class BejeweledTileFactory(TileFactory):
    def __init__(self) -> None:
        gems = ["red square", "yellow rhombus", "green circle", "blue diamond", "purple triangle", "white ball"]
        super().__init__(gems)

    def createTile(self, shape, color):
        name = color + " " + shape
        if (name in self.tiles):
            return Tile(shape, color)
        else:
            print("Error: Tile not in Tile Factory")

    def createRandomTile(self):
        tileName = random.choice(self.tiles)
        color = tileName.split()[0]
        shape = tileName.split()[1]
        return Tile(shape, color)
