num_ini=(input ("Introduce un número entero: "))
nuevo_num=0
for i in range(0,len(num_ini)):
	nuevo_num=nuevo_num+int(num_ini[i])**2
num=str(nuevo_num)
while num!="1":
	nuevo_num=0
	for i in range(0,len(num)):
		nuevo_num=nuevo_num+int(num[i])**2
	num=str(nuevo_num)
if nuevo_num==1:
	print(num_ini, " es feliz")