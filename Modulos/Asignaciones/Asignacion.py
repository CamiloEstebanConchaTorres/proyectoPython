import json
from Storage.Datos import rutas as rutas
from Storage.Datos import datos as datos
from Storage.Datos.datos import Rutas, Temas

Rutas = rutas.carga()
Temas = datos.carga()

# print(rutas)
# print(modulos)

print("CRUD de rutas")
print("1. Asignar modulos a las ruta")
print("2. Buscar")
print("3. Actualizar")
print("4. Eliminar")
opc = int(input())

def plantilla(data):
    lista = []
    for i,val in enumerate(data):
        lista.append(f"\n\t\t{i+1} - {val}")
    return "".join(lista)

def asignarModulos():
    # Temario: {"".join([f"{i} - {val}" for i,val in enumerate(val.get("temario"))])}
    selecion = set()
    nuevaLista = []
    while(True):
        for val in Temas:
            print(f"""
            ________________
            Codigo: {val.get("codigo")}
            Nombre: {val.get("nombre_modulo")}
            Prioridad: {val.get("prioridad")}
            Temario: {plantilla(val.get("temario"))}
            ________________
            """)

        selecion.add(input("¿Selecione el modulo que deseas ingresando el codigo?\n"))
        if(not int(input("¿Deseas agregar otro modulo?\n1.SI\n0.NO\n"))):
            for i in selecion:
                for val in Temas:
                   if(val.get("codigo") == i):
                        nuevaLista.append(val)
            break
    return nuevaLista
match(opc):
    case 1:
        Myruta = {
            "codigo": f"R{len(rutas)+1}",
            "nombre_ruta": input("Ingrese el nombre de la ruta: "),
            "modulo": asignarModulos()
        }
        rutas.append(Myruta)
        path = "module/storage/"
        with open(path+"rutas.json", "w") as f:
            f.write(json.dumps(rutas, indent=4))
            f.close()
    case _:
        print("La opcion no esta habilitada")




