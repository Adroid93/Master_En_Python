''''
Crear un scrip que tenga 4 variables : una lista, un string, un entero
y booleano y que imprima un mensaje segun el tipo de dato de cda
variable. Usar funciones
'''


def mostrarTipo(tipoDato):
    return print(f"El tipo de dato de {tipoDato} es " + str(type(tipoDato)))


lista = ["Alexis", 24, "Argentino", True]
texto = "Brian"
numero = 24
booleano = False

mostrarTipo(lista)
mostrarTipo(texto)
mostrarTipo(numero)
mostrarTipo(booleano)