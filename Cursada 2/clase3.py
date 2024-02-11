# Clase de hoy 
def esPrimoV1(x):
    for i in range(2, x):
        if (x % i == 0):
            print(" No es primo ")
            return False
    print(" es primo ")
    return True

def esPrimoV2(x):
    contador = 0
    for i in range(2, x):
        if (x % i == 0):
            contador +=1
    return contador
"""
if ( esPrimoV2(10) == 0 ):
    print(" es primo ")
elif (esPrimoV2(10) == 1 ):
    print(" no es primo") 
 """


#Crear una función que pide al usuario la cantidad de
#huevos de gallinas recolectada y retorne en qué tipo de cosecha 
#se encuentra (baja (<100),  media (<300),  alta (>300) ).

def mostrarTipoCosecha():
    huevos = input(" Ingrese la cantidad de huevos: ")
    if (not huevos.isnumeric()):
        return "ERROR: Ingrese un numero entero"        
    huevos = int(huevos)
    if (huevos < 0):
        return 'ERROR: La cantidad de huevos no puede ser negativa'
    elif (huevos < 100):
        return 'Baja'
    elif (huevos >=100 and huevos < 300):
        return 'Media'
    elif (huevos >= 300):
        return 'Alta'

#print(mostrarTipoCosecha())

import random as r  

#r.seed(7)
unaEdad = r.randint(20, 40)
unFlotante = r.uniform(3.5, 9.9)
unaLetra = r.choice(['A', 'B', 'C', 'D', 'E'])

#print(f" {unFlotante} {unaLetra} {unaEdad} ")

def getCategoriaIngreso():
    sueldo = r.uniform(100.0, 900.0)
    sueldo = round(sueldo, 2)
    print(f'{sueldo}')
    if (sueldo < 100):
        return 'Baja'
    elif (sueldo >= 100 and sueldo < 600 ):
        return 'Media'
    elif (sueldo >= 600):
        return 'Alta'

#print(getCategoriaIngreso())


# Crear una función que genere tres números random enteros los muestre 
# de forma ascendente y retorna el mayor.

def getMayor(x, y):
    mayor = x
    if x < y :
        mayor = y
    return mayor

def getMenor(x, y):
    menor = x 
    if x > y:
        menor = y
    return menor


def getMayorNumDe3():
    num1 = r.randint(0, 10)
    num2 = r.randint(0, 10)
    num3 = r.randint(0, 10)
    print(f" {num1} {num2} {num3}")
    numMedio = -1
    mayor1 = getMayor(num1, num2)
    numMasGrande = getMayor(mayor1, num3)
    if (numMasGrande == mayor1):
        numMedio = getMayor(num3, getMenor(num1, num2))
    elif (numMasGrande == num3):
        numMedio = mayor1
    menor1 = getMenor(num1, num2)
    numMasPeque = getMenor(menor1, num3)
        
    print(f" {numMasPeque}, {numMedio} {numMasGrande} " )
    return numMasGrande

getMayorNumDe3()

""" 
Otra solucion con if y elifs
    if ( (num1 == numMasGrande and num2 == numMasPeque) or (num1 == numMasPeque and num2 == numMasGrande)  ):
        numMedio = num3
    elif ( (num2 == numMasGrande and num3 == numMasPeque) or (num2 == numMasPeque and num3 == numMasGrande)  ):
        numMedio = num1
    elif ( (num3 == numMasGrande and num1 == numMasPeque) or (num3 == numMasPeque and num1 == numMasGrande)  ):
        numMedio = num2
"""

