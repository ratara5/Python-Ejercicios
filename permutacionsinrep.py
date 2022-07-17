def inserta(elemento,lista,indice):
	listaNueva=lista[:indice]+[elemento]+lista[indice:]
	return listaNueva

# lisNew=inserta("A",[2,5,6],1)
# print(lisNew)

def insertamultiple(listaAPermutar):
	for i in range(0,len(listaAPermutar)):
		elem=listaAPermutar[i]
		lisNew=inserta(elem,listaAPermutar,i)
		print(lisNew)

lisAPer=['A','B','C','D','E']
insertamultiple(lisAPer)

	
			
					
	
		


	

