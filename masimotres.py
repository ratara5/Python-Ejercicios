# Determinar mediante restas y desigualdades sencillas cuál es el mayor de tres números

def masimo(n1, n2, n3):
	resta12=int(n1)-int(n2)
	if resta12>0:
		print(n1, " es mayor que ", n2)
		resta31=int(n3)-int(n1)
		if resta31>0:
			print(n3, " es mayor que ", n1)
			print(n3+" es el mayor de los tres números")
		elif resta31<0:
			print(n1, "es mayor que ", n3)
			print(n1+" es el mayor de los tres números")
		else:
			print(n1, "es igual a ", n3)
			print(n1+"y"+n3+" son el mayor de los tres números")
	elif resta12<0:
		print(n2, " es mayor que ", n1)
		resta32=int(n3)-int(n2)
		if resta32>0:
			print(n3, " es mayor que ", n2)
			print(n3+" es el mayor de los tres números")
		elif resta32<0:
			print(n2, "es mayor que ", n3)
			print(n2+" es el mayor de los tres números")
		else:
			print(n2, "es igual a ", n3)
			print(n2+" y "+n3+" son el mayor de los tres números")
	else:
		print(n2, " es igual a ", n1)
		resta31=int(n3)-int(n1)
		if resta31>0:
			print(n3, " es mayor que ", n1)
			print(n3+" es el mayor de los tres números")
		elif resta31<0:
			print(n1, "es mayor que ", n3)
			print(n1+" y "+n2+" son el mayor de los tres números")
		else:
			print(n1, "es igual a ", n3)
			print("los tres números son iguales")

num1=input("ingresa el primer número: ")
num2=input("ingresa el segundo número: ")
num3=input("ingresa el tercer número: ")
masimo(num1,num2,num3)
