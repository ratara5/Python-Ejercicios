import os #Contiene función para saber si existe archivo

def mostrar_bienvenida(): 
    print("Bienvenido a Petbook... ")
    print("""              _                  __
               __ ___.                  __    
______   _____/  |\_ |__   ____   ____ |  | __
\____ \_/ __ \   __\ __ \ /  _ \ /  _ \|  |/ /
|  |_> >  ___/|  | | \_\ (  <_> |  <_> )    < 
|   __/ \___  >__| |___  /\____/ \____/|__|_ \
|__|        \/         \/                   \/
""")

def obtener_nombre():
    nombre = input("Para empezar, dime cómo te llamas. ")
    return nombre

def obtener_edad():
    agno = int(input("Para preparar tu perfil, dime en qué año naciste. "))
    return 2018-agno-1

def obtener_estatura():
    estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dímelo en metros. "))
    metros = int(estatura)
    centimetros = int( (estatura - metros)*100 ) #Al valor decimal se le restan las unidades y se multiplican por 100 para conocer los centímetros
    return (metros, centimetros)

def obtener_sexo():
    sexo = input("Por favor, ingresa tu sexo (M=Masculino, F=Femenino): ")
    while sexo != 'M' and sexo != 'F':
        sexo = input("Por favor, ingresa tu sexo (M=Masculino, F=Femenino): ") #Mientras no se digiten M o F, se sigue desplegando la solicitud de género
    return sexo

def obtener_pais():
    pais = input("Indica tu país de nacimiento: ")
    return pais

def obtener_lista_amigos():
	lista = input("Muy bien. Finalmente, escribe una lista con los nombres de tus amigos separados solo por comas (,). ")
	amigos=lista.split(",") #Se convierte el texto ingresado por el usuario en una lista (o variable tipo lista)
	return amigos

def obtener_datos():
	n = obtener_nombre()
	e = obtener_edad()
	(em, ec) = obtener_estatura()
	se = obtener_sexo()
	pa = obtener_pais()
	a = obtener_lista_amigos()
	return (n,e,em,ec,se,pa,a)

def mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos):
	print("--------------------------------------------------")
	print("Nombre: ", nombre)
	print("Edad: ", edad)
	print("Estatura (m): ", estatura_m)
	print("Estatura (cm): ", estatura_cm)
	print("Sexo: ", sexo)
	print("País: ", pais)
	print("Amigos: ", len(amigos))
	print("--------------------------------------------------")

def opcion_menu():
	print("Acciones disponibles:")
	print("  1. Escribir un mensaje")
	print("  2. Mostrar mi muro")
	print("  3. Mostrar los datos de perfil")
	print("  4. Actualizar el perfil de usuario")
	print("  5. Cambiar de usuario")
	print("  6. Agregar un amigo") 
	print("  7. Ver estados de amigos")
	print("  0. Salir")
	op = int(input("Ingresa una opción: "))
	while op < 0 or op > 7:
		print("No conozco la opción que has ingresado. Inténtalo otra vez.") #Mientras no se digite un número entre 0 o 5, se sigue desplegando la solicitud de opción4
		op = int(input("Ingresa una opción: "))
	return op

def obtener_mensaje():
    mensaje = input("Ahora vamos a publicar un mensaje. ¿Qué piensas hoy? ")
    return mensaje

def mostrar_mensaje(origen, mensaje):
	print("--------------------------------------------------")
	print(origen+":", mensaje)
	print("--------------------------------------------------")

#Publica un mensaje en el muro personal y en el de los amigos
def publicar_mensaje(origen, amigos, mensaje, muro):
	print("--------------------------------------------------")
	print(origen, "dice: ", mensaje)
	print("--------------------------------------------------")
	muro.append(mensaje) #Se agrega cada mensaje a la lista muro propia del archivo activo sea que esta exista o no
	for amigo in amigos:
		if existe_archivo(amigo+".user"):
			archivo=open(amigo+".user", "a") #Se abre archivo para escribir en nueva linea al final
			archivo.write("@"+origen+" dice: "+mensaje+"\n") #Se escribe cada entrada en el archivo del usuario. Si el MARCADOR @ está presente, el mensaje lo escribió un amigo del usuario y no el mismo usuario.
			archivo.close()	
	
#Muestra todos los mensajes recibidos
def mostrar_muro(muro): 
	print("-------MURO ("+str(len(muro))+" mensajes)---------")
	for entrada in muro: #entrada es un elemento de la lista muro
		print(entrada) #Se imprime cada entrada de la lista muro
	print("--------------------------------------------------")

def agregar_amigo(amigos):
	print("AGREGA UN NUEVO AMIGO!")
	if amigos[0]=="": 
		amigos.pop(0) #Si no hay ningún amigo, entonces eliminar el elemento vacío que se genera por esa razón en la pimera posición
	alias=input("ingresa el nombre de tu amigo :")
	amigos.append(alias)
	print("tus amigos son: ", amigos)

#Muestra el último estado propio del usuario (personal) de cada uno de los archivos de usuarios de los amigos
def mostrar_estados_amigos(amigos): 
	for amigo in amigos:
		if existe_archivo(amigo+".user"): #Se abre el archivo de usuario del amigo
			archivo_usuario=open(amigo+".user", "r")
			archivo_usuario.readline().rstrip() 
			archivo_usuario.readline().rstrip()
			archivo_usuario.readline().rstrip()
			archivo_usuario.readline().rstrip()
			archivo_usuario.readline().rstrip()
			archivo_usuario.readline().rstrip()
			archivo_usuario.readline().rstrip() #Se han recorrido todas las lineas de el archivo de usuario hasta llegar a la primera linea de mensajes
			mensaje=archivo_usuario.readline().rstrip() #Este es el primer mensaje en el archivo del usuario	
			muro=[]
			mensaje=archivo_usuario.readline().rstrip()		
			while mensaje!="":
				muro.append(mensaje)
				mensaje=archivo_usuario.readline().rstrip() #Se toma cada mensaje del archivo del usuario y se almacena como elemento en la LISTA muro
			# print("este es el muro de: ", amigo, "/n", muro)
			propios_muro=[] #lista auxiliar en la que se almacenarán los estados personales
			for mensaje in muro:
				if mensaje[0]!="@":
					propios_muro.append(mensaje)
					# print(propios_muro)
					# print(len(propios_muro))
			if len(propios_muro)==0:
				print(amigo, "dice: ", propios_muro[len(propios_muro)]) #se muestra el último elemento de la lista auxiliar
			else:
				print(amigo, "dice: ", propios_muro[len(propios_muro)-1]) #se muestra el último elemento de la lista auxiliar
			
def existe_archivo(ruta):
    return os.path.isfile(ruta)
	
def leer_datos(nombre):
	archivo_usuario=open(nombre+".user", "r")
	print()
	print("--------------------------------------------------")
	nombre=archivo_usuario.readline().rstrip()
	edad=int(archivo_usuario.readline().rstrip())
	estatura_m=int(archivo_usuario.readline().rstrip())
	estatura_cm=int(archivo_usuario.readline().rstrip())
	sexo=archivo_usuario.readline().rstrip()
	pais=archivo_usuario.readline().rstrip()
	amigos=archivo_usuario.readline().rstrip().split(",")
	muro=[]
	mensaje=archivo_usuario.readline().rstrip()		
	while mensaje!="":
		muro.append(mensaje)
		mensaje=archivo_usuario.readline().rstrip() #Se toma cada mensaje del archivo del usuario y se almacena como elemento en la lista muro
	archivo_usuario.close()
	return(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos, muro)
	
def grabar_datos(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos, muro):
	archivo_usuario = open(nombre+".user", "w")
	print()
	print("Guardando perfil en ",nombre+".user")
	print()
	archivo_usuario.write(nombre+"\n")
	archivo_usuario.write(str(edad)+"\n")
	archivo_usuario.write(str(estatura_m)+"\n")
	archivo_usuario.write(str(estatura_cm)+"\n")
	archivo_usuario.write(sexo+"\n")
	archivo_usuario.write(pais+"\n")
	archivo_usuario.write(",".join(amigos)+"\n")
	for mensaje in muro:
		archivo_usuario.write(mensaje+"\n") #Se guarda cada mensaje de la lista muro en el archivo del usuario
	archivo_usuario.close()	