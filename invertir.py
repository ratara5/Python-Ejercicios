def invercadena(cadena):
	cadena_inv=""
	for i in range(1, len(cadena)+1):
		cadena_inv=cadena_inv+cadena[-1*i]
	print(cadena_inv)

cad=str(input("introduce la cadena de texto: "))
invercadena(cad)