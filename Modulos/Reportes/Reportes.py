# IMPORTACION DE LIBRERIAS Y OTRAS FUNCIONALIDADES DE PYTHON #
import json
from os import system

# IMPORTACION DE LOS MODULOS PARA PODER INGRESAR #
from Modulos.Validaciones.Validaciones import menuNoValid
from Storage.Datos.datos import Rutas
from Storage.Datos.datos import Areas
from Storage.Datos.datos import Temas
from Storage.Datos.datos import trainer
from Storage.Datos.datos import camper




def AllTrainers():
    bandera=True
    while (bandera):
        system("clear")
        print("""
        ************************
        *  Filtro del trainer  *
        ************************
        """)
        for i,val in enumerate(trainer):
            print(f"""
________________________
Codigo: {i}
Nombre: {val.get('Nombre')}
Apellido: {val.get('Apellido')}
Identifiacion: {val.get('Identifiacion')}
Edad: {val.get('Edad')}
Telefono: {val.get('Telefono')}
Disponibilidad: {val.get('Disponibilidad')}
Campers: {val.get('Campers')}
________________________
""")
        Codigo = int(input("Ingrese el Codigo del trainer especifico que desea filtrar \n"))
        system("clear")
        print(f"""
________________________
Codigo: {Codigo}
Nombre: {trainer[Codigo].get('Nombre')}
Apellido: {trainer[Codigo].get('Apellido')}
Identifiacion: {trainer[Codigo].get('Identifiacion')}
Edad: {trainer[Codigo].get('Edad')}
Telefono: {trainer[Codigo].get('Telefono')}
Disponibilidad: {trainer[Codigo].get('Disponibilidad')}
Campers: {trainer[Codigo].get('Campers')}
________________________
        """)
        print("¿Desea filtrar otro Trainer? \n")
        print("1. Si")
        print("2. No")
        print("3. Salir\n")
        opc = int(input("Seleccione su opcion \n"))
        if (opc == 1):
            system("clear")
            bandera = True
        if (opc == 2):
            system("clear")
            menu()
        if (opc == 3):
            bandera = False
            system("clear")
            
def AreasEntrenamiento():
    bandera=True
    while (bandera):
        system("clear")
        print("""
        **************************************
        *  Filtro de Areas de entrenamiento  *
        **************************************
        """)
        for i,val in enumerate(Areas):
            print(f"""
________________________
Codigo: {i}
Nombre: {val.get('Nombre')}
Ruta: {val.get('Ruta')}
Trainer: {val.get('Trainer')}
Campers: {val.get('Campers')}
________________________
""")
        Codigo = int(input("Ingrese el Codigo del Area especifico que desea filtrar \n"))
        system("clear")
        print(f"""
________________________
Codigo: {Codigo}
Nombre: {Areas[Codigo].get('Nombre')}
Ruta: {Areas[Codigo].get('Ruta')}
Trainer: {Areas[Codigo].get('Trainer')}
Campers: {Areas[Codigo].get('Campers')}
________________________
        """)
        print("¿Desea filtrar otra Area? \n")
        print("1. Si")
        print("2. No")
        print("3. Salir\n")
        opc = int(input("Seleccione su opcion \n"))
        if (opc == 1):
            system("clear")
            bandera = True
        if (opc == 2):
            system("clear")
            menu()
        if (opc == 3):
            bandera = False
            system("clear")

def RutasEntrenamiento():
    bandera=True
    while (bandera):
        system("clear")
        print("""
        **************************************
        *  Filtro de Rutas de entrenamiento  *
        **************************************
        """)
        for i,val in enumerate(Rutas):
            print(f"""
________________________
Codigo: {i}
Nombre: {val.get('Nombre')}
Tema: {val.get('Tema')}
________________________
""")
        Codigo = int(input("Ingrese el Codigo de la Ruta especifica que desea filtrar \n"))
        system("clear")
        print(f"""
________________________
Codigo: {Codigo}
Nombre: {Rutas[Codigo].get('Nombre')}
Tema: {Rutas[Codigo].get('Tema')}
________________________
        """)
        print("¿Desea filtrar otra Ruta? \n")
        print("1. Si")
        print("2. No")
        print("3. Salir\n")
        opc = int(input("Seleccione su opcion \n"))
        if (opc == 1):
            system("clear")
            bandera = True
        if (opc == 2):
            system("clear")
            menu()
        if (opc == 3):
            bandera = False
            system("clear")

def Temarios():
    bandera=True
    while (bandera):
        system("clear")
        print("""
        ************************
        *  Filtro de Temarios  *
        ************************
        """)
        for i,val in enumerate(Temas):
            print(f"""
________________________
Codigo: {i}
codigo: {val.get('codigo')}
nombre_modulo: {val.get('nombre_modulo')}
temario: {val.get('temario')}
________________________
""")
        Codigo = int(input("Ingrese el Codigo del Tema especifico que desea filtrar \n"))
        system("clear")
        print(f"""
________________________
Codigo: {Codigo}
codigo: {Temas[Codigo].get('codigo')}
nombre_modulo: {Temas[Codigo].get('nombre_modulo')}
temario: {Temas[Codigo].get('temario')}
________________________
        """)
        print("¿Desea filtrar otra Tema? \n")
        print("1. Si")
        print("2. No")
        print("3. Salir\n")
        opc = int(input("Seleccione su opcion \n"))
        if (opc == 1):
            system("clear")
            bandera = True
        if (opc == 2):
            system("clear")
            menu()
        if (opc == 3):
            bandera = False
            system("clear")

def menu():
    bandera = False
    while (bandera):
        print("""***************************
SISTEMA DE REPORTES Y FILTROS
*****************************
""")
    print("        * SISTEMA DE FILTROS * \n")    
    print("\t1. Filtrar todos los Trainers")
    print("\t2. Filtrar Areas de entrenamiento")
    print("\t3. Filtrar Rutas de entrenamiento")
    print("\t4. Filtrar Temarios")
    print("\t5. Filtrar Campers Preinscritos")
    print("\t6. Filtrar Campers Inscritos")
    print("\t7. Filtrar Campers Aprobados")
    print("\t8. Filtrar Campers En Riesgo")
    print("\t9. Filtrar Campers Filtrados")
    print("\t0. Salir \n")
    opc = int(input("seleccione la opcion del filtro que desea buscar \n"))
    match(opc):
        case 1: AllTrainers()
        case 2: AreasEntrenamiento()
        case 3: RutasEntrenamiento()
        case 4: Temarios()
        case 0: bandera = False
        case _: print(menuNoValid(opc))
    