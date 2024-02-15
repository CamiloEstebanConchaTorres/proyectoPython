import json

path = "Storage/"
def carga():
    with open(path+"peliculas.json", "r") as f:
        return json.loads(f.read())