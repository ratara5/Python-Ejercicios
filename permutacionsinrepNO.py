# Halla todas las permutaciones sin repetición de los elementos de una lista (02/04/2018 hasta el momento, solo de 5 elementos)
# ... 02/04/2018 Agregar todas las listas a una matriz y luego borrar las repetidas?
# ... Funciona bien, hasta la mitad del arreglo

import math

# 1 Conformar lista
# elem=0
# lista=[]
# while elem!="#":
	# elem=input("Ingrese elemento o '#' para terminar: ")
	# if elem!="#":
		# lista.append(elem)
# print("La lista original es: ", lista) #Supuesto '[A,B,C,D]'
lista=['A','B','C','D']

# 2 Todo lo siguiente se repite tantas veces como elementos tiene la lista
# 2 Arreglos con el primer elemento sin variar: Hay (n-1)! arreglos...
# ...Arreglos con el segundo elemento sin variar: Hay (n-2)! arreglos...
# ...Arreglos con el tercer elemento sin variar: Hay (n-3)! arreglos...???

l=len(lista)
listaNueva=[]
lisNew=[]
for i in range (0,l):
	listaNueva.append('_')
print(listaNueva)


def inserta(elemento,lista,indice)
	listaNueva=lista[:indice]+[elemento]+lista[indice:]
	return listaNueva


		
	



# for m in range(0,l):
	# listaNueva[0]=lista[m]
	# for n in range(1,l):
		# listaNueva[1]=lista[n]
		# for p in range (2,l):
			# if listaNueva[1]!=lista[p]:
				# listaNueva[2]=lista[p]
			# for r in range (3,l):
				# if listaNueva[2]!=lista[r]:
					# listaNueva[3]=lista[r]
				# print(listaNueva)
					
		
		# for n in range(2,l):
			# for j in range (0,int(math.factorial(l-3))): # Repetir cada letra desde la tercera (l-3)! veces
				# listaNueva[2]=lista[n]
			
			# Después de pasar por el elemento central...
				# for p in range (3,l):
					# if lista[p]!=listaNueva[2]:
						# for i in range (0,int(math.factorial(l-4))):
							# listaNueva[3]=lista[p]
					# print(listaNueva) # Listas de arreglos aparecen repetidas
						
		
		# for m in range (2, int(math.factorial(l-3))):
			# listaNueva[m]=lista[2] # ...Arreglos con el tercer elemento sin variar: Hay (n-3)! arreglos...
			
			# listaNueva[3]=lista[3]
	
			
					
	
		


	

