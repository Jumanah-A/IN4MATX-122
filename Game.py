import Controller

class Game:
	def __init__(self, players, board, matchingLogic, timer = None):
		self.players = players
		self.board = board
		self.playerTurn = 0
		self.matchingLogic = matchingLogic
		self.timer = timer
		self.controller = Controller()

	def resetGame(self):
		self.playerTurn = 0
		self.board.resetBoard()

	def start(self):
		self.board.createBoard()
		running = True
		
		while(running):
			coordinates, direction = self.controller.getInput()
			
			if coordinates == (-1, 0):
				running = False

			elif coordinates != (-1, -1):
				if self.board.isValidSwapTile(coordinates, direction):
					self.board.swapTile(coordinates, direction)
					self.board.updateBoard()




