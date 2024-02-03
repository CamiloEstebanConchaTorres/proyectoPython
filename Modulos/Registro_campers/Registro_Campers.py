# IMPORTACION DE LIBRERIAS Y OTRAS FUNCIONALIDADES DE PYTHON #
import json
from os import system


# IMPORTACION DE LOS MODULOS PARA PODER INGRESAR #
from Storage.Datos.datos import camper
from Storage.Datos.datos import Estados
from Modulos.Validaciones.Validaciones import menuNoValid



def save():
    edad = int(input("ingrese la edad del camper"))
    Acudiente = ""
    if edad <=15:
        return print("No puede ingresar a Campuslands, ya que no cumple con la edad necesaria \n")
    elif edad >=16 and edad <=17:
        Acudiente = (int(input("Porfavor ingrese el numero de identificacion de su acudiente \n")))
    info = {
        "Nombre": input("Ingrese los nombres del camper\n"),
        "Apellido": input("Ingrese los apellidos del camper\n"),
        "Identifiacion": int(input("Ingrese el numero de identificacion del camper\n")),
        "Direccion": input("Ingrese la direccion del camper\n"),
        "Edad": edad,
        "idAcudiente": Acudiente,
        "Telefono":[
            {
            f"{'Fijo' if(int(input('1. Fijo  0. Celular:  '))) else 'Celular'}":
            int(input(f'Numero de contacto {x+1}: '))
            }
            for x in range(int(input("Ingrese la cantidad de telefonos que tiene:  ")))
        ],          
        "Estado": int(input("Asigne el Estado del camper:\n\t"+"\t".join([f"{Estados.index(i)+1}. {i}\n" for i in (Estados)]))),

    }
    camper.append(info)
    with open("Storage/Campers/camper.json", "w") as f:
        datos = json.dumps(camper, indent=4)
        f.write(datos)
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