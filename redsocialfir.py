# Proyecto RED SOCIAL
print("Bienvenido a ... ")
print("""              _                  __
               __ ___.                  __    
______   _____/  |\_ |__   ____   ____ |  | __
\____ \_/ __ \   __\ __ \ /  _ \ /  _ \|  |/ /
|  |_> >  ___/|  | | \_\ (  <_> |  <_> )    < 
|   __/ \___  >__| |___  /\____/ \____/|__|_ \
|__|        \/         \/                   \/
""")
# Preguntar nombre y saludar
nombre=input("Para empezar, dime cómo te llamas. ")
print()
print("Hola", nombre, "bienvenido(a) a PETBOOK")
print()
# Preguntar año de nacimiento e informar edad aproximada
agno=int(input("En qué año naciste?"))
edad_aprox=2018-agno-1
print()
print("Tienes aproximadamente ", edad_aprox, " años de edad.")
print()
# Preguntar estatura en metros e informar estatura en centímetros
estatura=float(input("Por favor, dime cuánto mides en metros (usa el punto (.) para decimales) "))
estatura_m=int(estatura)
estatura_cm=int((estatura-estatura_m)*100)
print()
print("Tu estatura es ", estatura_m, " metro(s) con ", estatura_cm, " centímetros")
print()
# Preguntar número de amigos
num_amigos=int(input("Finalmente, cuántos amigos tienes? "))
print()
# Escribir resumen
print("Excelente ", nombre, ". Ahora, podemos crear tu perfil con estos datos.")
print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
print("Nombre: ", nombre)
print("Edad: ", edad_aprox)
print("Estatura: ", estatura_m, " metro(s) con ", estatura_cm, " centímetros")
print("Amigos: ", num_amigos)
print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
print("Gracias por la información. Esperamos que disfrutes con PETBOOK")
# Solicitar mensaje de prueba
mensaje=input("Ahora, vamos a publicar tu primer mensaje. ¿Qué piensas hoy?: ")
print()
print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
print(nombre, " dice: ", mensaje)
print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
print()
# Solicitar más datos e informar todo el perfil
sexo=input("¿Cuál es tu sexo (femenino ó masculino)? ")
telefono=input("¿Cuál es tu número de teléfono? ")
ciudad=input("¿En qué ciudad vives? ")
pais=input("¿De qué país eres? ")
direccion=input("¿Cuál es tu dirección física? ")
print()
print("De nuevo, gracias! Los siguientes son tus datos: ")
print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
print("Nombre: ", nombre)
print("Edad: ", edad_aprox)
print("Estatura: ", estatura_m, " metro(s) con ", estatura_cm, " centímetros")
print("Amigos: ", num_amigos)
print("Sexo: ", sexo)
print("Teléfono: ", telefono)
print("Vives en la ", direccion, " de ", ciudad, ", ", pais)
print("Sigue disfrutando de PETBOOK")
print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
#Variable boole y ciclo para que el usuario siga activo
continuar_opcion=True
while continuar_opcion==True:
	print()
	print("Escribir mensaje: 1")
	print("Modificar perfil: 2")
	print("Salir: 3")
	opcion=str(input())
	if opcion=="1":
		continuar_mensaje=True
		while continuar_mensaje==True:
			escribir_mensaje=str(input("¿Deseas escribir un mensaje? (S/N)"))
			if escribir_mensaje=="S" or escribir_mensaje=="s" or escribir_mensaje==" ":
				mensaje=input("Vamos a publicar algo. ¿Qué piensas hoy? ")
				print()
				print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
				print(nombre, " dice: ", mensaje)
				print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
			elif escribir_mensaje=="N" or escribir_mensaje=="n":
				continuar_mensaje=False
			else:
				continuar_mensaje=True
	elif opcion=="2":
		nombre=input("Cómo te llamas. ")
		agno=int(input("En qué año naciste?"))
		estatura=float(input("Cuánto mides en metros (usa el punto (.) para decimales) "))
		num_amigos=int(input("Cuántos amigos tienes? "))
		sexo=input("¿Cuál es tu sexo (femenino ó masculino)? ")
		telefono=input("¿Cuál es tu número de teléfono? ")
		ciudad=input("¿En qué ciudad vives? ")
		pais=input("¿De qué país eres? ")
		direccion=input("¿Cuál es tu dirección física? ")
		print()
		print("De nuevo, gracias! Los siguientes son tus datos: ")
		print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
		print("Nombre: ", nombre)
		print("Edad: ", edad_aprox)
		print("Estatura: ", estatura_m, " metro(s) con ", estatura_cm, " centímetros")
		print("Amigos: ", num_amigos)
		print("Sexo: ", sexo)
		print("Teléfono: ", telefono)
		print("Vives en la ", direccion, " de ", ciudad, ", ", pais)
		print("Sigue disfrutando de PETBOOK")
		print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")	
	else:
		continuar_opcion=False
		


