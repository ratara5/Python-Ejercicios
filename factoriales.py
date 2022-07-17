def factorial(num):
	num=int(num)
	fact=1
	for i in range(1,num+1):
		fact=fact*i
	print("el factorial de ", num, " es: ", fact)
	return fact
	
# factorial(int(input("ingresa el número del cuál se calcula el factorial: ")))



def factoriallista(lst):
	listaelemyres=[]
	for elem in lst:
		fctrl=factorial(elem)
		# for i in range(0, len(listanum))
		# mensaje=
		listaelemyres.append(str(elem)+"!="+str(fctrl))	
	print(listaelemyres)


listanum=input("Ingresa la lista de valores a calcular factorial, sin ',' y sin espacios: ")
lista=listanum.split(",")
factoriallista(lista)