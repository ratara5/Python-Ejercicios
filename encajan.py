# Determinar si dos fichas de dominó encajan. ATENCIÓN: Se usan tuplas en lugar de listas

def encajadomino(ficha1,ficha2):
	ctrl=False
	for i in range(0,len(ficha1)):
		print(ficha1[i])
		for j in range(0, len(ficha2)):
			print(ficha2[j])
			if ficha1[i]==ficha2[j]:
				ctrl=True
	return ctrl
				
f1=tuple(input("indique primera ficha de domino (los dos números seguidos, n1n2): "))
print(f1, type(f1))
f2=tuple(input("indique segunda ficha de domino (los dos números seguidos, n1n2): "))
print(f2, type(f2))
control=encajadomino(f1,f2)
print("Las fichas ",f1," y ",f2," encajan: ",control)