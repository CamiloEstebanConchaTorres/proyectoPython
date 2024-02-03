# IMPORTACION DE LIBRERIAS Y OTRAS FUNCIONALIDADES DE PYTHON #
import json
from os import system


# IMPORTACION DE LOS MODULOS PARA PODER INGRESAR #
from Storage.Datos.datos import camper
from Storage.Datos.datos import Estados
from Modulos.Validaciones.Validaciones import menuNoValid



def save():
    info = {
        "Nombre": input("Ingrese los nombres del camper\n"),
        "Apellido": input("Ingrese los apellidos del camper\n"),
        "Identifiacion": int(input("Ingrese el numero de identificacion del camper\n")),
        "Direccion": input("Ingrese la direccion del camper\n"),
        "Edad": int(input("Ingrese la edad del camper\n")),
        "Telefono": int(input("Ingrese el Telefono del camper\n")),
        "Estado": int(input("Asigne el Estado del camper:\n\t"+"\t".join([f"{Estados.index(i)+1}. {i}\n" for i in (Estados)])))
    }
    camper.append(info)
    with open("Storage/Campers/camper.json", "w") as f:
        data = json.dumps(camper, indent=4)
        f.write(data)
        f.close()
    return "Sucessfully Camper"
      
def menu ():
    print("""******************************
SISTEMA DE CREACION DE CAMPERS
******************************
""")
    bandera=True
    while (bandera):
        print("\t1. Crear camper")
        print("\t0. Atras \n")
        opc = int(input("Seleccione su Opcion: \n"))
        match(opc):
            case 1: save()
            case 0:
                system("clear")
                bandera = False
            case _: print(menuNoValid(opc))