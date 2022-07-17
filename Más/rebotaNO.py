import pygame, sys, random
from pygame.locals import *

width=400
height=400
r=40



pygame.init()
ventana=pygame.display.set_mode((width,height))
pygame.display.set_caption("rebota")

posX=0
posY=400

velX=2
velY=1

derecha=True
arriba=True
diagonal=True



while True:
	
	ventana.fill((255,255,255))
	circulo=pygame.draw.circle(ventana,(0,0,255),(posX,posY),r)
	
	for evento in pygame.event.get():
		if evento.type==QUIT:
			pygame.quit()
			sys.exit()
		
	if derecha==True and arriba==True:
		if posX<width-r and posY>r:
			posX+=velX
			posY-=velY
			print(posX, posY)
		elif posX==width-r and posY>r:
			derecha==False
			donde=[True, False]
			indice=random.randint(0,1)
			arriba=donde[indice]		
		elif posX<width-r and posY==r:
			arriba==False
			donde=[True, False]
			indice=random.randint(0,1)
			derecha=donde[indice]
		else: #posX==width-r and posY==r
			derecha=False
			arriba=False
		print("Derecha: "+str(derecha)+"\nArriba: "+str(arriba))

	elif derecha==True and arriba==False:
		if posX<width-r and posY>r:
			posX+=velX
			posY+=velY
		elif posX==width-r and posY>r:
			derecha==False
			donde=[True, False]
			indice=random.randint(0,1)
			arriba=donde[indice]		
		elif posX<width-r and posY==r:
			arriba==True
			donde=[True, False]
			indice=random.randint(0,1)
			derecha=donde[indice]
		else: #posX==width-r and posY==r
			derecha=False
			arriba=True
		print("Derecha: "+str(derecha)+"\nArriba: "+str(arriba))
	
	elif derecha==False and arriba==False:
		if posX<width-r and posY>r:
			posX-=velX
			posY+=velY
		elif posX==width-r and posY>r:
			derecha==True
			donde=[True, False]
			indice=random.randint(0,1)
			arriba=donde[indice]		
		elif posX<width-r and posY==r:
			arriba==True
			donde=[True, False]
			indice=random.randint(0,1)
			derecha=donde[indice]
		else: #posX==width-r and posY==r
			derecha=True
			arriba=True
		print("Derecha: "+str(derecha)+"\nArriba: "+str(arriba))
		
	else: # derecha==False and arriba==True
		if posX<width-r and posY>r:
			posX-=velX
			posY-=velY
		elif posX==width-r and posY>r:
			derecha==True
			donde=[True, False]
			indice=random.randint(0,1)
			arriba=donde[indice]		
		elif posX<width-r and posY==r:
			arriba==False
			donde=[True, False]
			indice=random.randint(0,1)
			derecha=donde[indice]
		else: #posX==width-r and posY==r
			derecha=True
			arriba=False
		print("Derecha: "+str(derecha)+"\nArriba: "+str(arriba))
			
		
	pygame.display.update()