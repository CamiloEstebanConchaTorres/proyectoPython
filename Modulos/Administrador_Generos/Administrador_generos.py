# IMPORTACION DE LIBRERIAS Y OTRAS FUNCIONALIDADES DE PYTHON #
import json
from os import system

# IMPORTACION DE LOS MODULOS PARA PODER INGRESAR #
from Modulos.Validaciones.Validaciones import menuNoValid
from Storage.datos import generos




def Generos():

    info = {
            "codigo": f"G0{len(generos)+1}",
            "id": f"G0{len(generos)+1}",
            "nombre_genero": input("Ingrese el nombre del genero: \n"),
    }
    generos.append(info)
    with open("Storage/generos.json", "w") as f:
            datos = json.dumps(generos, indent=4)
            f.write(datos)
            f.close()
            system("clear")
            print("Genero Creado con exito")
    return "Sucessfully Generos"    

def ListarGenero():
    bandera=True
    while (bandera):
        system("clear")
        print("""
        ***********************
        *  Lista de Generos  *
        ***********************
        """)
        for i,val in enumerate(generos):
            print(f"""
________________________
codigo: {val.get('codigo')}
id: {val.get('id')}
nombre_genero: {val.get('nombre_genero')}
________________________
""")
        opc = int(input("Digite el numero 0 en su teclado y presione enter para volver al crud de Generos \n"))
        if (opc == 0):
            system("clear")
            bandera = False
  
def menu():
    bandera = True
    while (bandera):
        print("""***************************
MODULO DE GESTOR DE GENEROS
***************************
CRUD de Gestor de generos
""")
        print("\t1. Crear Generos")
        print("\t2. Listar Generos")
        print("\t0. Menu Principal \n")
        opc = int(input("seleccione su opcion \n"))
        match(opc):
            case 1: Generos()
            case 2: ListarGenero()
            case 0: 
                system("clear")
                bandera = False
            case _: print(menuNoValid(opc))