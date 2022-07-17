def solicitarperfil():
	print()
	# Solicitud de nombre
	no = input("¿Cómo te llamas? ")
	print()
	print("Hola ", no, ", estás en PETBOOK")
	print()
	# Cálculo de edad
	agno = int(input("¿En qué año naciste? "))
	ed = 2017-agno-1
	print()
	# Cálculo de estatura
	es = float(input("¿Cuánto mides? Dímelo en metros. "))
	es_m = int(es)
	es_cm = int( (es - es_m)*100 )
	# Cantidad de amigos
	nu_am = int(input("¿Cuántos amigos tienes? "))
	# Género
	ge=str(input("¿Cúal es tu género? (Femenino, Masculino). "))
	# País
	pa=str(input("¿De qué país eres?"))
	return (no,ed,es_m,es_cm,nu_am,ge,pa)
