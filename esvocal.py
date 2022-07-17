# Verificar si un caracter es vocal

def es_vocal(caracter):
	vocales=["a", "e", "i", "o", "u"]
	for vocal in vocales:
		if caracter==vocal:
			# print("el caracter introducido es una vocal")
			return True
	return False

def intro():
	carac=input("Introduce un caracter ")
	return carac

caract=intro()
verifica=es_vocal(caract)
print("El caracter introducido es una vocal ", verifica)