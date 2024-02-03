# IMPORTACION DE LIBRERIAS Y OTRAS FUNCIONALIDADES DE PYTHON #
import json
from os import system

# VALIDACION #
from Modulos.Validaciones.Validaciones import menuNoValid

# IMPORTACION DE LOS MODULOS PARA PODER INGRESAR #
from Storage.Datos.datos import trainer
from Storage.Datos.datos import Disponibilidad


def save():
    info = {
        "Nombre": input("Ingrese los nombres del Trainer\n"),
        "Apellido": input("Ingrese los apellidos del Trainer\n"),
        "Identifiacion": int(input("Ingrese el numero de identificacion del Trainer\n")),
        "Direccion": input("Ingrese la direccion del Trainer\n"),
        "Edad": int(input("Ingrese la edad del Trainer\n")),
        "Telefono": int(input("Ingrese el Telefono del Trainer\n")),
        "Disponibilidad": int(input("Que disponibilidad tiene el trainer?:\n\t"+"\t".join([f"{Disponibilidad.index(i)+1}. {i}\n" for i in (Disponibilidad)])))
    }
    trainer.append(info)
    with open("Storage/trainers/trainer.json", "w") as f:
        data = json.dumps(trainer, indent=4)
        f.write(data)
        f.close()
    return "Sucessfully Trainer"
      
def menu ():
    print("""*******************************
SISTEMA DE CREACION DE TRAINERS
*******************************
""")
    bandera=True
    while (bandera):
        print("\t1. Crear Trainer")
        print("\t0. Atras \n")
        opc = int(input("Seleccione su Opcion: \n"))
        match(opc):
            case 1: save()
            case 0:
                system("clear")
                bandera = False
            case _: print(menuNoValid(opc))