import pygame, sys
from pygame.locals import *

pygame.init()
ventana=pygame.display.set_mode((600,300))
pygame.display.set_caption("reloj arena")

posX=30
posY=270

velX=2
velY=1

derecha=True
arriba=True
diagonal=True
ctrl_mov=1

while True:
	ventana.fill((255,255,255))
	circulo=pygame.draw.circle(ventana,(0,0,255),(posX,posY),30)
	for evento in pygame.event.get():
		if evento.type==QUIT:
			pygame.quit()
			sys.exit()
		
	if ctrl_mov==1:	
		if posX<=570 and posY>=30:
			posX+=velX
			posY-=velY
			print(posX,posY)
		else:
			ctrl_mov=2
		print(posX, posY)
		
	elif ctrl_mov==2:
		if posX>0:
			posX-=velX
		else:
			ctrl_mov=3
	elif ctrl_mov==3:
		if posX<=570 and posY<=270:
			posX+=velX
			posY+=velY
		else:
			ctrl_mov=4
	else:
		if posX>0: 
			posX-=velX
		else:
			ctrl_mov=1
	
	pygame.display.update()