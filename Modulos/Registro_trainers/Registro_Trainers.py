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
        "Disponibilidad": int(input("Que disponibilidad tiene el trainer?:\n\t"+"\t".join([f"{Disponibilidad.index(i)+1}. {i}\n" for i in (Disponibilidad)]))),
        "Campers": ""
    }
    trainer.append(info)
    with open("Storage/trainers/trainer.json", "w") as f:
        data = json.dumps(trainer, indent=4)
        f.write(data)
        f.close()
    return "Sucessfully Trainer"

def Actualizar():
    bandera=True
    while (bandera):
        system("clear")
        print("""
        ***************************
        * Acualizacion del Trainer *
        ***************************
        """)
        codigo = int(input("Ingrese el codigo del trainer que desea actualizar \n"))
        print(f"""
________________________
Codigo: {codigo}
Nombre: {trainer[codigo].get('Nombre')}
Apellido: {trainer[codigo].get('Apellido')}
Identifiacion: {trainer[codigo].get('Identificacion')}
Direccion: {trainer[codigo].get('Direccion')}
Edad: {trainer[codigo].get('Edad')}
Telefono: {trainer[codigo].get('Telefono')}
________________________
        """)
        print("¿Este es el trainer que deseas actualizar? \n")
        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc = int(input())
        if(opc == 1):
            info = {
                "Nombre": input("Ingrese el nombre del trainer\n"),
                "Apellido": input("Ingrese el apellido del trainer\n"),
                "Identifiacion": int(input("Ingrese la Identificacion del trainer\n")),
                "Direccion": int(input("Ingrese la Direccion del trainer\n")),
                "Edad": int(input("Ingrese la Edad del trainer\n")),
                "Telefono": int(input("Ingrese el Telefono del trainer\n")),
            }
            trainer[codigo] = info
            with open("Storage/trainers/trainer.json", "w") as f:
                data = json.dumps(trainer, indent=4)
                f.write(data)
                f.close()
            bandera == False
        elif(opc == 3):
            bandera == False
    return "Actualizado"

def menu ():
    print("""*******************************
SISTEMA DE CREACION DE TRAINERS
*******************************
""")
    bandera=True
    while (bandera):
        print("\t1. Crear Trainer")
        print("\t2. Actualizar Trainer")
        print("\t0. Atras \n")
        opc = int(input("Seleccione su Opcion: \n"))
        match(opc):
            case 1: save()
            case 2: Actualizar()
            case 0:
                system("clear")
                bandera = False
            case _: print(menuNoValid(opc))