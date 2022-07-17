# 29/03/2018 En este programa es probable que la pelota tome una trayectoria anterior. Se puede cambiar...

import pygame, sys, random
from pygame.locals import *

width=400
height=400
r=40

pygame.init()
ventana=pygame.display.set_mode((width,height))
pygame.display.set_caption("rebota")

posX=80
posY=360

velX=2
velY=2

derecha=True
vienedederecha=True
arriba=True
vienedearriba=True
control=1


while True:
	
	ventana.fill((255,255,255))
	circulo=pygame.draw.circle(ventana,(0,0,255),(posX,posY),r)
	
	for evento in pygame.event.get():
		if evento.type==QUIT:
			pygame.quit()
			sys.exit()	
			
	if derecha==True:  # Lógica de X izquierda derecha
		if posX<width-r:
			posX+=velX
		else:
			derecha=False		
	else:
		if posX>r:
			posX-=velX
		else:
			derecha=True
				
	if arriba==True:  # Lógica de Y arriba abajo
		if posY>r:
			posY-=velY
		else:
			arriba=False		
	else:
		if posY<height-r:
			posY+=velY
		else:
			arriba=True
			
	if posX==r or posX==width-r:  # Al tocar bordes izquierdo o derecho
		donde=[True, False] # Arriba aleatorio
		indice=random.randint(0,1) # Arriba aleatorio
		arriba=donde[indice] # Arriba aleatorio
		velY=random.randint(2,5)
		velX=random.randint(2,5)
		
	if posY==r or posY==height-r:  # Al tocar bordes superior o inferior
		donde=[True, False] # Derecha aleatorio
		indice=random.randint(0,1) # Derecha aleatorio
		derecha=donde[indice] # Derecha aleatorio
		velX=random.randint(2,5)
		velY=random.randint(2,5)
		
	clock = pygame.time.Clock()
	clock.tick(180)
	
	pygame.display.update()