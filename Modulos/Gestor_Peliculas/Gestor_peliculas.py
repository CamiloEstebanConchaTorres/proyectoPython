# IMPORTACION DE LIBRERIAS Y OTRAS FUNCIONALIDADES DE PYTHON #
import json
from os import system

# IMPORTACION DE LOS MODULOS PARA PODER INGRESAR #
from Modulos.Validaciones.Validaciones import menuNoValid
from Storage.datos import peliculas, actores





def Listar_Pleiculas():
    bandera=True
    while (bandera):
        system("clear")
        print("""
        ***********************
        *  Lista de Peliculas  *
        ***********************
        """)
        for i,val in enumerate(peliculas):
            print(f"""
________________________
Peliculas: {val.get('Peliculas')}
id: {val.get('id')}
Nombre: {val.get('Nombre')}
Duracion: {val.get('Duracion')}
Sinopsis: {val.get('Sinopsis')}
_Generos: {val.get('_Generos')}
_Actores: {val.get('_Actores')}
_Formato: {val.get('_Formato')}
________________________
""")
        opc = int(input("Digite el numero 0 en su teclado y presione enter para volver al crud de Listas de Peliculas \n"))
        if (opc == 0):
            system("clear")
            bandera = False

def ELiminar_pelicula():
    bandera = True
    while(bandera):
        system("clear")
        print("""
        ***************************
        * Eliminacion de Pelicula  *
        ***************************
        """)
        for i,val in enumerate(peliculas):
            print(f"""
________________________
Codigo: {i}
Peliculas: {val.get('Peliculas')}
id: {val.get('id')}
Nombre: {val.get('Nombre')}
Duracion: {val.get('Duracion')}
Sinopsis: {val.get('Sinopsis')}
_Generos: {val.get('_Generos')}
_Actores: {val.get('_Actores')}
_Formato: {val.get('_Formato')}
________________________
""")
        codigo = int(input("Ingrese el codigo de la Pelicula que deseas eliminar: \n"))
        print(f"""
________________________
Codigo: {codigo}
Peliculas: {peliculas[codigo].get('Peliculas')}
id: {peliculas[codigo].get('id')}
Nombre: {peliculas[codigo].get('Nombre')}
Duracion: {peliculas[codigo].get('Duracion')}
Sinopsis: {peliculas[codigo].get('Sinopsis')}
_Generos: {peliculas[codigo].get('_Generos')}
_Actores: {peliculas[codigo].get('_Actores')}
_Formato: {peliculas[codigo].get('_Formato')}
________________________
        """)
        print("¿Este es la pelicula que deseas eliminar?")
        print("1. Si")
        opc = int(input())
        if(opc == 1):
            peliculas.pop(codigo)
            with open("Storage/peliculas.json", "w") as f:
                data = json.dumps(peliculas, indent=4)
                f.write(data)
                f.close()
            bandera = False
        elif(opc == 3):
            bandera = False
            system("clear")
    return "Pelicula Eliminada"

def Eliminar_Actor():
  bandera = True
  while(bandera):
        system("clear")
        print("""
        ***************************
        * Eliminacion de Actor  *
        ***************************
        """)
        for i,val in enumerate(actores):
            print(f"""
________________________
Codigo: {i}
id: {val.get('id')}
nombre_actor: {val.get('nombre_actor')}
rol: {val.get('rol')}
________________________
""")
        codigo = int(input("Ingrese el codigo del actor que deseas eliminar: \n"))
        print(f"""
________________________
Codigo: {codigo}
id: {actores[codigo].get('id')}
nombre_actor: {actores[codigo].get('nombre_actor')}
rol: {actores[codigo].get('rol')}
________________________
        """)
        print("¿Este es el Actor que deseas eliminar?")
        print("1. Si")
        opc = int(input())
        if(opc == 1):
            actores.pop(codigo)
            with open("Storage/actores.json", "w") as f:
                data = json.dumps(actores, indent=4)
                f.write(data)
                f.close()
            bandera = False
        elif(opc == 3):
            bandera = False
            system("clear")
        return "Actor Eliminado"


def menu():
    bandera = True
    while (bandera):
        print("""*******************
MODULO DE PELICULAS
*******************
CRUD de Gestor Peliculas
""")
        print("\t1. Listar todas las Peliculas")
        print("\t2. Eliminar Peliculas")
        print("\t3. Eliminar Actor")
        print("\t0. Menu Principal \n")
        opc = int(input("seleccione su opcion \n"))
        match(opc):
            case 1: Listar_Pleiculas()
            case 2: ELiminar_pelicula()
            case 3: Eliminar_Actor()
            case 0: 
                system("clear")
                bandera = False
            case _: print(menuNoValid(opc))