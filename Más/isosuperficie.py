import pygame, sys, math
from pygame.locals import *

pygame.init()

ancho=600
alto=360
ventana=pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("isosuperficie")


mi_fuente=pygame.font.SysFont("Arial",15) #3. Se define fuente



while True:

	for x in range(0,ancho):
		for y in range(0,alto):
			d=math.sqrt((ancho-x)**2+(alto-y)**2)
			print(d/3)
			color=(0,d/3,0) # Tupla color, depende de pixel
			# color=(int(x*255/ancho),0,int(y*255/alto)) # Tupla color, depende de pixel. Se ve degradado entre azul y rojo
			print(color) # Imprime tupla 'color' para hacer seguimiento
			ventana.set_at((x,y),color) # Se pinta pixel de color en la variable 'color'
	
	# color_pixel=ventana.get_at(pygame.mouse.get_pos())# Devuelve color sobre el que está el puntero como tupla RGBA. ¡¡¡HACE LENTO ESTE PROGRAMA!!!
	# texto=mi_fuente.render("Color R: "+str(color_pixel[0])+" Color G: "+str(color_pixel[1])+" Color B: "+str(color_pixel[2])+" Alpha: "+str(color_pixel[3]),0,(255,255,255)) #3. Crear objeto texto con cada color
	# ventana.blit(texto,(50,50))#. Mostrar objeto texto con el número de cada color
	
	for evento in pygame.event.get():
		if evento.type==QUIT:
			pygame.quit()
			sys.exit()
		
	pygame.display.update()	
		