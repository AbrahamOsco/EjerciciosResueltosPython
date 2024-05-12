import json

def pruebaJson():
    dicAJson = json.dumps( {"hobbies": ("correr", "cantar", "codear", None),
                 "frutas" : ["pera", "manzana", "melon"],
                 "fullName": "Ricardo Gonzalo Mathias",
                 "mascotas": [ {"animal":"Perro", "edad": 3, "pesoEnKg": 45.5},
                               {"animal":"Gato", "edad": 4, "pesoEnKg": 20.5}]
                 }, sort_keys=True, indent=4)
    print(dicAJson)
    #dumps: Serializa los objeto recibido como argumento y 
    # retorna en un string con el formato Json. 

def prubaDump():
    objetoParaSerializar = {"hobbies": ("correr", "cantar", "codear", None),
                 "frutas" : ["pera", "manzana", "melon"],
                 "fullName": "Ricardo Gonzalo Mathias",
                 "mascotas": [ {"animal":"Perro", "edad": 3, "pesoEnKg": 45.5},
                               {"animal":"Gato", "edad": 4, "pesoEnKg": 20.5}]
                 }
    with open("datos.json", "w") as unArchivoJson:
        json.dump(objetoParaSerializar, unArchivoJson, indent=4)
    # Escribimos el objeto serializado en un archivo, le pasamos el objeto el archivo y el indent 

def pruebaLeerJsonCargandoTodoMemoria():
    datosJson: dict = {}
    with open("datos.json","r") as archivoJson:
        datosJson: dict = json.load(archivoJson)
    
    nombres = datosJson.get("fullName", "")
    mascotas = datosJson.get("mascotas", "")
    hobbies = datosJson.get("hobbies", "")
    
    print(f"nombres: {nombres}\n Mascotas: {mascotas}\n Hobbies {hobbies}")

def pruebaLeerJsonDesdeUnString():
    jsonStr = '''
        {"hobbies":["correr","cantar","codear",null],"frutas":["pera","manzana","melon"],
        "fullName":"Ricardo Gonzalo Mathias","mascotas":[{"animal":"Perro","edad":3,"pesoEnKg":45.5},
        {"animal":"Gato","edad":4,"pesoEnKg":20.5}]}
    '''
    datosJson =  json.loads(jsonStr)
    nombres = datosJson.get("fullName", "")
    mascotas = datosJson.get("mascotas", "")
    hobbies = datosJson.get("hobbies", "")
    
    print(f"nombres: {nombres}\n Mascotas: {mascotas}\n Hobbies {hobbies}")

def main():
    #pruebaJson()
    #prubaDump()
    #pruebaLeerJsonCargandoTodoMemoria()
    pruebaLeerJsonDesdeUnString()
    
main()