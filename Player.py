class Player:
    def __init__(self, score, name):
        self.score = score
        self.name = name

    def setName(self, name):
        self.name = name

    def increaseScore(self, amount):
        self.score += amount

    def resetScore(self):
        self.score = 0

    def getName(self):
        return self.name

    def getScore(self):
        return self.score