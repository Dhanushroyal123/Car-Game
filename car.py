import pygame
import random
from pygame import mixer


pygame.init()


screen = pygame.display.set_mode((500, 800))


player = pygame.image.load(r'E:\Programming\Python\Gaming in python\car\car4.png')

mixer.music.load(r'E:\Programming\Python\Gaming in python\car\carsound.wav')

mixer.music.play(-1)

playerX, playerY, player_change = 190, 600, 0

def car(x, y):
	screen.blit(player, (x, y))

def rectangle(c = (), axis = ()):
	pygame.draw.rect(screen, c, axis)

rectx, recty, rectw, recth, rect_change = 230, 180, 40, 100, 0

l=[]

running = True

while running:
	screen.fill((0, 100, 0))
	rectangle((105, 105, 105), (100, 0, 300, 800))
	pygame.draw.line(screen, (255, 255, 255), (150, 0), (150, 800))
	pygame.draw.line(screen, (255, 255, 255), (350, 0), (350, 800))
	if recty >699:
		recty = 0
	if playerX<115:
		playerX = 115
	if playerX>260:
		playerX = 260
	rect_change = 1.5
	recty+= rect_change
	rectangle((255, 255, 255), (rectx, recty, rectw, recth))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player_change = -0.3
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				player_change = 0.3
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				player_change = 0
	playerX+=player_change
	car(playerX, playerY)
	pygame.display.update()


