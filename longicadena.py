# Determinar la longitud de una cadena

def longitud(cadena):
	i=0
	while cadena[i]!="@":
		i=i+1
	print("la longitud de la cadena ingresada es: ", i)

cdn_prev=input("Escribe la cadena (no uses '@'). ")
cdn=cdn_prev+"@"
longitud(cdn)
