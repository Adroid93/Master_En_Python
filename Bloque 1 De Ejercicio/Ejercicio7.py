"Mostrar todos lo numeros impares en un rango delimitado por el usurio"

inicial=int(input("Rango inicial: "))
fin= int(input("Rango final: "))

if(inicial<fin):
    for i in range(inicial,fin+1):
        if(i%2!=0):
            print(i," es impar")
else:
    print("Rango invalido!")
