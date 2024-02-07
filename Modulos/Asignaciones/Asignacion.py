# IMPORTACION DE LIBRERIAS Y OTRAS FUNCIONALIDADES DE PYTHON #
import json
from os import system

# IMPORTACION DE LOS MODULOS PARA PODER INGRESAR #
from Modulos.Validaciones.Validaciones import menuNoValid
from Storage.Datos.datos import Rutas
from Storage.Datos.datos import Areas
from Storage.Datos.datos import Temas
from Storage.Datos.datos import trainer




def temario():
    bandera=True
    while (bandera):
        system("clear")
        print("""
        ************************************
        *  Asignacion de Temas a una Ruta  *
        ************************************
        """)
        for i,val in enumerate(Rutas):
            print(f"""
________________________
Codigo: {i}
Nombre: {val.get('Nombre')}
Tema: {val.get('Tema')}
________________________
""")
        Codigo = int(input("Seleccione una Ruta \n"))
        print(f"""
________________________
Codigo: {Codigo}
Nombre: {Rutas[Codigo].get('Nombre')}
Tema: {Rutas[Codigo].get('Tema')}
________________________
""")
        print("¿Esta es la Ruta a la que desea asignarle temas? \n")
        print("1. Si")
        print("2. No")
        print("3. Salir\n")
        opc = int(input("Seleccione su opcion \n"))
        if (opc == 1):
            info = {
                "Nombre": Rutas[Codigo].get('Nombre'),
                "Tema": int(input("Asigne el temario de la ruta:\n\t"+"\t".join([f"{Temas.index(i)+1}. {i}\n" for i in (Temas)])))
                }
            Rutas[Codigo] = info
            with open("Storage/Rutas_entrenamiento/rutas.json", "w+") as f: 
                datos = json.dumps(Rutas, indent=4)
                f.write(datos)
                f.close()
                return print(f"rutas successfully ")            
        elif (opc == 2):
            bandera = False
        elif (opc == 3):
            system("clear")
            bandera = False

def Area():
    bandera=True
    while (bandera):
        system("clear")
        print("""
        ************************************
        *  Asignacion de Ruta a un Area  *
        ************************************
        """)
        for i,val in enumerate(Areas):
            print(f"""
________________________
Codigo: {i}
Nombre: {val.get('Nombre')}
Ruta: {val.get('Ruta')}
________________________
""")
        Codigo = int(input("Seleccione un Area \n"))
        print(f"""
________________________
Codigo: {Codigo}
Nombre: {Areas[Codigo].get('Nombre')}
Tema: {Areas[Codigo].get('Tema')}
________________________
""")
        print("¿Esta es el Area al que desea asignarle una Ruta? \n")
        print("1. Si")
        print("2. No")
        print("3. Salir\n")
        opc = int(input("Seleccione su opcion \n"))
        if (opc == 1):
            info = {
                "Nombre": Areas[Codigo].get('Nombre'),
                "Ruta": int(input("Asigne la Ruta del Area:\n\t"+"\t".join([f"{Rutas.index(i)+1}. {i}\n" for i in (Rutas)])))
                }
            Areas[Codigo] = info
            with open("Storage/Areas_entrenamiento/areas.json", "w+") as f: 
                datos = json.dumps(Areas, indent=4)
                f.write(datos)
                f.close()
                return print(f"rutas successfully ")            
        elif (opc == 2):
            bandera = False
        elif (opc == 3):
            system("clear")
            bandera = False      

def trainers():
    bandera=True
    while (bandera):
        system("clear")
        print("""
        *************************************
        *  Asignacion de trainer a un Area  *
        *************************************
        """)
        for i,val in enumerate(Areas):
            print(f"""
________________________
Codigo: {i}
Nombre: {val.get('Nombre')}
Ruta: {val.get('Ruta')}
Trainer: {val.get('Trainer')}
________________________
""")
        Codigo = int(input("Seleccione un Area \n"))
        print(f"""
________________________
Codigo: {Codigo}
Nombre: {Areas[Codigo].get('Nombre')}
Ruta: {Areas[Codigo].get('Ruta')}
Trainer: {Areas[Codigo].get('Trainer')}
________________________
""")
        print("¿Esta es el Area al que desea asignarle un Trainer? \n")
        print("1. Si")
        print("2. No")
        print("3. Salir\n")
        opc = int(input("Seleccione su opcion \n"))
        if (opc == 1):
            info = {
                "Nombre": Areas[Codigo].get('Nombre'),
                "Ruta": Areas[Codigo].get('Nombre'),
                "Trainer": int(input("Asigne el trainer a el Area:\n\t"+"\t".join([f"{trainer.index(i)+1}. {i}\n" for i in (trainer)])))
                }
            Areas[Codigo] = info
            with open("Storage/Areas_entrenamiento/areas.json", "w+") as f: 
                datos = json.dumps(Areas, indent=4)
                f.write(datos)
                f.close()
                return print(f"rutas successfully ")            
        elif (opc == 2):
            bandera = False
        elif (opc == 3):
            system("clear")
            bandera = False      

def camper():
    print("hola")

    print("hola")

def menu():
    bandera = True
    while (bandera):
        print("""**********************
MODULO DE ASIGNACIONES
**********************
CRUD del modulo de Evaluacion del camper
""")
        print("\t1. Asignacion de temas a una Ruta de entrenamiento")
        print("\t2. Asignacion de Ruta un Area de entrenamiento")
        print("\t3. Asignacion de Trainers a un Area de entrenamiento")    
        print("\t4. Asignacion de Campers a Trainers")
        print("\t0. Salir \n")
        opc = int(input("seleccione su opcion \n"))
        match(opc):
            case 1: temario()
            case 2: Area()
            case 3: trainers()
            case 4: camper()
            case 0: 
                system("clear")
                bandera = False
            case _: print(menuNoValid(opc))