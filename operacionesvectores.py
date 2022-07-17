# OPERACIONES CON VECTORES EN 3D. ATENCIÓN: LOS VECTORES SE TRABAJARÁN COMO TUPLA (POR EJERCICIO)

# Tomar vectores
def tomarvectores():
	vector1=input("Ingrese primer vector (x,y,z) sin espacios: ")
	vector2=input("Ingrese segundo vector (x,y,z) sin espacios: ")
	# print(dat, type(dat))
	vector1=vector1.rstrip(")")
	vector1=vector1.lstrip("(")
	vector2=vector2.rstrip(")")
	vector2=vector2.lstrip("(")
	vector1list=vector1.split(",")
	vector2list=vector2.split(",")
	# print(dat, type(dat))
	print(vector1list, vector2list)
	tupla1=tuple(vector1list)
	tupla2=tuple(vector2list)
	print(tupla1, type(tupla1), type(tupla1[0]), tupla2, type(tupla2), type(tupla2[0]))
	return tupla1, tupla2

def escalar(vctr1,vctr2):
	suma=0
	for i in range(0,len(vctr1)):
		suma=suma+float(vctr1[i])*float(vctr2[i])
	return suma
	

def ortogonal(vctr1,vctr2):
	esc=escalar(vctr1,vctr2)
	if esc==0:
		ort=True
	else:
		ort=False
	return ort

def paralelo(vctr1,vctr2):
	listaver1=[]
	listaver2=[]
	# for i in range(0,len(vctr1)):
	a=float(vctr1[0])/float(vctr2[0])
	print(a)
	# lista.append(a)
	for i in range(0,len(vctr2)):
		listaver2.append(float(vctr2[i])*a)
		listaver1.append(float(vctr1[i]))
	print(listaver1,listaver2)
	if listaver1==listaver2:
		par=True
	else:
		par=False
	return par
	

def operacion(op, vec1, vec2):
	if op==1:
		esc=escalar(vec1,vec2)
		print("El producto escalar de",vec1,"y",vec2,"es",esc)
	elif op==2:
		otg=ortogonal(vec1,vec2)
		print("Los vectores",vec1,"y",vec2,"son ortogonales:",otg)
	elif op==3:
		pll=paralelo(vec1,vec2)
		print("Los vectores",vec1,"y",vec2,"son paralelos:",pll)
	elif op==4:
		norma(vec1,vec2)
		
def proceso():
	opc=0
	while opc<1 or opc>4:
		opc=int(input("Selecciona una operación: \n1.    Producto escalar \n2.    Ortogonalidad \n3.     Paralelismo \n4.     Norma \n"))
		operacion(opc,v1,v2)
		
(v1,v2)=tomarvectores()
proceso()