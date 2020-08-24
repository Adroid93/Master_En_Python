'''
Crear una lista con el contenido de esta tabla

ACCION     AVENTURA                DEPORTE
GTA        ASSINS                  FIFA 21
COD        CRASH                   PRO 21
PUGB       PRINCE OF PRESIA        MOTO GP 21
Mostrar esta informacion ordenada
'''
juegos = [ {'ACCION':['GTA','COD','PUGB']},
           {'AVENTURA':['ASSINS','CRASH','PRINCE OF PRESIA']},
           {'DEPORTE':['FIFA 21','PRO 21','MOTO GP 21']  }
           ]
for i in juegos:
    for j in i:
        print("\n",j,"\n")
        for k in i[j]:
            print(k)