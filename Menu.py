# class Menu:
#     def __init__(self) -> None:
#         self.games = []
#         pass

#     def chooseGame(self, chosenGame):
#         self.currentGame = chosenGame
#         pass

#     #create new instance/start()  of current game
#     def restartGame():
#         #chosenGame.resetGame()
#         pass

# def main():
#     pass

# if __name__ == "__main__":
#     main()
from Bejeweled import Bejeweled
from CandyCrush import CandyCrush
from functools import partial
import pygame_menu


class Menu:
    def __init__(self, GUI) -> None:
        self.games = [(CandyCrush, "Candy Crush"), (Bejeweled, "Bejeweled")]
        self.theme = pygame_menu.themes.THEME_BLUE.copy()
        self.theme.title_font = pygame_menu.font.FONT_FRANCHISE
        self.theme.widget_font = pygame_menu.font.FONT_FRANCHISE
        self.GUI = GUI
        self.mainMenu()

    def updateMenu(self):
        self.menu.mainloop(self.GUI.DISPLAYSURF)

    def chooseNumPlayers(self, game):
        self.resetMenu()
        self.menu.add.button('1 Player', partial(
            self.chooseNames, game, playerCount=1))
        self.menu.add.button('2 Player', partial(
            self.chooseNames, game, playerCount=2))
        self.menu.add.button('Go Back', self.mainMenu)
        self.updateMenu()

    def chooseNames(self, game, playerCount):
        self.resetMenu()
        nameInputs = []
        for playerNum in range(playerCount):
            nameInputs.append(self.menu.add.text_input(
                "Player " + str(playerNum+1) + ": "))
        self.menu.add.button('Start Game', partial(
            self.startGame, game, playerCount, nameInputs))
        self.menu.add.button('Go Back', self.mainMenu)
        self.updateMenu()

    def resetMenu(self):
        self.menu = pygame_menu.Menu(
            'INF122 FINAL PROJECT', 1000, 600, theme=self.theme)

    def startGame(self, game, playerCount, nameInputs):
        playerNames = [nameInput.get_value() for nameInput in nameInputs]
        gameInstance = game(playerCount, playerNames, self.GUI)
        self.GUI.setGameAttributes(gameInstance)
        gameInstance.start()

    def mainMenu(self):
        self.resetMenu()

        for game, name in self.games:
            self.menu.add.button('Play ' + name, partial(
                self.chooseNumPlayers, game))

        self.menu.add.button('Quit', pygame_menu.events.EXIT)
