# IMPORTACION DE LIBRERIAS Y OTRAS FUNCIONALIDADES DE PYTHON #
import json
from os import system

# IMPORTACION DE LOS MODULOS PARA PODER INGRESAR #
from Modulos.Validaciones.Validaciones import menuNoValid
from Storage.datos import actores




def Actores():

    info = {
            "codigo": f"A0{len(actores)+1}",
            "id": f"A0{len(actores)+1}",
            "nombre_actor": input("Ingrese el nombre del Actor: \n"),
            "rol": input("ingrese el rol del actor \n")
    }
    actores.append(info)
    with open("Storage/actores.json", "w") as f:
            datos = json.dumps(actores, indent=4)
            f.write(datos)
            f.close()
            system("clear")
            print("Actor Creado con exito")
    return "Sucessfully Actores"    

def ListarActores():
    bandera=True
    while (bandera):
        system("clear")
        print("""
        ***********************
        *  Lista de Actores  *
        ***********************
        """)
        for i,val in enumerate(actores):
            print(f"""
________________________
codigo: {val.get('codigo')}
id: {val.get('id')}
nombre_actor: {val.get('nombre_actor')}
rol: {val.get('rol')}
________________________
""")
        opc = int(input("Digite el numero 0 en su teclado y presione enter para volver al crud de Actores \n"))
        if (opc == 0):
            system("clear")
            bandera = False
  
def menu():
    bandera = True
    while (bandera):
        print("""***************************
MODULO DE GESTOR DE ACTORES
***************************
CRUD de Gestor de ACTORES
""")
        print("\t1. Crear Actores")
        print("\t2. Listar Actores")
        print("\t0. Menu Principal \n")
        opc = int(input("seleccione su opcion \n"))
        match(opc):
            case 1: Actores()
            case 2: ListarActores()
            case 0: 
                system("clear")
                bandera = False
            case _: print(menuNoValid(opc))