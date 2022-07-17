# Halla la suma y la multiplicación de los  elementos de una lista

def sumalista(lista):
	lista_num=lista.split(",")
	print(lista)
	suma=0
	for i in range(0, len(lista_num)):
		suma=suma+int(lista_num[i])
	print("la suma de los elementos es ",suma)
	proceso()
	
def multiplista(lista):
	lista_num=lista.split(",")
	print(lista)
	multip=1
	for i in range(0, len(lista_num)):
		multip=multip*int(lista_num[i])
	print("la multiplicación de los elementos es ",multip)
	proceso()
	
	
def obtenerdatos():
	lst=input("ingresa la lista de números (separados por ',' sin espacios): ")
	print(lst,type(lst))
	return lst
	
def seleccionoperacion(lt):
	op=3
	while op<0 or op>2:
		op=int(input("¿Qué operación deseas realizar? Escoge una opcion:\n1:   suma\n2:    multiplicación"))
		if op==1:
			sumalista(lt)
		elif op==2:
			multiplista(lt)
		else:
			op=3
			
def proceso():
	lis=obtenerdatos()
	seleccionoperacion(lis)

proceso()

