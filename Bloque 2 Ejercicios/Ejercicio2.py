'''
Escribe un programa que agregue valores a una lista mientras que su longitud sea menor a 120
y luego mostrar la lista
Realizar con For y While
'''
numero=[]
x=1
print("Con el For:")
for i in range(0,121):
    numero.append(i)
    print("Mostrando el ",numero[i])

print(numero)

print("Con while ")

while(x<121):
    numero.append(x)
    print("Mostrando el ", numero[x])
    x+=1
