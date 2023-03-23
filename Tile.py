class Tile:
    def __init__(self, shape, color) -> None:
        self.shape = shape
        self.color = color

    def getName(self):
        name = self.color + " " + self.shape
        return name

    def __eq__(self, __o) -> bool:
        if (self.shape == __o.shape and self.color == __o.color and isinstance(__o, type(self))):
            return True
        return False
