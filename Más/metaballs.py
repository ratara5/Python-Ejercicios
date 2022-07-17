import pygame, sys
from pygame.locals import *

pygame.init()

ventana=pygame.display.set_mode((600,300))
pygame.display.set_caption("diagonal")

posX=60
posY=250

velX=2
velY=1

derecha=True
arriba=True
diagonal=True


while True:
	for x in range(0,600)
		for y in range(0,300)
			ventana.fill((x+1,y+1,x+y+1))
	
	for evento in pygame.event.get():
		if evento.type==QUIT:
			pygame.quit()
			sys.exit()
	
	pygame.display.update()	
		