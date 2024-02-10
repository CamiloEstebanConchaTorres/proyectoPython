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
    print("\t3. Registro/Actualizacion del camper")
    print("\t4. Registro/Actualizacion del Trainer")
    print("\t5. Reportes(FILTROS)")
    print("\t0. Salir \n")
    
bandera = True
while (bandera):
    menu()
    opc = int(input("ingrese el numero del modulo al que desea ingresar \n"))
    match(opc):
        case 1:
            with open("Storage/Rutas_entrenamiento/rutas.json", "r") as f:
                Asignacion.Rutas = json.loads(f.read())
                f.close()
            with open("Storage/Rutas_entrenamiento/temas.json", "r") as f:
                Asignacion.Temas = json.loads(f.read())
                f.close()
            with open("Storage/Areas_entrenamiento/areas.json", "r") as f:
                Asignacion.Areas = json.loads(f.read())
                f.close()
            with open("Storage/trainers/trainer.json", "r") as f:
                Asignacion.trainer = json.loads(f.read())
                f.close()
            with open("Storage/Campers/camper.json", "r") as f:
                Asignacion.camper = json.loads(f.read())
                f.close()                                          
                system("clear")
                Asignacion.menu()
        case 2:
            with open("Storage/Campers/camper.json", "r") as f:
                Evaluacion_Camper.camper = json.loads(f.read())
                f.close()
            with open("Storage/Campers/Inscritos.json", "r") as f:
                Evaluacion_Camper.Inscrito = json.loads(f.read())
                f.close()
            with open("Storage/Campers/Aprobados.json", "r") as f:
                Evaluacion_Camper.Aprobado = json.loads(f.read())
                f.close()
            with open("Storage/Campers/En_riesgo.json", "r") as f:
                Evaluacion_Camper.En_riesgo = json.loads(f.read())
                f.close()
            with open("Storage/Campers/Filtrados.json", "r") as f:
                Evaluacion_Camper.Filtrado = json.loads(f.read())
                f.close()          
                system("clear")
                Evaluacion_Camper.menu()
        case 3:
            with open("Storage/Campers/camper.json", "r") as f:
                Registro_Campers.camper = json.loads(f.read())
                f.close()
            with open("Storage/Campers/Preinscritos.json", "r") as f:
                Registro_Campers.Preinscritos = json.loads(f.read())
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
            with open("Storage/trainers/trainer.json", "r") as f:
                Reportes.trainer = json.loads(f.read())
                f.close()
            with open("Storage/Campers/camper.json", "r") as f:
                Reportes.camper = json.loads(f.read())
                f.close()
            with open("Storage/Areas_entrenamiento/areas.json", "r") as f:
                Reportes.Areas = json.loads(f.read())
                f.close()
            with open("Storage/Rutas_entrenamiento/rutas.json", "r") as f:
                Reportes.Rutas = json.loads(f.read())
                f.close()
            with open("Storage/Rutas_entrenamiento/temas.json", "r") as f:
                Reportes.Temas = json.loads(f.read())
                f.close()
            with open("Storage/Campers/Preinscritos.json", "r") as f:
                Reportes.Preinscritos = json.loads(f.read())
                f.close()
            with open("Storage/Campers/Inscritos.json", "r") as f:
                Reportes.Inscrito = json.loads(f.read())
                f.close()
            with open("Storage/Campers/Aprobados.json", "r") as f:
                Reportes.Aprobado = json.loads(f.read())
                f.close()
            with open("Storage/Campers/En_riesgo.json", "r") as f:
                Reportes.En_riesgo = json.loads(f.read())
                f.close()
            with open("Storage/Campers/Filtrados.json", "r") as f:
                Reportes.Filtrado = json.loads(f.read())
                f.close()                                                        
                system("clear")
                Reportes.menu()                           
        case 0:
            system("clear")
            bandera = False, system("clear")
        case _:
            print(menuNoValid(opc))