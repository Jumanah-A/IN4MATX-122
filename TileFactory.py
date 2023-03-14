import Tile
import random


class TileFactory:
    def __init__(self, tiles) -> None:
        # ['candycane', 'star']
        self.tiles = tiles

    def createTile(self,shape, color, name):
        return Tile(shape, color, name)

    def createRandomTile(self):
        return random.choice(self.tiles)
