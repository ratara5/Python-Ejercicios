# Determinar si un número es feliz. Este programa está limitado por un cantidad fija de iteraciones

num_ini=(input ("Introduce un número entero: "))
nuevo_num=0
for i in range(0,len(num_ini)):
	nuevo_num=nuevo_num+int(num_ini[i])**2
num=str(nuevo_num)
lista_ver=[]
for j in range(0,31):
	lista_ver.insert(j,num)
	nuevo_num=0
	for i in range(0,len(num)):
		nuevo_num=nuevo_num+int(num[i])**2
	num=str(nuevo_num)
	print(lista_ver)
if lista_ver[30]=="1":
	print(num_ini, " es feliz")
else:
	print(num_ini, " no es feliz")
