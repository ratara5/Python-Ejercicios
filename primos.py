# Todo este programa permite determinar qué números de una lista son primos

# Determinar si un número es primo
def primo(num): #4. Definir función
	num=int(num) #4.1 Convertir parámetro de tipo str a tipo int
	indicador=True #4.2 Variable que por defecto indica que el número es primo
	divisores=[] #4.3 Crear lista vacía para guardar
	for i in range(1,num+1): #4.4 Para cada natural desde 1 hasta el parámetro...
		if num%i==0: #... comparar mediante la función módulo el parámetro y el natural del ciclo para ver si el segundo es divisor del primero...
			# print(num, "es divisible por ", i) # Instrucción no ejecutada
			if i!=num and i!=1: #...si el natural del ciclo no es el parámetro ni el uno (1)...
				indicador=False #...cambiar el valor de la variable que indica si el número es primo...
				divisores.append(i) #...agregar en una lista el natural que es divisor del parámetro
		# else: # Instrucción no ejecutada
			# print(num, "NO es divisible por ", i) # Instrucción no ejecutada
	divisores.insert(0,1) #4.5 Agregar en la primera posición de una lista el natural 1 (uno) que es divisor de cualquier parámetro
	divisores.append(num) #4.6 Agregar en una lista el parámetro, pues es divisor de sí mismo
	print("¿El número ", num,"es primo?: ", indicador) #4.7 Mostrar si el parámetro es primo o no es primo
	print("Los divisores de ",num," son: ",divisores) #4.8 Mostrar los divisores del parámetro
	if indicador==True: #4.9 Si el número (parámetro) es primo...
		return num #...la función retorna ese número. Ir a fin de 3.5...

# numero=int(input("ingresa el número: "))
# primo(numero)

# Determinar qué números de una lista son primos
def primolista(lista): #3.1 Definir función
	listaprimos=[] #3.2 Crear lista vacía para guardar
	nuevalistaprimos=[] #3.3 Crear lista vacía para guardar
	for numero in lista: #3.4 Para cada elemento de la lista ingresada en el primer paso...
		numprimo=primo(numero) #3.5 ejecutar la función primo siendo el argumento dicho elemento. Ir a 4... La variable numprimo toma el valor del retorno de la función primo
		listaprimos.append(numprimo) #5. Agregar en una lista la variable numprimo. ATENCIÓN: numprimo toma el valor None cuando no hay retorno de la función primo, es decir, cuando el número no es primo 
	for i in range(0,len(listaprimos)): #6. Llenar nueva lista a partir de la lista listaprimos en la que no aparezcan los valores None. Para cada posición...
		if listaprimos[i]!=None: #...Si el valor es diferente de None  
			nuevalistaprimos.append(listaprimos[i]) #...agregar dicho valor a la nueva lista
	print("Los números primos de la lista ingresada son: ",nuevalistaprimos) #7. Informar al usuario en formato lista, cuáles son los primos de la lista ingresada
		
cadena=input("introduce la lista de números separados por ',' sin espacios: ") #1. Solicitar lista de números a usuario
lst=cadena.split(",") #2. Convertir cadena ingresada por el usuario en una lista
primolista(lst) #3. Ejecutar la función primolista con el argumento creado en 2.