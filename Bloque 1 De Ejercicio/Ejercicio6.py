
#Mostrar todas las tabla de multiplicar del 1 al 10
resultado=0
for i in range(1,11):

    print("Tabla del ",i)

    for numero in range(1,11):

        resultado= i*numero
        print(i," x ",numero," = ",resultado)

