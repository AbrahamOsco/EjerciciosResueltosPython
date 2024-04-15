def saludarVaca():
    print("Hola vaquita come chocolate")

def saludarToro():
    print("Hola toro como estas? ")


def repasarListas():
    lista = ["40", 1 , True, "Hola Vaca"]
    print(lista)
    lista.append("La Vaca Lola")
    lista.insert(0, 750)
    lista.remove(1)
    numerica = [1, 30 , -3, 80, 30]
    # Sort ordenamiento implace 
    #numerica.sort() # ordenar ASCENDENTE forma por defecto en la informatico. 
    unaNuevaNumerica = sorted(numerica)
    print(numerica)
    print(unaNuevaNumerica)
    for c in "La vaca lola":
        print(c, end="@")
    unNombre = " Mi NombRe Es RiCARDo"
    nombreUpper = unNombre.upper() 
    print(nombreUpper)
    
    listaLoca = [ saludarVaca, saludarToro ]
    for f in listaLoca:
        f()
        

def calcularListas():
    datos = [ ['Ricardo', "Sol", 17, 20], ["Felipe", "Enrique", 40, 30] ]
    print(datos[0][2])
    print(datos[1][0])
    return (datos[0][0], datos[1][0])

def jugarTuplas(unaTupla):
    print(unaTupla, unaTupla[0])
    for t in unaTupla:
        print(t)

def jugarMatrices():
    datos = [ ['Ricardo', "Sol", 17, 20],
              ["Felipe", "Enrique", 40, 30],
              ["Abraham", "Antiheroe", 50, 50]]
    for lista in datos:
        for elemento in lista:
            print(elemento, end=' ')
        print('')

# Ejercico de final
# Hacer una funcion que retorne una matriz de 4 filas y 5 columnas llenas de numeros random q van
# del 0 al 10
import random as r
def getMatriz():
    filas = 4
    columnas = 5 
    tablero = []
    for i in range(0, filas):
        unaFila = []
        for j in range(0, columnas):
            unaFila.append(r.randint(0, 9))
        tablero.append(unaFila)
    return tablero, filas, columnas

def printearTablero(tablero, filas, columnas):
    for i in range(0, filas):
        print("--"*filas)
        for j in range(0, columnas):
            print(tablero[i][j], end='|')
        print('')
    print("--"*filas)

def jugarDiccionarios():
    diccionario = {"Ricardo": 40, "Felipe": 10}
    #print(diccionario["Ricardo"])
    #print(diccionario["Felipe"])
    diccionario["Sol"] = 45
    diccionario["Cristian"] = 37
    diccionario["Felipe"] = 50
    diccionario["Vaca"] = 100
    for elemento in diccionario:
        print(elemento)
    for elemento in diccionario.items():
        clave, valor = elemento
        print(f'{clave} y {valor}')
        #print(elemento)

    """ 
    for clave in diccionario.keys():
        print(clave)
    for valor in diccionario.values():
        print(valor)
    
    if "pepe" in diccionario.keys():
        print("pepe es clave")
    else: 
        print("Pepe no es clave")
    diccionario.pop("Vaca")
    valor = diccionario.get("Vaca Lola", 50000000)
    #print(valor)
    """


def main():
    #repasarListas()
    #tuplaLoca = calcularListas()
    #jugarTuplas(tuplaLoca)
    #jugarMatrices()
    #tablero, fila, columna = getMatriz()
    #printearTablero(tablero, fila, columna)
    jugarDiccionarios()


main()