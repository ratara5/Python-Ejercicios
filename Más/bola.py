import pygame, sys, math
from pygame.locals import *

pygame.init()

ancho=600
alto=300
ventana=pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("bola")

posX=30
posY=270
velX=10
velY=5
ctrl_mov=1

mi_fuente=pygame.font.SysFont("Arial",15) #3. Se define fuente

while True:
	ventana.fill((0,85,0))
	for x in range(int(ancho/2),int(ancho)):
		for y in range(int(alto/2),int(alto)):
			d=math.sqrt((ancho-x)**2+(alto-y)**2)
			print(d)
			color=(0,d/3,0) # Tupla color, depende de pixel
			# color=(0,int(x*255/ancho),int(y*255/alto)) # Tupla color, depende de pixel. Se ve degradado entre azul y rojo
			print(color) # Imprime tupla 'color' para hacer seguimiento
			# ventana.set_at((x,y),color) # Se pinta pixel de color en la variable 'color'
			pygame.draw.circle(ventana,color,(posX,posY),int(d/4)) #Dibuja círculo
			
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