import json

path = "Storage/Rutas_entrenamiento/"
def carga():
    with open(path+"rutas.json", "r") as f:
        return json.loads(f.read())