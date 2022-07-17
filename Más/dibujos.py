import pygame,sys
from pygame.locals import *

pygame.init()

color1=(255,0,255,100) # 1. Color transparente con componente alpha
color2=(0,255,255,100) # 1. Color transparente con componente alpha
rojo=(255,0,0) # 2.
verde=(0,255,0) # 2.
azul=(0,0,255) # 2.
blanco=(255,255,255) # 2. 

ventana=pygame.display.set_mode((400,400)) # Ventana de dibujo
pygame.display.set_caption("dibujos") # Título de la ventana de dibujo

# ventana.fill((255,255,255))
c1=pygame.Surface((200,200)).convert_alpha() # 1. Superficie de tamaño 200x200 y transparente
c2=pygame.Surface((200,200)).convert_alpha() # 1. Superficie de tamaño 200x200 y transparente
c1.fill(color1) # 1. Lleno de la superficie
c2.fill(color2) # 1. Lleno de la superficie
#ventana.blit(c1, (20,20)) # 1. Dibujar superficie en la ventana en la posición 20,20
#ventana.blit(c2, (140,140)) # 1. Dibujar superficie en la ventana en la posición 140,140
# ventana.set_clip(0,0,200,200) # 2. Se enfoca atención en espacio desde 0,0 alto 200, ancho 200
# ventana.fill(rojo) # 2. Se colorea espacio enfocado
# ventana.set_clip(200,0,200,200) # 2. Se enfoca atención en espacio desde 0,0 alto 200, ancho 200
# ventana.fill(verde) # 2. Se colorea espacio enfocado
# ventana.set_clip(0,200,200,200) # 2. Se enfoca atención en espacio desde 0,0 alto 200, ancho 200
# ventana.fill(azul) # 2. Se colorea espacio enfocado
# ventana.set_clip(200,200,200,200) # 2. Se enfoca atención en espacio desde 0,0 alto 200, ancho 200
# ventana.fill(blanco) # 2. Se colorea espacio enfocado

mi_imagen=pygame.image.load('Imagenes/nave.png') # 3. Carga imagen desde archivo
mi_imagen=mi_imagen.convert_alpha() # 3. Convierte imagen en pixel a formato de la ventana
mi_imagen_rect=mi_imagen.get_rect() # 3. Obtiene el rectángulo q ocupa la imagen, como <rect(0, 0, 180, 200)>
ventana_rect=ventana.get_rect() # 3. Obtiene el rectángulo q ocupa la ventana
xc,yc=mi_imagen_rect.center # 3. Obtiene las coordenadas del centro del rectángulo de la imagen
vh,vv=ventana_rect.center # 3. Obtiene las coordenadas del centro del rectángulo de la ventana

 
rectangulo=pygame.Rect(30,30,15,15) # 3. Objeto rectángulo que contendrá la muestra
rectangulodos=pygame.Rect(30,30,16,16) # 3. Objeto rectángulo para el borde del que contendrá la muestra
mi_fuente=pygame.font.SysFont("Arial",15) #3. Se define fuente

while True:
	ventana.fill((0,0,0))
	ventana.blit(mi_imagen,(int(vh-xc),int(vv-yc))) # 3. Dibuja la imagen con su centro en las coordenadas del centro de la ventana
	
	for evento in pygame.event.get():
		if evento.type==QUIT:
			pygame.quit()
			sys.exit()
	
	color_pixel=ventana.get_at(pygame.mouse.get_pos())# 3. Devuelve color sobre el que está el puntero como tupla RGBA
	pygame.draw.rect(ventana,(255,255,255),rectangulodos,1) #3. Dibuja el objeto rectángulo para el borde
	pygame.draw.rect(ventana,(color_pixel),rectangulo)#3. Se (Dibuja)llena el rectángulo con el color del pixel sobre el que está el puntero
	texto=mi_fuente.render("Color R: "+str(color_pixel[0])+" Color G: "+str(color_pixel[1])+" Color B: "+str(color_pixel[2])+" Alpha: "+str(color_pixel[3]),0,(255,255,255)) #3. Crear objeto texto con cada color
	ventana.blit(texto,(50,50))#3. Mostrar objeto texto con el número de cada color
	
	pygame.display.update()	
	