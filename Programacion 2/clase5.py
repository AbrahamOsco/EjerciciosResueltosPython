import random as r
""" 
Escribir una función, llamada head que reciba una ruta de un archivo y un número N e imprima las
primeras N líneas del archivo.
"""
def head(unaRuta, cantLineas:int):
    with open(unaRuta, "r") as unArchivo:
        for i,linea in enumerate(unArchivo, 0): 
            if ( i >= cantLineas ):
                break
            print(linea, end="")
"""
Escribir una función, llamada wc (word counter), que dado un archivo de texto, lo procese e imprima por
pantalla cuántas líneas, cuantas palabras y cuántos caracteres contiene el archivo
"""
def wordCounter(unaRuta):
    with open(unaRuta, "r") as unArchivo:
        cantLineas = 0
        cantPalabras = 0
        cantCaracteres = 0
        for linea in unArchivo:
            linea = linea.rstrip('\n')
            palabras = linea.split(' ')
            cantPalabras += len(palabras)
            print(f"palabras: {palabras}")
            for unaPalabra in palabras:
                cantCaracteres += len(unaPalabra)
            cantLineas +=1
        print(f"Lineas: {cantLineas}  Palabras: {cantPalabras} Caracteres: {cantCaracteres} ")
        
"""
Escribir una función, llamada grep, que reciba una cadena y un 
archivo e imprima las líneas del archivo que contienen la cadena recibida.
"""
def grep(unaRuta, stringBuscado:str):
    with open(unaRuta, "r") as unArchivo:
        for linea in unArchivo:
            if (linea.find(stringBuscado) >=0 ):
                print(linea, end="")    

"""
Desarrolla un programa que tome dos CSV de Estudiante.csv y Notas.csv y realice
un apareo de registros basado (en un campo que identifica de forma unívoca al alumno ->idEstudiante)
combinando/joineando/mergeando la información de ambos archivos en un nuevo archivo
"""
import csv

def escribirReporte(estudiantes: dict):
    matriz = []
    for clave,valor in estudiantes.items():
        for materia, nota in valor[1]:
            registro = [clave, valor[0], materia, nota]
            matriz.append(registro)
        if( len(valor[1]) == 0 ):
            matriz.append([clave, valor[0], " ", " "])
        
    with open("datosCompletos.csv", "w") as fileEstudiantes:
        writer = csv.writer(fileEstudiantes)
        writer.writerow(["idEstudiante", "Nombre", "materia", "nota"])
        writer.writerows(matriz)                  
            
def joinArchivosCSV(rutaEstudiante, rutaNotas):
    with open(rutaEstudiante, "r") as fileEstudiante , open(rutaNotas, "r") as fileNotas:
        csvReaderStudent = csv.reader(fileEstudiante, delimiter=',')
        csvReaderNotas = csv.reader(fileNotas, delimiter=',')
        next(csvReaderStudent, None)
        next(csvReaderNotas, None)
        estudiantes = {}
        for linea in csvReaderStudent:
            estudiantes[linea[0]] = [linea[1], [] ]
        # cargado todos los estudiantes. en el dic estudiantes.
        for linea in csvReaderNotas:
            estudiantes[linea[0]][1].append((linea[1], linea[2]))
        print(estudiantes)
        escribirReporte(estudiantes)
        
def main():
   #head("archivo.txt", 500)
   #wordCounter("archivo.txt")
   #grep("archivo.txt", "gonza")
   joinArchivosCSV("estudiantes.csv", "notas.csv")
   

main()
