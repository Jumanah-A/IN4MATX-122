from Tile import Tile


class EmptyTile(Tile):
    def __init__(self):
        super().__init__("", "none")
