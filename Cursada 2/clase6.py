import logic as l

def printResultados():
    var1 = l.getOperaciones(3)
    var2 = l.sumarNumerosLocos(5, 4)
    print(var1, var2)
"""Crea un programa que calcule y retorne la suma de los  números pares del 1 al 10 
    usando un bucle while."""
# [1, 2, 3, 4, 5, 6, 8, 9, 10] => 48*8*10 

def sumarPares(limite):
    i = 1
    acumulador = 1
    while ( i <= limite):
        if (i %2 == 0):
            acumulador *= i
        i +=1
    return acumulador

"""
Escribe un programa que le pida al usuario ingresar un número e
imprime la tabla de multiplicar de ese número del 1 al 12.
"""
def printearTabla(unNum):
    print(f'TABLA DEL {unNum}' )
    print("---"*5)
    i = 1
    while ( i <= 12):
        print(unNum * i)
        i +=1
    print("---"*5)


def main():
    printearTabla(5)
    printearTabla(2)

main()