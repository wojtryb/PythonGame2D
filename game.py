import pygame
from Player import Player
from Keyboard import Keyboard
from Ground import Ground

def myUpdate(P, G):
	
	P.checkStaticFriction()
	P.countX()
	P.countY()
	G.countAngle(P.x)
	G.countHeigth(P.x)
	P.checkFloor(G.heigth)
	#print(G.heigth, G.angle)

pygame.init()

width = 1920
heigth = 1080

win = pygame.display.set_mode((width, heigth))
screen = pygame.display.set_caption("My Awesome Game")
bg = pygame.image.load("bg1Art.png")

K = Keyboard()
G = Ground()
P = Player(G = G)

run = True;
while run:
	pygame.time.delay(20)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	K.keyboard(pygame, P)

	myUpdate(P, G)
	
	#print(P.ay, P.vy)
	#print(P.onFloor)
	
	win.fill((0, 0, 0))
	win.blit(bg, [0, 0]) #BACKGROUND - comment to get better performance

	P.render(win)
	pygame.display.update()

pygame.quit

