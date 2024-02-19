def appendSinRepetidos(unaLista, unValor):
    if (unaLista.count(unValor) == 0 ):
        unaLista.append(unValor)

def pruebaListas():
    listaLoca = [30, "juan perez", True, 50]
    listaLoca.insert(0, "La vaca")
    listaLoca.remove(50)
    valorAInsertar = "La vaca"
    appendSinRepetidos(listaLoca, valorAInsertar)
    print(listaLoca)
    print(len(listaLoca))

def pruebaStrings():
    edad = 20
    nombre = "Juan perez Ricardo " + str(edad)
    for caracter in nombre:
        print(caracter, end='')

"""
Escribe una función que tome una lista de números como parámetro y devuelva la
suma de todos los elementos de la lista.
"""
def sumarNumeros(unaLista):
    sumaAcumulador = 0 
    for numero in unaLista:
        sumaAcumulador += numero
    return sumaAcumulador

""" 
Crea una función que tome una lista de números y devuelva el resultado de multiplicar 
todos los números pares de la lista.
"""
def getProductoPares(unaLista):
    acumulador = 1
    for numero in unaLista:
        if (numero % 2 == 0):
            acumulador *= numero
    return acumulador

def duplicarLista(unaLista):
    for i in range(0, len(unaLista)):
        unaLista.insert(i*2, unaLista[i*2])
    return unaLista

def duplicar2(unaLista):
    [elemento for elemento in unaLista for _ in range(2)]
    print(unaLista)

def main():
    #pruebaStrings()
    #pruebaListas()
    listaLoca = [3, 4, 10, 2, 4, -1 ,3]
    print(sumarNumeros(listaLoca))
    print(getProductoPares(listaLoca))
    print(duplicarLista(listaLoca))
    duplicar2(listaLoca)
main()