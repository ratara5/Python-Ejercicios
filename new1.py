1 == 1
print(1==1)
1 is 1
print(1 is 1)
[1] == [1]
print([1]==[1])
[1] is [1]
print([1] is [1])
type (1.2)
print(type(1.2))
a = 2
a += 1
print(a)

elem=1
fctrl=1

mensaje="el factorial de ",elem," es ",fctrl
print(mensaje)
print(type(('2','1'))) #Es tupla
print(type((2,1))) #Es tupla. Diferente si los datos vienen de input
# print(type('2','1')) #Error
# print(type(2,1)) #Error

dat=(input("Ingrese datos: "))
print(dat, type(dat))
datlist=dat.split(",")
tupla=tuple(datlist)
print(tupla, type(tupla))