import json

def getDatosJson(unaRuta:str):
    datosJson : dict = {}
    with open(unaRuta, "r") as archivoJson:
        datosJson = json.load(archivoJson)
    return datosJson

def escribirJson(unObjetoJson:dict):
    with open("alumnosUpdate.json", "w") as nuevoArchivoJson:
        json.dump(unObjetoJson, nuevoArchivoJson, sort_keys=True, indent=3)

def agregarMateriaYNotaAAlumnos(unaRuta:str, unaMateria:str, unNota:int):
    datosJson = getDatosJson(unaRuta)

    for dicEstudiante in datosJson["alumnos"]:
        dicEstudiante["notas"][unaMateria] = unNota
    escribirJson(datosJson)

def promedioNotas(unaRuta:str, unaMateria:str):
    datosJson = getDatosJson(unaRuta)
    cantAlumnosConEsaMateria = 0
    acumuladoNotas = 0
    for dicEstudiante in datosJson["alumnos"]:
        dicActual : dict = dicEstudiante["notas"]
        if ( unaMateria in dicActual.keys()):
            cantAlumnosConEsaMateria +=1
            acumuladoNotas += dicActual[unaMateria]
    if(cantAlumnosConEsaMateria == 0):
        print(f"No hay alumnos con la materia {unaMateria}")
        return
    promedio :float = round(acumuladoNotas/cantAlumnosConEsaMateria, 2)
    print(f"La cantida de alumnos con {unaMateria} es {cantAlumnosConEsaMateria} 💯 y el promedio en total es: {promedio}")
    escribirJson(datosJson)


def updateDeNotaAAlumno(unaRuta:str, unNombreAlumno:str, unaMateria:str, unaNota:int ):
    datosJson = getDatosJson(unaRuta)
    for dicEstudiante in datosJson["alumnos"]:
        if (dicEstudiante["nombre"] == unNombreAlumno):
            if( dicEstudiante["notas"].get(unaMateria, "") != "" ):
                dicEstudiante["notas"][unaMateria] = unaNota
            else: 
                print(f"La materia {unaMateria} para el estudiante {unNombreAlumno} no existe! ❌")
            break
        else:
            print(f" El alumno {unNombreAlumno} no existe ! ❌")
            
    escribirJson(datosJson)

def FiltrarEstudiantePorNotaMayorOIgualEnMateria(unaRuta:str, unaMateria:str, unaNotaLimite:int ):
    datosJson = getDatosJson(unaRuta)
    nuevoJson : dict = { "alumnos": [] }
    listaNombres = []
    for dicEstudiante in datosJson["alumnos"]:
        if ( unaMateria in dicEstudiante["notas"].keys() and dicEstudiante["notas"][unaMateria] >= unaNotaLimite):
            listaNombres.append(dicEstudiante["nombre"])
            nuevoJson["alumnos"].append(dicEstudiante)
    print("Nombres de los alumnos que cumple la condicion", listaNombres)
    escribirJson(nuevoJson)


def main():
    agregarMateriaYNotaAAlumnos("alumnos.json", "Programacion 2", 80)
    promedioNotas("alumnos.json", "algo 3")
    updateDeNotaAAlumno("alumnos.json", "Ana", "ciencia", 17)
    FiltrarEstudiantePorNotaMayorOIgualEnMateria("alumnos.json", "ciencia", 90)
main()
