# IMPORTACION DE LIBRERIAS Y OTRAS FUNCIONALIDADES DE PYTHON #
import json
from os import system

# IMPORTACION DE LOS MODULOS PARA PODER INGRESAR #
from Modulos.Validaciones.Validaciones import menuNoValid
from Storage.Datos.datos import camper
from Storage.Datos.datos import Estados




def search():
    bandera=True
    while (bandera):
        system("clear")
        print("""
        ***************************
        *  Evaluacion del Camper  *
        ***************************
        """)
        Codigo = int(input("Ingrese el numero del camper al que desea asignar notas \n"))
        print(f"""
________________________
Codigo: {Codigo}
Nombre: {camper[Codigo].get('Nombre')}
Apellido: {camper[Codigo].get('Apellido')}
Identificacion: {camper[Codigo].get('Identificacion')}
Direccion: {camper[Codigo].get('Direccion')}
Edad: {camper[Codigo].get('Edad')}
NombreAcudiente: {camper[Codigo].get('NombreAcudiente')}
NumeroAcudiente: {camper[Codigo].get('NumeroAcudiente')}
idAcudiente: {camper[Codigo].get('idAcudiente')}
TelefonoCamper: {camper[Codigo].get('TelefonoCamper')}
Estado: {camper[Codigo].get('Estado')}
________________________
        """)
        print("¿Este es el camper al que desea asignar nota? \n")
        print("1. Si")
        print("2. No")
        print("3. Salir\n")
        opc = int(input("Seleccione su opcion \n"))
        if (opc == 1):
            Nota_teorica = int(input("ingrese el valor de la nota teorica \n"))
            Nota_Practica = int(input("ingrese el valor de la nota practica \n"))
            Promedio = (Nota_teorica + Nota_Practica) / 2
            if Promedio <= 59:
                return  print("! LO SENTIMOS EL CAMPERO NO HA SUPERADO LA PRUEBA! \n")
            else:
                print("! EL CAMPER HA SUPERADO LA PRUEBA !")
                info = {
                    "Estado": int(input("Asigne el Estado del camper:\n\t"+"\t".join([f"{Estados.index(i)+1}. {i}\n" for i in (Estados)])))            
                }
                camper.append(info)
                with open("Storage/Campers/camper.json", "w") as f: 
                 datos = json.dumps(camper, indent=4)
                 f.write(datos)
                 f.close()
                 return print("! CAMPER ASCENDIDO HA INSCRITOS")            
        elif (opc == 2):
            bandera = False
        elif (opc == 3):
            system("clear")
            bandera = False

            
def menu():
    bandera = True
    while (bandera):
        print("""*******************************
MODULO DE EVALUACION DEL CAMPER
*******************************
CRUD del modulo de Evaluacion del camper
""")
        print("\t1. Prueba Teorica y Practica del camper (Registro de Prueba)")
        print("\t0. Salir \n")
        opc = int(input("seleccione su opcion \n"))
        match(opc):
            case 1: search()
            case 2:
                system("clear")
                bandera = False
            case _: print(menuNoValid(opc))