""" 
    EJERCICIO: Crear un funcion que reciba una y que 
    agrege elementos sin repetir, por ej si agrege el 3 
    dos veces la lista solo debe tener un 3
"""
def addElementSinRepetir(lista, elemento):
    if lista.count(elemento) == 0:
        lista.append(elemento)
    

def probarLista():
    numeros = []
    numeros.append(1)
    numeros.append(2)
    numeros.append(3)
    numeros.append(4)
    numeros.insert(1, "Anthony")
    numeros.insert(500, "ruiz")
    try:
        numeros.remove("gonza")
    except ValueError:
        print("No se puede eliminar el valor 'gonza' porque no existe en la lista")
    numeros.insert(500, "ruiz")
    return numeros


def probarSort(lista :list):
    unaNuevaLista = sorted(lista)
    print(unaNuevaLista)
    print(lista)
    #lista.sort()
    #print(lista)

def ejercitarStrings():
    nombre = "Anthony y Leonardo"
    for letra in nombre:
        print(letra)

"""
Escribe una función que tome una lista de
números como parámetro y devuelva la suma de todos 
los elementos de la lista.
"""
def sumarElementos(unaLista):
    sumaTotal = 0
    for elemento in unaLista:
        sumaTotal += elemento
    return sumaTotal

""" 
Crea una función que tome una lista de 
números y devuelva el resultado de multiplicar 
todos los números pares de la lista.
"""
def multiplicarPares(unaLista):
    productoResult = 1
    for elemento in unaLista:
        if elemento % 2 == 0:
            productoResult *= elemento
    return productoResult


"""
Escribe una función que tome una lista como parámetro y devuelva una nueva
lista donde cada elemento esté duplicado.
"""
def duplicarLista(unaLista):
    listaDuplicada = []
    for elemento in unaLista:
        listaDuplicada.append(elemento)
        listaDuplicada.append(elemento)
    print(unaLista)
    print(listaDuplicada)
    return listaDuplicada

def main():
    print(probarLista())
    listaLoca = [3, "anthony", 4, 3.0, "0.1"]
    addElementSinRepetir(listaLoca, 3)
    listaNumerica = [ 3, -4, 10, -100, 40, 34.1]
    probarSort(listaNumerica)    
    ejercitarStrings()
    print(sumarElementos([3, 4, 5, 10, 20]))
    unaLista = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(multiplicarPares(unaLista))
    duplicarLista(listaLoca)
main()
