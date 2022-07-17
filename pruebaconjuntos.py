def inserta(lista, elemento, indice): #Inserta un elemento en la posición indice de una lista
	listaConInsercion=lista[:indice]+[elemento]+lista[indice:]
	return listaConInsercion

lst=['r','s','t']
i=2
elem='p'
lstCnInsc=inserta(lst,elem,i)
print("Lista con elemento insertado:",lstCnInsc)