from os import system
from Modulos import Asignacion




from Modulos.Validaciones import menuNoValid






print("""************************************
BIENVENIDO AL SISTEMA DE CAMPUSLANDS
************************************
        CRUD de CAMPUSLANDS
""")
def menu():
    print("\t1. Asignacion")
    print("\t2. Evaluacion del camper")
    print("\t3. Registro del camper")
    print("\t3. Registro de Prueba")
    print("\t3. Registro del Trainer")
    print("\t3. Reportes(FILTROS)")
    print("\t3. Rutas de entrenamiento")
    print("\t0. Salir \n")
    
bandera = True
while (bandera):
    menu()
    opc = int(input("ingrese el numero del modulo al que desea ingresar \n"))
    match(opc):
        case 1:
            system("clear")
            Asignacion.menu()
        case _:
            print(menuNoValid(opc))