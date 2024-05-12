import csv

def trabajarArchivosInicial():
    archivo = open("matias.txt", "w")
    for i in range(0, 10):
        archivo.write(f"La linea del for es: {i} 🔥\n")
    archivo.close()

def appendearLastLine():
    archivo = open("matias.txt", "a")
    archivo.write("Agrego otra linea 🤽\n")
    archivo.close()

def leerArchivo():    
    archivo = open("matias.txt", "r")
    lineas = []
    for linea in archivo:
        linea = linea.rstrip('\n')
        lineas.append(linea)
    print(f"lineas {lineas}")

def lecturaSinCloseYConEnumerate():
    with open('matias.txt', 'r+') as archivo:
        archivo.write("Escribo una linea mas 🦅\n")
        for i, linea in enumerate(archivo, 500):
            print(f"i: {i}, linea {linea}", end="")

    #archivo.write("Intento escribir") No tiene sentido escribir en un archivo que esta cerrado.
def abrirImagen():
    with open('toy.png', "rb") as archivoSasuke:
        position = archivoSasuke.tell()
        quinceBytes = archivoSasuke.read(15)
        print(f"diezBytes: {quinceBytes}")
        archivoSasuke.seek(100)
        position = archivoSasuke.tell()
        print(f"position: {position}")
        totalData = archivoSasuke.read() # prohibido hacer en el tp1
        print(f"totalData: {totalData}")

def leerCSV():
    with open("estudiantes.csv", "r") as studentFile:
        csvReader = csv.reader(studentFile, delimiter=',')
        headers = next(csvReader, None)
        students = []
        print(f"headers: {headers}")
        for linea in csvReader:
            students.append(linea)
        print(students)
    
def escribirCSV():
    matriz = [
              ["Vaca", "Lola", "Si", 3 ], 
              ["Toro", "Lolo", "Si", 4 ], 
              ["Burro", "maria", "Si", 9 ], 
              ["Pato", "gallo", "Si", 10 ], 
              ["Lobo", "Lola", "No", 10 ] ]
    with open("MiPrimer.csv", "w") as archivoCSV:
        writer = csv.writer(archivoCSV)
        writer.writerow(["Tipo De Animal", "Nombre", "esDomestico?", "edad"])
        writer.writerows(matriz)
     

def main():
    #trabajarArchivosInicial()    
    #appendearLastLine()
    #leerArchivo()
    #lecturaSinCloseYConEnumerate()
    #abrirImagen()
    leerCSV()
    #escribirCSV()
    
main()

