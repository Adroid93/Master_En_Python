'''
Pedir dos numeros al usuario para realizar las operaciones basicas de una calculadora basica
'''
resultado=0
print("CALCULADORA SIMPLE\n")
print("Ingrese 1 para Sumar\n")
print("Ingrese 2 para Restar\n")
print("Ingrese 3 para Multiplicar\n")
print("Ingrese 4 para Dividir\n")
opc=int(input("Seleccione una opcion"))

numero1=int(input("Ingrese el primer numero: "))
numero2=int(input("Ingrese el segundo numero: "))

if(opc==1):
    resultado= numero1 + numero2
    print("La suma de ",numero1,"+", numero2,"es ",resultado)

if (opc == 2):
    resultado = numero1 - numero2
    print("La resta de ", numero1, "-", numero2, "es ", resultado)

if(opc==3):
    resultado= numero1 * numero2
    print("La multiplicacion de ",numero1,"x", numero2,"es ",resultado)

if(opc==4):
    resultado= numero1 / numero2
    print("La division de ",numero1,"/", numero2,"es ",resultado)



