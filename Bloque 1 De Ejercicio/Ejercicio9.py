'''
Hacer un programa que pida numeros y los muestre indefinidamente
hasta que el usuario ingrese el numero 111
'''
numero=int(input("Ingrese un numero"))
print("El numero es: ",numero)

while(numero!=111):
    numero=int(input("Ingrese un numero"))
    print("El numero es: ",numero)