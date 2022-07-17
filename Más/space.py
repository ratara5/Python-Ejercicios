import pygame, sys #1.
from pygame.locals import * #1.
from random import randint #7.

coloruno=(0,140,60) #3.Color tupla
colordos=pygame.Color(255,120,9) #3.Alternativa pygame color

pygame.init() #2.Necesario en cualquier programa que use pygame
ventana=pygame.display.set_mode((600,300)) #2.Objeto superficie, en este caso: ventana
pygame.display.set_caption("Hola Mundo") #2.Agregar texto a la barra de título de la superficie 

color=pygame.Color(70,80,150)#4 Crear color en pygame
pygame.draw.line(ventana,color,(60,80),(160,100),8) #4Dibuja linea, en dónde, con qué  color, de dónde a dónde, con qué ancho. OJO que pueden ir más parámetros
print (color.r) # 4. Método para saber saturación de color rojo (R ó r)
print (color.g) # 4. Método para saber saturación de color verde (G ó g)
print (color.b) # 4. Método para saber saturación de color azul (B ó b)

pygame.draw.circle(ventana,(50,150,50),(160,100),30) #5Dibuja círculo
pygame.draw.rect(ventana,(100,0,100),(160,100,200,250)) #5Dibuja rectángulo, en dónde, con qué color, desde qué punto y qué ancho y alto
pygame.draw.polygon(ventana,(90,180,170),((80,90),(50,100),(40,80),(60,80))) #5 Dibuja polígono cuyos lados son la unión de los puntos de la tupla de tuplas
# pygame.draw.polygon(ventana,(10,10,190),((140,0),(291,106),(237,277),(56,277),(0,106))) #5 Dibuja pentágono regular

# mi_imagen=pygame.image.load('Imagenes/nave.png') #6Objeto mi_imagen hace que este programa capte imagen
posX, posY=130,70 #6.Esquina superior izquierda de la imagen irá en este punto
# posX=randint(10,300) #7.
# posY=randint(10,200) #7.
# ventana.blit(mi_imagen,(posX,posY)) #6.Se dibuja imagen

rectangulo=pygame.Rect(0,0,100,50) #11.Crear objeto rectangulo
rectangulodos=pygame.Rect(100,100,100,50) #11.Crear objeto rectangulodos

mi_fuente=pygame.font.SysFont("Arial",50) #12.Crear fuente de sistema, nombre de fuente y color
mi_texto=mi_fuente.render("Prueba Hola",0,(100,100,100),(50,0,50)) #12.Crear texto aplicando fuente ya creada

velocidad=1 #8.

derecha=True

while True: #2.Ciclo infinto
	ventana.fill((255,255,255)) #3.Se pinta color fondo en ventana, blanco en esta ocasión
	# ventana.blit(mi_imagen,(posX,posY)) #8.
	# ventana.blit(mi_texto,(100,100)) #12. Mostrar texto en ventana en la posición indicada
	
	pygame.draw.rect(ventana,(100,70,70),rectangulo) #11. Dibujar objeto rectangulo
	pygame.draw.rect(ventana,(0,255,0),rectangulodos) #11. Dibujar objeto rectangulodos
	rectangulo.left,rectangulo.top=pygame.mouse.get_pos() #10.Retorna tupla con coordenadas de mouse y se la entrega a la ezquina superior izquierda del objeto
	rectangulo.left=rectangulo.left-50 #10.Mover la esquina superior izquierda de la imagen, para que el centro del objeto dibujado coincida con el puntero.
	rectangulo.top=rectangulo.top-25 #10.Mover la esquina superior izquierda de la imagen, para que el centro del objeto dibujado coincida con el puntero.
	
	tiempo=pygame.time.get_ticks() #13.Almacenar en variable contador de milisegundos
	segundos=tiempo//1000 #13.División entera de milisegundos
	if tiempo==segundos*1000:
		print(segundos) #13. Imprimir solo segundos enteros. OJO: No se imprime el segundo de la colisión
	texto_seg=mi_fuente.render("Tiempo: "+str(segundos),0,(100,255,100)) #13. Crear objeto texto con segundos
	ventana.blit(texto_seg,(100,100))#13. Mostrar objeto texto con segundos en ventana
	
	
	if rectangulo.colliderect(rectangulodos): #11.Pregunta si rectangulodos colisiona con algo
		velocidad=0
	
	for evento in pygame.event.get(): #2.Revisa lista de eventos predefinidos en pygame
		if evento.type==QUIT: #2.Evento quit
			pygame.quit() #2.Deja de ejecutarse el presente
			sys.exit() #2.Se cierra ventana
		# elif evento.type==pygame.KEYDOWN: #9.Eventos con el teclado
			# if evento.key==K_LEFT: #9.Si presiono tecla  izquierda...
				# posX-=velocidad #9... imagen va a la izquierda
			# elif evento.key==K_RIGHT: #9.Si presiono tecla  derecha...
				# posX+=velocidad #9... imagen va a la derecha
		# elif evento.type==pygame.KEYUP: #9.Si levanto tecla  izquierda...
			# if evento.key==K_LEFT:
				# print("Tecla izquierda liberada")
			# elif evento.key==K_RIGHT:  #9.Si levanto tecla  derecha...
				# print("Tecla derecha liberada")
	
	if derecha==True: #8.Condición de movimiento a la derecha
		if posX<600:
			posX+=velocidad
			rectangulodos.left=posX #11.
			derecha=True
		else: #8.Cuando la posición en X sea 400
			derecha=False
	else: #8. Condición de movimiento a la izquierda
		if posX>0:
			posX-=velocidad
			rectangulodos.left=posX #11.
			derecha=False
		else: #8.Cuando la posición en X sea 0
			derecha=True
		
	pygame.display.update() #2.Se actualiza o refresca ventana
	
	
	