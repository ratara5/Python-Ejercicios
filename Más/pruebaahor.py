import pygame, sys #1.
from pygame.locals import * #1.
from random import randint #7.

color=(255,255,255)

pygame.init() #2.Necesario en cualquier programa que use pygame
ventana=pygame.display.set_mode((600,300)) #2.Objeto superficie, en este caso: ventana
pygame.display.set_caption("Hola Mundo") #2.Agregar texto a la barra de título de la superficie 

ban_pal = ["genesis", "exodo", "levitico", "deuteronomio", "numeros", "josue", "jueces", "rut", "esdras", "nehemias", "cronicas", "samuel", "reyes", "ester", "job", "salmos"]
empezar = "s"

i = len(ban_pal)-1 # ya que randint busca entre los dos extremos del intervalo INCLUIDOS
j = randint(0,i) # generar aleatorio
pal_ban_pred = ban_pal[j] # seleccionar elemento de indice 'j' como palabra a acertar
pal_pred=""

for k in range(0,len(pal_ban_pred)):
		pal_pred = pal_pred + pal_ban_pred[k] + "," # las letras de la palabra generada se separan por ','
		pal_pred = pal_pred.rstrip(",") # Se elimina la última ',' de la derecha
		print(pal_pred)
		lis_pred = pal_pred.split(",") # Se convierte la palabra predeterminada en una lista en la que cada elemento es una letra en su posición
		print(lis_pred)
		print("La palabra tiene "+str(len(lis_pred))+" letras")
		lis_usu = []


while True:

	for evento in pygame.event.get(): #2.Revisa lista de eventos predefinidos en pygame
		if evento.type==QUIT: #2.Evento quit
			pygame.quit() #2.Deja de ejecutarse el presente
			sys.exit() #2.Se cierra ventana
			
	for i in range(0,4): #Se hace una linea tras otra tantas veces como como maxrange-1
		a=55
		lineaInicia=(60+a*i,80)
		lineaTermina=(100+a*i,80)
		pygame.draw.line(ventana,color,lineaInicia,lineaTermina,8)
	
	
			
	pygame.display.update() #2.Se actualiza o refresca ventana
