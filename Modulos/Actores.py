import json

path = "Storage/"
def carga():
    with open(path+"actores.json", "r") as f:
        return json.loads(f.read())