import pygame
from Player import Player

class Keyboard:
	def __init__(self):
		self.a = False
		self.aCount = 0

	def keyboard(self, pygame, Player):
		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT]:
			Player.runLeft()
		if key[pygame.K_RIGHT]:
			Player.runRight()
		if not key[pygame.K_RIGHT] and not key[pygame.K_LEFT]:
			Player.runStop()
		if key[pygame.K_a] and self.aCount <= 8:
			Player.jumpFloor(key[pygame.K_RIGHT], key[pygame.K_LEFT], self.aCount)
		if key[pygame.K_s]:
			Player.glide()
		if key[pygame.K_DOWN]:
			Player.stamp()

		if key[pygame.K_a]:
			self.aCount += 1
		else:
			self.aCount = 0
			Player.jump = False