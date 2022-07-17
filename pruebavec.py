v1=('2','3','1')
v2=('4','6','2')
print(v1, v2, type(v1), type(v2), type(v1[0]), type(v2[0]))
listav1=[]
listav2=[]
a=float(v1[0])/float(v2[0])
print(a)
# lista.append(a)
for i in range(0,len(v2)):
	listav2.append(float(v2[i])*a)
	listav1.append(float(v1[i]))	
if listav1==listav2:
	par=True
else:
	par=False
print("paralelos: ", par)
