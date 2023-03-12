class Player:
    def __init__(self, score, name):
        self.score = score;
        self.name = name;

    def setName(self, name):
        self.name = name

    def increaseScore(self, amount):
        self.score += amount