'''
Realice un programa que compruebe si una variable esta vacia
y si esta vacia rellenarla con texto en minusculas y mostrarlo en mayusculas
'''

texto=" "

if(len(texto.strip())<=0):
    texto="hola soy un texto en minusculas"
    print(texto.upper()) #Esta funcion convierte en mayusculas

else:
    print("la variable tiene contenido: ",texto)
