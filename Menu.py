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
        self.theme = pygame_menu.themes.THEME_BLUE.copy()
        self.theme.title_font = pygame_menu.font.FONT_FRANCHISE
        self.theme.widget_font = pygame_menu.font.FONT_FRANCHISE
        self.GUI = GUI
        self.mainMenu()

    def mainloop(self, surface):
        self.menu.mainloop(surface)

    def chooseGame(self, game):
        self.menu = pygame_menu.Menu(
            'INF122 FINAL PROJECT', 1000, 600, theme=self.theme)
        self.menu.add.button('1 Player', partial(
            self.startGame, playerCount=1))
        self.menu.add.button('2 Player', partial(
            self.startGame, playerCount=2))
        self.menu.add.button('Go Back', self.mainMenu)
        self.mainLoop(self.GUI.DISPLAYSURF)

    def startGame(self, game, playerCount):
        gameInstance = game(playerCount, self.GUI)
        self.GUI.setGame(gameInstance)

    def mainMenu(self):
        self.menu = pygame_menu.Menu(
            'INF122 FINAL PROJECT', 1000, 600, theme=self.theme)
        self.menu.add.button('Play Candy Crush', partial(
            self.chooseGame, game=CandyCrush))
        self.menu.add.button('Play Bejeweled', partial(
            self.chooseGame, game=Bejeweled))
        self.menu.add.button('Quit', pygame_menu.events.EXIT)
