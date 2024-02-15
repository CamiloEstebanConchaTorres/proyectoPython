import json

path = "Storage/"
def carga():
    with open(path+"generos.json", "r") as f:
        return json.loads(f.read())