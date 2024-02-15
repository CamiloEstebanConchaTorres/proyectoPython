# IMPORTACION DE LIBRERIAS Y OTRAS FUNCIONALIDADES DE PYTHON #
from os import system
import json

# IMPORTACION DE LOS MODULOS PARA PODER INGRESAR #
from Modulos.Administrador_Generos import Administrador_generos
from Modulos.Administador_Actores import Administrador_actores
from Modulos.Administrar_Formatos import Administrar_formatos
from Modulos.Gestor_Peliculas import Gestor_peliculas

from Storage.datos import generos


# IMPORTACION DE VALIDACIONES DE LOS MODULOS #
from Modulos.Validaciones.Validaciones import menuNoValid



import Modulos.Actores as Actores
import Modulos.Formatos as Formatos
import Modulos.Generos as Generos
import Modulos.Peliculas as Peliculas

from Storage.datos import generos, actores, formatos, peliculas

actores = Actores.carga()
formatos = Formatos.carga()
generos = Generos.carga()
peliculas = Peliculas.carga()





print("""***************************************
SISTEMA GESTOR DE PELICULAS BLOCKBUSTER
***************************************
        CRUD de BLOCKBUSTER
""")
def menu():
    print("\t1. Administrador de Generos")
    print("\t2. Administrador de Actores")
    print("\t3. Administrador de Formatos")
    print("\t4. Crear Pelicula")
    print("\t5. Gestionar Peliculas")
    print("\t0. Salir \n")
    
bandera = True
while (bandera):
    menu()
    opc = int(input("ingrese el numero del modulo al que desea ingresar \n"))
    match(opc):
        case 1: 
            with open("Storage/generos.json", "r") as f:                                                             
                Administrador_generos.generos = json.loads(f.read())
                f.close()      
                system("clear")
                Administrador_generos.menu()
        case 2: 
            with open("Storage/actores.json", "r") as f:                                                             
                Administrador_actores.actores = json.loads(f.read())
                f.close()      
                system("clear")
                Administrador_actores.menu()
        case 3: 
            with open("Storage/formatos.json", "r") as f:                                                             
                Administrar_formatos.formatos = json.loads(f.read())
                f.close()      
                system("clear")
                Administrar_formatos.menu()    
        case 4:
            Pelis = {
            "Peliculas": f"P0{len(peliculas)+1}",
            "id": f"P0{len(peliculas)+1}",
            "Nombre": input("ingrese el nombre de la pelicula \n"),
            "Duracion": input(input("ingrese la duracion de la pelicula ej.(tres horas) \n")),
            "Sinopsis": input("ingrese la sinpsis de la pelicula \n"),
            "_Generos": Generos.carga(),
            "_Actores": Actores.carga(),
            "_Formato": Formatos.carga()
        }
            peliculas.append(Pelis)
            path = "Storage/"
            with open(path+"peliculas.json", "w") as f:
                f.write(json.dumps(peliculas, indent=4))
                f.close()
        case 5:
            with open("Storage/peliculas.json", "r") as f:                                                             
                Gestor_peliculas.peliculas = json.loads(f.read())
                f.close()
            with open("Storage/actores.json", "r") as f:                                                             
                Gestor_peliculas.actores = json.loads(f.read())
                f.close()      
                system("clear")
                Gestor_peliculas.menu()
        case 0:
            system("clear")
            bandera = False
        case _:
            print(menuNoValid(opc))

def plantilla(data):
    lista = []
    for i,val in enumerate(data):
        lista.append(f"\n\t\t{i+1} - {val}")
    return "".join(lista)
