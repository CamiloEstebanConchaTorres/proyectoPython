# IMPORTACION DE LIBRERIAS Y OTRAS FUNCIONALIDADES DE PYTHON #
import json
from os import system


# IMPORTACION DE LOS MODULOS PARA PODER INGRESAR #
from Storage.Datos.datos import camper
from Storage.Datos.datos import Estados
from Modulos.Validaciones.Validaciones import menuNoValid



def save():
    edad = int(input("ingrese la edad del camper \n"))
    N_Acudiente = ""
    Numero_Acu = ""
    Acudiente = ""
    if edad <=15:
        return print("! No puede ingresar a Campuslands, ya que no cumple con la edad necesaria ! \n")
    elif edad >=16 and edad <=17:
        print(" ! CAMPER MENOR DE EDAD !")
        N_Acudiente = input("Porfavor ingrese el Nombre del acudiente \n")
        Numero_Acu =  (int(input("Porfavor ingrese el Numero del acudiente \n")))
        Acudiente = (int(input("Porfavor ingrese el numero de identificacion del acudiente \n")))
    info = {
        "Nombre": input("Ingrese los nombres del camper\n"),
        "Apellido": input("Ingrese los apellidos del camper\n"),
        "Identificacion": int(input("Ingrese el numero de identificacion del camper\n")),
        "Direccion": input("Ingrese la direccion del camper\n"),
        "Edad": edad,
        "NombreAcudiente": N_Acudiente,
        "NumeroAcudiente": Numero_Acu,
        "idAcudiente": Acudiente,
        "TelefonoCamper":[
            {
            f"{'Fijo' if(int(input('1. Numero Fijo  0. Numero de Celular:  '))) else 'Celular'}":
            int(input(f'Numero de contacto {x+1}: '))
            }
            for x in range(int(input("Cuantos numeros de telefono tiene el camper?:  ")))
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