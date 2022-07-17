#Recordemos que en este módulo están todos las funciones de interacción.
import S6Red as Red

Red.mostrar_bienvenida()
nombre = Red.obtener_nombre()
print("Hola ", nombre, ", bienvenido a PETBOOK")

if Red.existe_archivo(nombre+".user"):
	print(nombre, "\nya tienes un perfil", "\ntus datos son:")
	(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos, muro)=Red.leer_datos(nombre)
	
else:
	print(nombre, " te invitamos a completar un perfil")
	Red.obtener_edad
	Red.obtener_estatura
	Red.obtener_sexo
	Red.obtener_pais
	Red.obtener_lista_amigos
	(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos)=Red.obtener_datos()
	muro=[]
	Red.grabar_datos(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos, muro)

Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos) #Se muestran los datos del usuario, sea nuevo o recientemente creado

opcion=1 #Se inicializa variable para ciclo de menú
while opcion!=0:
	opcion=Red.opcion_menu()
	if opcion==1:
		mensaje=Red.obtener_mensaje()
		Red.publicar_mensaje(nombre, amigos, mensaje, muro) #Se necesita la lista muro para agregar mensajes a ella. Recordar que muro es una lista llena si el usuario ya existe o una lista vacía si el usuario es nuevo
	elif opcion==2:
		Red.mostrar_muro(muro) #Recordar que muro es una lista llena si el usuario ya existe o una lista vacía si el usuario es nuevo
	elif opcion==3:
		Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos)
	elif opcion==4:
		Red.obtener_edad
		Red.obtener_estatura
		Red.obtener_sexo
		Red.obtener_pais
		Red.obtener_lista_amigos
		(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos)=Red.obtener_datos()
		Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos)
		# Red.grabar_datos(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos) #Esta opción no se debe ejecuar acá, pues se eliminaría los mensajes existentes
	elif opcion==5:
		nombre=input("¿Cuál es tu nombre?")
		if Red.existe_archivo(nombre+".user"):
			print("hola ", nombre, "\n ya tienes un perfil", "\n tus datos son:")
			(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos, muro)=Red.leer_datos(nombre)
			Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos)
		else:
			print("no existe este nombre de usuario!")
	elif opcion==6:
		Red.agregar_amigo(amigos)
	elif opcion==7:
		Red.mostrar_estados_amigos(amigos)
	elif opcion==0:
		Red.grabar_datos(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos, muro)
		print("Has salido de PETBOOK. ¡Gracias por visitarnos!")
		
	
	

