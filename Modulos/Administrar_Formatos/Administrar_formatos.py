# IMPORTACION DE LIBRERIAS Y OTRAS FUNCIONALIDADES DE PYTHON #
import json
from os import system

# IMPORTACION DE LOS MODULOS PARA PODER INGRESAR #
from Modulos.Validaciones.Validaciones import menuNoValid
from Storage.datos import formatos




def Formatoss():

    info = {
            "codigo": f"F0{len(formatos)+1}",
            "id": f"F0{len(formatos)+1}",
            "nombre_formato": input("Ingrese el nombre del formato: \n"),
            "NroCopias": int(input("Ingrese la cantidad de copias del formato: \n")),
            "valorPrestamo": int(input("Ingrese el valor del prestamo ej.(5000 - sin usar puntos): \n")),
    }
    formatos.append(info)
    with open("Storage/formatos.json", "w") as f:
            datos = json.dumps(formatos, indent=4)
            f.write(datos)
            f.close()
            system("clear")
            print("Formato Creado con exito")
    return "Sucessfully Formatos"    

def ListarFormatos():
    bandera=True
    while (bandera):
        system("clear")
        print("""
        ***********************
        *  Lista de Formatos  *
        ***********************
        """)
        for i,val in enumerate(formatos):
            print(f"""
________________________
codigo: {val.get('codigo')}
id: {val.get('id')}
nombre_formato: {val.get('nombre_formato')}
NroCopias: {val.get('NroCopias')}
valorPrestamo: {val.get('valorPrestamo')}
________________________
""")
        opc = int(input("Digite el numero 0 en su teclado y presione enter para volver al crud de Formatos \n"))
        if (opc == 0):
            system("clear")
            bandera = False
  
def menu():
    bandera = True
    while (bandera):
        print("""****************************
MODULO DE GESTOR DE FORMATOS
****************************
CRUD de Gestor de generos
""")
        print("\t1. Crear Formatos")
        print("\t2. Listar Formatos")
        print("\t0. Menu Principal \n")
        opc = int(input("seleccione su opcion \n"))
        match(opc):
            case 1: Formatoss()
            case 2: ListarFormatos()
            case 0: 
                system("clear")
                bandera = False
            case _: print(menuNoValid(opc))