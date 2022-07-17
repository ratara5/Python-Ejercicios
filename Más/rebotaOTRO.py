# 29/03/2018 Crear variable de control para que se sepa desde dónde viene la bola

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
velY=1

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
	
	# if iraderecha==True and posX<width-r:
		# if iraarriba==True and posY>r:
			# if vienedederecha==False: # viene de la izquierda
				# posX+=velX
				# if vienedearriba==False: # viene de abajo
					# posY-=velY
				# else:
					# pass
				
		# if arriba==False and posY==r:
			# posX+=velX
			# posY+=velY	
			
	if derecha==True:
		if posX<width-r:
			posX+=velX
		else:
			derecha=False
			donde=[True, False] # Arriba aleatorio
			indice=random.randint(0,1) # Arriba aleatorio
			arriba=donde[indice] # Arriba aleatorio
	else:
		if posX>r:
			posX-=velX
		else:
			derecha=True
			donde=[True, False] # Arriba aleatorio
			indice=random.randint(0,1) # Arriba aleatorio
			arriba=donde[indice] # Arriba aleatorio
			
	if arriba==True:
		if posY>r:
			posY-=velY
		else:
			arriba=False
			donde=[True, False] # Derecha aleatorio
			indice=random.randint(0,1) # Derecha aleatorio
			derecha=donde[indice] # Derecha aleatorio
	else:
		if posY<height-r:
			posY+=velY
		else:
			arriba=True
			donde=[True, False] # Derecha aleatorio
			indice=random.randint(0,1) # Derecha aleatorio
			derecha=donde[indice] # Derecha aleatorio
			
			
	# if derecha==True and arriba==True:
		# if posX<width-r and posY>r:
			# posX+=velX
			# posY-=velY
			# print(posX, posY)
		# elif posX==width-r and posY>r:
			# derecha==False
			# else:
		# if posX>=r
			# pos-=velX	
		# elif posX<width-r and posY==r:
			# arriba==False
			# donde=[True, False]
			# indice=random.randint(0,1)
			# derecha=donde[indice]
		# else: #posX==width-r and posY==r
			# derecha=False
			# arriba=False
		# print("Derecha: "+str(derecha)+"\nArriba: "+str(arriba))

	# elif derecha==True and arriba==False:
		# if posX<width-r and posY>r:
			# posX+=velX
			# posY+=velY
		# elif posX==width-r and posY>r:
			# derecha==False
			# donde=[True, False]
			# indice=random.randint(0,1)
			# arriba=donde[indice]		
		# elif posX<width-r and posY==r:
			# arriba==True
			# donde=[True, False]
			# indice=random.randint(0,1)
			# derecha=donde[indice]
		# else: #posX==width-r and posY==r
			# derecha=False
			# arriba=True
		# print("Derecha: "+str(derecha)+"\nArriba: "+str(arriba))
	
	# elif derecha==False and arriba==False:
		# if posX<width-r and posY>r:
			# posX-=velX
			# posY+=velY
		# elif posX==width-r and posY>r:
			# derecha==True
			# donde=[True, False]
			# indice=random.randint(0,1)
			# arriba=donde[indice]		
		# elif posX<width-r and posY==r:
			# arriba==True
			# donde=[True, False]
			# indice=random.randint(0,1)
			# derecha=donde[indice]
		# else: #posX==width-r and posY==r
			# derecha=True
			# arriba=True
		# print("Derecha: "+str(derecha)+"\nArriba: "+str(arriba))
		
	# else: # derecha==False and arriba==True
		# if posX<width-r and posY>r:
			# posX-=velX
			# posY-=velY
		# elif posX==width-r and posY>r:
			# posX-=velX
			# posY-=velY
			# donde=[True, False]
			# indice=random.randint(0,1)
			# arriba=donde[indice]		
		# elif posX<width-r and posY==r:
			# arriba==False
			# donde=[True, False]
			# indice=random.randint(0,1)
			# derecha=donde[indice]
		# else: #posX==width-r and posY==r
			# derecha=True
			# arriba=False
		# print("Derecha: "+str(derecha)+"\nArriba: "+str(arriba))
			
		
	pygame.display.update()