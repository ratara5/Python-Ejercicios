# Operaciones con elementos de conjuntos

c=[2 ** x for x in range(10)] # Lista de potencias de 2. Exponentes de 0 a 9
d=[n for n in range(1, 101) if n % 7 == 0 or n % 10 == 7] # Lista de números múltiplos de 7 y terminados en 7
p=[(camisa,pantalon) 
	for camisa in ['amarilla', 'azul', 'roja'] 
	for pantalon in ['negro', 'gris', 'beige']] # Producto cartesiano de camisas y pantalones. Todos los conjuntos.
print(p)
t=[(a, b, c)
    for a in range(1, 20)
    for b in range(1, 20)
    for c in range(1, 20)
    if a ** 2 + b ** 2 == c ** 2] # Ternas pitagóricas (repetidas)
t=[(a, b, c)
    for a in range(1, 20)
    for b in range(1, 20)
    for c in range(1, 20)
    if a ** 2 + b ** 2 == c ** 2 and a<b and b<c] # Ternas pitagóricas (sin repetir)
print(t)
r = []
for a in range(1, 20):
    for b in range(a + 1, 20):
        for c in range(b + 1, 20):
            if a ** 2 + b ** 2 == c ** 2:
                r.append((a, b, c)) # Igual al último t impreso
# [[1,0,0],[0,1,0],[0,0,1]]
i3=[[a,b,c]
	for a in range(2)
	for b in range(2)
	for c in range(2)
	if a+b+c==1]
print(i3) # Matriz I(3) pero con filas desordenadas
id3=[[fila,columna]
	 for fila in range(2)
	 for columna in range(2)
	 if fila==columna]
print("id3: ",id3) # NO
identidad3=[[(1 if fila==columna else 0) for columna in range(3)]
			 for fila in range(3)]
print(identidad3) # Matriz I(3) CORRECTA

def identidad_n(n):
	return print([[(1 if fila==columna else 0) for columna in range(n)]
					for fila in range(n)]) # Matriz I(n) CORRECTA. También válida
	
def identidad_n(n):
	matrizIdentidad_n=[[(1 if fila==columna else 0) for columna in range(n)]
					for fila in range(n)] # Matriz I(n) CORRECTA
	return matrizIdentidad_n
	

matrizIdentidad_6=identidad_n(6)
print(matrizIdentidad_6)

lista=['x','y','z','w']
print(lista[:-2])

punto={'x':1,'y':2,'z':3} # Diccionario
print(punto['x'])

materias = {}
materias["lunes"] = [6103, 7540]
materias["martes"] = [6201]
materias["miércoles"] = [6103, 7540]
materias["jueves"] = []
materias["viernes"] = [6201]

print(materias)
print(materias.get("domingo", 'no está'))
for dia in materias:
   print(dia, ":", materias[dia])
   
if 'viernes' in materias:
   print(materias['viernes'])
  
  
def potencia(c): # Hallar conjunto Potencia
	if len(c) == 0:
		return [[]]
	a=c[:-1]
	r = potencia(a)
	p=r+ [s + [c[-1]] for s in r]
	print(p)
	return p

arreglo=potencia([1,2,5,10]) # Imprimir suma de elementos de subconjuntos del conjunto potencia
for t in arreglo:
	print("Total dinero para arreglo {} es: ${}".format(t, sum(t)))

	
def imprime_ordenado(d):# Imprimir organizados subconjuntos de un conjunto de subconjuntos (lista de listas). Primero por longitud y luego por orden alfabético. 
	for e in sorted(d, key=lambda s: (len(s), s)): 
		print(e)
		
don=[[1],[1,2],[1,3],[3,4,5],[4,5]]
imprime_ordenado(don)

	
def combinaciones(conjunto,n): # Hallar arreglos de combinaciones de n elementos de un conjunto.
	conjunto_potencia=potencia(conjunto) # Se encuentra conjunto potencia
	combis=[] # Se crea lista para guardar listas de combinaciones
	for i in range (0,len(conjunto_potencia)):
		if len(conjunto_potencia[i])==n:
			combinacion=[conjunto_potencia[i]]
			combis=combis+combinacion
	return combis

cnj=['cereza','chocolate','fresa','nuez','vainilla']
num=3
cmbs=combinaciones(cnj,num)
print(cmbs)
imprime_ordenado(cmbs)

def inserta(lista, elemento, indice): #Inserta un elemento en la posición indice de una lista
	listaConInsercion=lista[:indice]+[elemento]+lista[indice:]
	return listaConInsercion

lst=['r','s','t']
i=2
elem='p'
lstCnInsc=inserta(lst,elem,i)
print("Lista con elemento insertado:",lstCnInsc)

def inserta_multiple(lista,elemento): #Inserta un elemento en todas las posiciones de una lista. Devuelve una lista de listas
	listaDeListas=[]
	for i in range(0,len(lista)+1):
		listaConIncersion=inserta(lista,elemento,i)
		listaDeListas=listaDeListas+[listaConIncersion]
	return listaDeListas # Devuelve lista de listas con insercion múltiple

lst=['r','s','t']
i=2
elem='p'
lstDLst=inserta_multiple(lst,elem)
print("Lista de listas:", lstDLst)

	
def permutaciones(conjunto): # Hallar arreglos de permutaciones de un conjunto. Sin repetición.
	if len(conjunto)==0: # Caso base
		return [[]]
	a=conjunto[1:] # Elementos de conjunto sin el primero
	pr=permutaciones(a) # Llamada recursiva a la función permutaciones para el conjunto sin su primer elemento
	todasPermutaciones=[] # Se genera lista vacía para ir guardando las listas de permutaciones
	for s in pr: # Para todos los elementos en pr...
		todasPermutaciones=todasPermutaciones+inserta_multiple(s,conjunto[0]) #...hacer listas con la inserción del primer elemento del cpmjunto
	return todasPermutaciones # Se retorna lista con todas las listas de permutaciones
	
cnj=['a','b','c','d'] # Se evalúa desempeño de funcion permutaciones
tPrms=permutaciones(cnj)
print(tPrms)
imprime_ordenado(tPrms)

# Hay permutaciones con listas obtenidas por combinaciones
def permutaciones(c, n):
    return sum([permuta(s)
                for s in combinaciones(c, n)],
               [])
# Permutaciones con repetición?