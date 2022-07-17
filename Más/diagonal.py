import pygame, sys, time
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
	ventana.fill((255,255,255))
	circulo=pygame.draw.circle(ventana,(float(255/(posX**1/32+1)),float(255/(posY**1/32+1)),10),(posX,posY),30)
	
	for evento in pygame.event.get():
		if evento.type==QUIT:
			pygame.quit()
			sys.exit()
	
	if diagonal==True:		
		if posX<600 and posY>0:
			posX+=velX
			posY-=velY
		else:
			diagonal=False
	else:
		if posX>0 and posY<300:
			posX-=velX
			posY+=velY
		else:
			diagonal=True
	
		
	
	time.sleep(0.2)		
	pygame.display.update()	
		