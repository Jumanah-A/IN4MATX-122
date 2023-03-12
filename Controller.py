import pygame
from pygame.locals import *

class Controller(object):

	def getInput(self):
		clicked = False
		cordinates = (0,0)
		direction = ""

		for event in pygame.event.get():
			if event.type == QUIT:
				return (-1, 0)
			
			if clicked == False and event.type == MOUSEBUTTONDOWN:
				clicked = True
				coordinates = (event.pos[0], event.pos[1])
			
			if clicked == True and event.type == MOUSEBUTTONUP:
				clicked = False
				coordinates = (0, 0)

			if clicked == True and event.type == MOUSEMOTION:
				x_move = coordinates[0] - event.pos[0]
				y_move = coordinates[1] - event.pos[1]

				if abs(x_move) >= abs(y_move):
					if x_move > 0:
						direction = "left"
					else:
						direction = "right"
				else:
					if y_move > 0:
						direction = "down"
					else:
						direction = "up"
				
			if direction != "":
				return coordinates, direction
		
		return (-1,-1)