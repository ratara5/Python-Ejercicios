def opciones():
	print()
	print("Acciones disponibles:")
	print("  1. Escribir un mensaje público")
	print("  2. Escribir un mensaje solo a algunos amigos")
	print("  3. Mostrar los datos de perfil")
	print("  4. Actualizar el perfil de usuario")
	print("  0. Salir")
	op = int(input("Ingresa una opción: "))
	while op<0 or op>4:
		print("Acciones disponibles:")
		print("  1. Escribir un mensaje público")
		print("  2. Escribir un mensaje solo a algunos amigos")
		print("  3. Mostrar los datos de perfil")
		print("  4. Actualizar el perfil de usuario")
		print("  0. Salir")
		op = int(input("Ingresa una opción: "))
	return op
