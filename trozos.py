#  Extraer de una tupla, "n" elementos desde una posición "p" ("p" también se extrae y se cuenta dentro de los "n" elementos). Luego, decir 'hola' a cada elemento extraído.

def trocear(tupla,p,n):
	if p+n<=len(tupla):
		for i in range(p,p+n):
			print("hola",tupla[i])
	else:
		print("la cantidad de elementos que se imprimirán debe ser menor o igual que",len(tupla)-p)

def entregartupla():
	cadena=input("ingrese los nombres separados por ',' sin espacios: ")
	lista=cadena.split(",")
	tup=tuple(lista)
	posicion=int(input("ingrese la posición desde la cual se imprimirá la tupla: "))
	numero=int(input("ingrese la cantidad de elementos que se imprimirán de la tupla (posición incluida): "))
	return tup, posicion, numero

(tupl,pos,num)=entregartupla()
trocear(tupl,pos,num)