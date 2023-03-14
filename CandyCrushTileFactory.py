import Tile
import random

class CandyCrushTileFactory:
    def __init__(self, tiles) -> None:
        self.tiles= tiles

    def createTile(self,shape, color):
        name= color + " "+ shape
        if(name in self.tiles):
            return Tile(shape, color)
        else:
            print("Error: Tile not in Tile Factory")

    def createRandomTile(self):
        tileName=random.choice(self.tiles)
        color = tileName.split()[0]
        shape = tileName.split()[1]
        return Tile(shape, color)
