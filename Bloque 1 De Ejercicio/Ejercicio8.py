#Sacar el tanto porciento de un numero dado

numero= int(input("Ingrese el numero al cual desea sacarle el porcentaje: "))
porcentaje=int(input("Cuanto porcentaje desea sacar?: "))

resultado=numero*porcentaje/100
print("El ",porcentaje,"% de ",numero," es",resultado)