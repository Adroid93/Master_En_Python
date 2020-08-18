'''
El programa debe pedir la nota de 15 alumnos
y mostrar por pantalla cuantos han aprobado y cuantos reprobados
'''
aprobados=0
reprobado=0

for i in range(1,16):
    notas=int(input("Ingrese nota : "))
    if(notas>=5):
        aprobados+=1
    else:
        reprobado+=1

print("La cantidad de aprobados es ",aprobados)
print("La cantidad de reprobados es ",reprobado)