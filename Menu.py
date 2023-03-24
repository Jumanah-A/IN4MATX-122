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
import pygame_menu


class Menu:
    def __init__(self, GUI) -> None:
        my_theme = pygame_menu.themes.THEME_BLUE.copy()
        my_theme.title_font = pygame_menu.font.FONT_FRANCHISE
        my_theme.widget_font = pygame_menu.font.FONT_FRANCHISE
        self.menu = pygame_menu.Menu(
            'INF122 FINAL PROJECT', 1000, 600, theme=my_theme)

        self.menu.add.button('Play Candy Crush 1P', GUI.startCandyCrush1P)
        self.menu.add.button('Play Candy Crush 2P', GUI.startCandyCrush2P)
        self.menu.add.button('Play Bejeweled 1P', GUI.startBejeweled1P)
        self.menu.add.button('Play Bejeweled 2P', GUI.startBejeweled2P)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)

    def mainloop(self, surface):
        self.menu.mainloop(surface)
