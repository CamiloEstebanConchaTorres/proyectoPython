import json

path = "Storage/"
def carga():
    with open(path+"formatos.json", "r") as f:
        return json.loads(f.read())