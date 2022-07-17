# AHORCADO
# Se predefine en el programa un nombre y se le da al usuario la opción de introducir letras para ver cuáles coinciden con las de esa palabra...
# ...Se dará indicación de ello...
# ...Si la palabra es completada por el usuario en una cantidad de vidas menor o igual a la establecida, habrá ganado, sino morirá 'ahorcado'
import random, os # random para sacar palabra aleatorio// os para limpiar ventana

ban_pal=["genesis", "exodo", "levitico", "deuteronomio", "numeros", "josue", "jueces", "rut", "esdras", "nehemias", "cronicas", "samuel", "reyes", "ester", "job", "salmos"]
empezar="s"
while empezar=="S" or empezar=="s":
	os.system('cls') # limpiar ventana
	i=len(ban_pal)-1 # ya que randint busca entre los dos extremos del intervalo INCLUIDOS
	j=random.randint(0,i) # generar aleatorio
	pal_ban_pred=ban_pal[j] # seleccionar elemento de indice 'j' como palabra a acertar
	# print(pal_ban_pred)
	pal_pred=""
	for k in range(0,len(pal_ban_pred)):
		pal_pred=pal_pred+pal_ban_pred[k]+"," # las letras de la palabra generada se separan por ','
	pal_pred=pal_pred.rstrip(",") # Se elimina la última ',' de la derecha
	# print(pal_pred)
	lis_pred=pal_pred.split(",") # Se convierte la palabra en una lista en la que cada elemento es una letra en su posición
	# print(lis_pred)
	print("La palabra tiene "+str(len(lis_pred))+" letras")
	lis_usu=[]
	for i in range(0,len(lis_pred)):
		lis_usu.append("_") # Se genera una lista de elementos '_' cuya cantidad es igual a la de elementos de la palabra (su lista) a acertar
	# lis_usu_ini=lis_usu
	vidas=5 # Inicializar cantidad de vidas
	intentos=0 # Inicializar cantidad de intentos
	while vidas>0:
		long_let_usu=1
		while long_let_usu==1: # El usuario no debe ingresar más de una letra (MEJORA: No válidos caractéres especiales)
			let_usu=input("Ingresa letra: ")
			long_let_usu=len(let_usu) 
			if long_let_usu>1: 
				print("Solo puedes ingresar una letra")
			else: # Si el usuario solo entra una letra, lo cual es lo adecuado
				for i in range(0,len(lis_pred)):
					if lis_pred[i]==let_usu:
						print("Muy bien! La letra '"+let_usu+"' está en la palabra"+", en la posición "+str(i))
						lis_usu[i]=lis_pred[i]
						
				if let_usu not in lis_pred:
					print("Lo siento. La letra '"+let_usu+"' no está en la palabra")
					long_let_usu=2 # Al terminar el if se rompe el ciclo de comprobación de cantidad de letras ingresadas por usuario para ir al ciclo de comprobación de vidas
					vidas=vidas-1 
					print("Te quedan "+str(vidas)+" vidas")
				print("".join(lis_usu)) # Se imprime la lista de lo logrado en forma de cadena
				intentos=intentos+1
				if lis_usu==lis_pred: # Cuando la lista de lo logrado sea igual a la lista de la palabra a acertar, entonces se termina el juego
					print("Has terminado en "+str(intentos)+" intentos, y te quedaron "+str(vidas)+" vidas. Felicidades!")
					long_let_usu=2 # Al terminar el if se rompe el ciclo de comprobación de cantidad de letras ingresadas por usuario para ir al ciclo de compobación de vidas
					vidas=0 # Al terminar el if se rompe el ciclo de comprobación de cantidad de comprobación de vidas para ir al ciclo de comprobación de continuar
	empezar=input("¿Deseas empezar de nuevo? Si:'S' -> ")
				
					