# IMPORTACION DE LIBRERIAS Y OTRAS FUNCIONALIDADES DE PYTHON #
from os import system
import json

# IMPORTACION DE LOS MODULOS PARA PODER INGRESAR #
from Modulos.Asignaciones import Asignacion
from Modulos.Evaluacion_camper import Evaluacion_Camper
from Modulos.Registro_campers import Registro_Campers
from Modulos.Registro_trainers import Registro_Trainers
from Modulos.Reportes import Reportes
from Modulos.Rutas_entrenamiento import Rutas_Entrenamiento
from Modulos.Areas_entrenamiento import Areas_Entrenamiento
from Storage.Datos.datos import camper
from Storage.Datos.datos import trainer


# IMPORTACION DE VALIDACIONES DE LOS MODULOS #
from Modulos.Validaciones.Validaciones import menuNoValid



print("""*************************************************************
BIENVENIDO AL SISTEMA DE SEGUIMIENTO ACADEMICO DE CAMPUSLANDS
*************************************************************
        CRUD de CAMPUSLANDS
""")
def menu():
    print("\t1. Asignaciones")
    print("\t2. Evaluacion del camper")
    print("\t3. Registro del camper")
    print("\t4. Registro del Trainer")
    print("\t5. Reportes(FILTROS)")
    print("\t6. Rutas de entrenamiento")
    print("\t7. Areas de entrenamiento")
    print("\t0. Salir \n")
    
bandera = True
while (bandera):
    menu()
    opc = int(input("ingrese el numero del modulo al que desea ingresar \n"))
    match(opc):
        case 1:
            system("clear")
            Asignacion.menu()
        case 2:
            system("clear")
            Evaluacion_Camper.menu()
        case 3:
            with open("Storage/Campers/camper.json", "r") as f:
                Registro_Campers.camper = json.loads(f.read())
                f.close()
                system("clear")
                Registro_Campers.menu()
        case 4:
            with open("Storage/trainers/trainer.json", "r") as f:
                Registro_Trainers.trainer = json.loads(f.read())
                f.close()
                system("clear")
                Registro_Trainers.menu() 
        case 5:
            system("clear")
            Reportes.menu()    
        case 6:
            system("clear")
            Rutas_Entrenamiento.menu()
        case 7:
            system("clear")
            Areas_Entrenamiento.menu()                         
        case 0:
            system("clear")
            bandera = False
        case _:
            print(menuNoValid(opc))