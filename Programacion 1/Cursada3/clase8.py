
def operarMatrices():
    listaLoca = [["Juan", "Perez", 20, 30.12],
                 ["Gonz", "Anthony", 3, 10.12],
                 ["luis", "jose", 40, 80.12] ]
    for unaLista in listaLoca:
        for elemento in unaLista:
            print(elemento)
        print(unaLista)

import random as r
""" 
Crear una matriz dinamica que le pida al usuario la fila y la columna 
y que la llena con numeros aleatorios enteros entre 0 y 10 
"""
def crearMatriz():
    fila = int(input("Ingrese una fila: "))
    columna = int(input("Ingrese una columna: "))
    tablero = []
    for i in range(0, fila):
        unaFila = []
        for j in range(0, columna):
            unValorRandom = r.randint(0, 10)
            unaFila.append(unValorRandom)
        tablero.append(unaFila)
    return tablero

def printTablero(unTablero):
    for unaFila in unTablero: 
        print("------------")
        for elemento in unaFila:
            print(elemento, end=" | ")
        print("")
    print("------------")

def ejemploDiccionario():
    unDic = {"Lunes": [100, 101]}
    unDic["Martes"] = "Anthony"
    unDic["Miercoles"] = (3, 30)
    unValor = unDic.get("Miercoles", "FIORELLA")
    retornoPop =  unDic.pop("Miercoles")
    print(unValor)
    print(retornoPop)
    print(unDic)

def main():
    #resultado = operarMatrices()
    #unTablero = crearMatriz() # lista de listas.
    #printTablero(unTablero)
    ejemploDiccionario()
    filas = 3
    print("---"*filas)
main()

