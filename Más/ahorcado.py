# AHORCADO
# Se predefine en el programa un nombre y se le da al usuario la opción de introducir letras para ver cuáles coinciden con las de esa palabra...
# ...Se dará indicación de ello...
# ...Si la palabra es completada por el usuario en una cantidad de vidas menor o igual a la establecida, habrá ganado, sino morirá 'ahorcado'
# 28/03/2018...El programa no muestra cuando una letra es incorrecta, y menos durante un tiempo adecuado
	# ...Al introducir la última letra correctamente, no muestra el mensaje de felicitaciones durante un tiempo adecuado

import random, os, time # random para sacar palabra aleatorio// os para limpiar ventana
import pygame, sys #1.
from pygame.locals import * #1

pygame.init() #2.Necesario en cualquier programa que use pygame
ventana = pygame.display.set_mode((1000,300)) #2.Objeto superficie, en este caso: ventana
pygame.display.set_caption("Ahorcado") #2.Agregar texto a la barra de título de la superficie

mi_fuente=pygame.font.SysFont("Arial",50) #12.Crear fuente de sistema, nombre de fuente y color

ban_pal = ["genesis", "exodo", "levitico", "deuteronomio", "numeros", "josue", "jueces", "rut", "esdras", "nehemias", "cronicas", "samuel", "reyes", "ester", "job", "salmos"]
empezar = "s"


while empezar == "S" or empezar == "s":

	os.system('cls') # limpiar ventana
	i = len(ban_pal)-1 # ya que randint busca entre los dos extremos del intervalo INCLUIDOS
	j = random.randint(0,i) # generar aleatorio
	pal_ban_pred = ban_pal[j] # seleccionar elemento de indice 'j' como palabra a acertar
	# print(pal_ban_pred)
	pal_pred = ""
	
	for k in range(0,len(pal_ban_pred)):
		pal_pred = pal_pred + pal_ban_pred[k] + "," # las letras de la palabra generada se separan por ','
	pal_pred = pal_pred.rstrip(",") # Se elimina la última ',' de la derecha
	# print(pal_pred)
	lis_pred = pal_pred.split(",") # Se convierte la palabra predeterminada en una lista en la que cada elemento es una letra en su posición
	#print(lis_pred)
	# print("La palabra tiene "+str(len(lis_pred))+" letras")
	lis_usu = []
		
	for i in range(0,len(lis_pred)):
		lis_usu.append("_") # Se genera una lista de elementos '_' cuya cantidad es igual a la de elementos de la palabra (su lista) a acertar
	lis_usu_tex=""
	
	for k in range(0,len(lis_usu)):
		lis_usu_tex = lis_usu_tex + lis_usu[k] + "," # los guiones bajos de la palabra generada se separan por ',')
	lis_usu_tex = lis_usu_tex.replace(","," ") # Se reemplazan las "," por espacios	
	
	vidas = 5 # Inicializar cantidad de vidas
	intentos = 0 # Inicializar cantidad de intentos	
	
	while True and vidas>0:
		
		ventana.fill((0,0,255))
		
		texto=mi_fuente.render(lis_usu_tex,0,(255,255,255)) #13. Crear objeto texto
		ventana.blit(texto,(60,30))#13. Mostrar objeto texto en ventana
		texto_vidas=mi_fuente.render("Vidas: "+str(vidas),0,(255,255,255)) #13. Crear objeto texto
		ventana.blit(texto_vidas,(60,80))#13. Mostrar objeto texto en ventana
		texto_intentos=mi_fuente.render("Intentos: "+str(intentos),0,(255,255,255)) #13. Crear objeto texto
		ventana.blit(texto_intentos,(60,120))#13. Mostrar objeto texto en ventana
		
		# for i in range(0,len(lis_pred)):
			# lineaInicia=(60+a*i,80)
			# lineaTermina=(100+a*i,80)
			# colorLinea=(255,255,255)
			# pygame.draw.line(ventana,colorLinea,lineaInicia,lineaTermina,8)
		
		# texto_aviso=mi_fuente.render("La palabra tiene: "+str(len(lis_pred))+" letras",0,(255,255,255)) #13. Crear objeto texto
		# ventana.blit(texto_aviso,(100,100))#13. Mostrar objeto texto con segundos en ventana
	
			
		for evento in pygame.event.get(): #2.Revisa lista de eventos predefinidos en pygame
			if evento.type==QUIT: #2.Evento quit
				pygame.quit() #2.Deja de ejecutarse el presente
				sys.exit() #2.Se cierra ventana
			elif evento.type in (pygame.KEYDOWN, pygame.KEYUP):
				let_usu=pygame.key.name(evento.key)
				if evento.type == pygame.KEYDOWN:
					print("letra "+let_usu+" presionada")
				elif evento.type == pygame.KEYUP:
					print("letra "+let_usu+" soltada") #En este momento la tecla ha sido presionada y soltada
					for i in range(0,len(lis_pred)):
						if let_usu == lis_pred[i]:
							lis_usu[i]=lis_pred[i]
					if let_usu not in lis_pred:
						texto_aviso=mi_fuente.render("Lo siento, la letra "+let_usu+" no está en la palabra",0,(255,255,255)) #13. Crear objeto texto
						ventana.blit(texto_aviso,(100,200))#13. Mostrar objeto texto_aviso en ventana
						pygame.time.wait(2000) # 28/03/2018 Por qué no funciona?
						vidas = vidas - 1 
					intentos=intentos+1
						
							
		lis_usu_tex=" ".join(lis_usu) # Se crea cadena de lo logrado (los caracteres están espaciados)
				# texto=mi_fuente.render(lis_usu_tex+" ",0,(255,255,255)) #13. Crear objeto texto
				# ventana.blit(texto,(60,30))#13. Mostrar objeto texto en ventana
											
		if lis_usu == lis_pred: # Cuando la lista de lo logrado sea igual a la lista de la palabra a acertar, entonces se termina el juego
			texto_aviso=mi_fuente.render("Has terminado en "+str(intentos)+" intentos, y te quedaron "+str(vidas)+" vidas. Felicidades!",0,(255,255,255)) #13. Crear objeto texto
			ventana.blit(texto_aviso,(100,200))#13. Mostrar objeto texto en ventana
			pygame.time.wait(2000) # 28/03/2018 Por qué no funciona?
			vidas = 0 # Al terminar el if se rompe el ciclo de comprobación de cantidad de comprobación de vidas para ir al ciclo de comprobación de continuar

		
	
		pygame.display.update() #2.Se actualiza o refresca ventana	
	