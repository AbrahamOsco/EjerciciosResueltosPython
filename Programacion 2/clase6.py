import json
OBJECT_JSON_PRUEBA = { "cantAlumnos": 3, "alumnosInfo":(
        {"nombre": "matias" , "numero": 10},
        {"nombre": "gonzalo" , "numero": 15},
        {"nombre": "cristian" , "numero": 17},   
    ), "fruta": True, "mascotas": None} 

JSON_STR_EXAMPLE = '''  
{
    "alumnosInfo": [
        {
            "nombre": "matias",
            "numero": 10
        },
        {
            "nombre": "gonzalo",
            "numero": 15
        },
        {
            "nombre": "cristian",
            "numero": 17
        }
    ],
    "cantAlumnos": 3,
    "fruta": true,
    "mascotas": null
}
'''


def pruebaJsonWriter():
    miPrimerJsonEnStr = json.dumps(OBJECT_JSON_PRUEBA, sort_keys=True, indent=3)
    print(miPrimerJsonEnStr)
    
    with open("pruebaEnVivo.json", "w") as archivoJson:
          json.dump(OBJECT_JSON_PRUEBA, archivoJson, indent=4, sort_keys=True)

def pruebaJsonReader():
    datosJson : dict = {}
    with open("pruebaEnVivo.json", "r") as archivoReadJson:
        datosJson = json.load(archivoReadJson)
    alumnos = datosJson.get("alumnosInfo", "")
    cantAlumnos = datosJson.get("cantAlumnos", 0)
    tieneFruta = datosJson.get("fruta", 3)
    print(f"{alumnos}\n y cantAlumnos: {cantAlumnos} tieneFruta: {tieneFruta} ")

def pruebaJsonReader2():
    datosJson : dict = json.loads(JSON_STR_EXAMPLE)
    alumnos = datosJson.get("alumnosInfo", "")
    cantAlumnos = datosJson.get("cantAlumnos", 0)
    tieneFruta = datosJson.get("fruta", 3)
    print(f"{alumnos}\n y cantAlumnos: {cantAlumnos} tieneFruta: {tieneFruta} ")


def main():
    #pruebaJsonWriter()
    #pruebaJsonReader()
    pruebaJsonReader2()
    
main()

