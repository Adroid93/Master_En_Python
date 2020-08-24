''''
Hacer un programa que tenga una lista de 8 numeros enteros y haga lo siguiente:
    - Recorra la lista y retorne un string para mostrarla (Hacer con y sin funcion)
    - Ordenar y mostrarla
    - Mostrar su longitud
    - Buscar algun elemento (que el usuario pida por teclado)
'''
#Sin funcion


'''for i in lista:
    print("Numero: ",i)
  '''

#Con funcion

def buscar(lista, elemento):
    for i in range(0,len(lista)):
        if(lista[i] == elemento):
            return "Se encontro una coincidencia en la posision ",lista.index(elemento)

def recorre(lista,elemento):
    resultado=""
    for i in lista:

        resultado+=str(i)
        resultado+="\n"
    return resultado,"el numero buscado es ",elemento

lista=[7,5,11,99,27,54,47,64]
numero=int(input("Ingrese el numero que desea buscar: "))

print(recorre(lista,numero))

print("lista ordenada")
lista.sort()
print(lista)

print("La longitud de la lista es: ",len(lista))