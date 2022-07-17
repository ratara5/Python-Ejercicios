# 1 == 1
# print(1==1)
# 1 is 1
# print(1 is 1)
# [1] == [1]
# print([1]==[1])
# [1] is [1]
# print([1] is [1])
# type (1.2)
# print(type(1.2))
# a = 2
# a += 1
# print(a)

# elem=1
# fctrl=1

# mensaje="el factorial de ",elem," es ",fctrl
# print(mensaje)
print(type(('2','1'))) #Es tupla
print(type((2,1))) #Es tupla. Diferente si los datos vienen de input
# print(type('2','1')) #Error
# print(type(2,1)) #Error

# dat=input("Ingrese datos separados por ',' sin espacios: ")
# print(dat, type(dat))
# datlist=dat.split(",")
# tupla=tuple(datlist)
# print(tupla, type(tupla), type(tupla[0]))

dat=input("Ingrese vector (x,y) sin espacios: ")
print(dat, type(dat))
dat=dat.rstrip(")")
dat=dat.lstrip("(")
datlist=dat.split(",")
print(dat, type(dat))
print(datlist)
tupla=tuple(datlist)
print(tupla, type(tupla), type(tupla[0]))