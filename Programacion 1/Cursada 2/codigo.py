""" Escribir un programa que le pida al usuario que ingrese una sucesión de números
naturales (primero uno, luego otro, y así hasta que el usuario ingrese ’-1’ como
condición de salida). Al final, el programa debe imprimir cuántos números fueron
ingresados, la suma total de los valores y el promedio.
"""
def printearSumYPromedio(unaSumaTotal, unaCantNum):
    print(f'La suma total de valores es: {unaSumaTotal}')
    promedio = round(unaSumaTotal/unaCantNum, 2) 
    print(f'El promedio calculado es : {promedio}')

def getCalculoNumeros():
    sumaTotal = 0 
    cantNumero = 0
    numIngresado = 0
    while (numIngresado != -1):
        numIngresado = int(input('Ingrese un numero natural: (-1: para cortar el ciclo) : '))
        if(numIngresado < 0 ):
            print('Error debe ingresar un numero natural ')
            continue
        cantNumero += 1
        sumaTotal += numIngresado       
    printearSumYPromedio(sumaTotal, cantNumero)

