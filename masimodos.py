def masimo(n1, n2):
	resta=int(n1)-int(n2)
	if resta>0:
		print(n1, " es mayor que ", n2)
	elif resta<0:
		print(n1, " es menor que ", n2)
	else:
		print(n1, " igual a ", n2)

num1=input("ingresa el primer número: ")
num2=input("ingresa el segundo número: ")
masimo(num1,num2)
