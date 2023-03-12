import Tile

class TileFactory:
    def __init__(self, tiles) -> None:
        # ['candycane', 'star']
        self.tiles = tiles

    def createTile(shape, color, name):
        return Tile(shape, color, name)

    def createRandomTile():
        pass
