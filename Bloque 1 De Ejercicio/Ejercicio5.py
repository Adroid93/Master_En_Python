'''
Hacer un Programa que todos los numeros entre un rango definido por el usuario
'''

inicio=int(input("Inicio: "))
fin=int(input("Fin: "))

if(inicio<fin):

    for i in range(inicio,fin+1): #Se incluye +1 porque el rango de la funcion es abierto por la derecha
        print(i)
else:
    print("Rango incorecto: El primer numero debe ser menor al segundo")
