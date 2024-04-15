import random as r
def pruebaRandom():
    #r.seed(7) # reproducimos lo aleatorio 
    numAleatorio =  r.randint(0,20)
    numFlotante = round(r.uniform(3.5, 5.8), 2)
    elemento = r.choice(["Sebatian", "Gonzalo", "Victor", "Trazabilidad"])
    print(numAleatorio, numFlotante, elemento)

""" 
Crear una función que genere un numero aleatorio entre 100.0 mil y 900.0 mil
y retorne en qué categoría de ingresos se encuentra (baja (<100k),
media (<600k),  alta).
"""
def getCategoria():
    unIngreso = round(r.uniform(100000.0, 900000.0), 2)
    print(unIngreso)
    if (unIngreso <= 100000):
        print("Categoria Baja")
    elif (unIngreso > 100000 and unIngreso <= 600000):
        print("Categoria Media")
    elif (unIngreso > 600000):
        print("Categoria Alta")
    return unIngreso


#getCategoria()

""" Crear una función que genere tres números random  
enteros los muestre en orden ascendente y  retorna el mayor.
""" 

def obtenerMayor(num1, num2):
    mayor = num1
    if( num2 >= num1):
        mayor = num2
    return mayor

def obtenerMenor(num1, num2):
    menor = num1 #supongamos que el mas chico es num1
    if (num2 <= num1):
        menor = num2
    return menor 

def getMayorDe3NumRandom():
    num1 = r.randint(1, 100)
    num2 = r.randint(1, 100)
    num3 = r.randint(1, 100)
    print(num1, num2, num3)
    mayorAux1 = obtenerMayor(num1, num2)
    numMasGrande = obtenerMayor(mayorAux1, num3)
    top2 = 0 
    if(numMasGrande == mayorAux1):
        numAux = obtenerMenor(num1, num2)
        top2 = obtenerMayor(numAux, num3) 
    elif ( numMasGrande == num3):
        top2 = mayorAux1
    menorAux1 = obtenerMenor(num1, num2)
    numMasChico = obtenerMenor(menorAux1, num3)
    
    print(f" {numMasChico} {top2} {numMasGrande}")
    return numMasGrande

def getMayorDe3NumRandomVersion2():
    num1 = r.randint(1, 100)
    num2 = r.randint(1, 100)
    num3 = r.randint(1, 100)
    print(num1, num2, num3)
    listaNum = [num1, num2, num3]
    listaNum.sort()
    print(listaNum)

#getMayorDe3NumRandomVersion2()

"""
Crear una función que elija entre un tipo de vehículo 
(coche, moto, bicicleta) de forma aleatoria y retorne qué tipo de vehículo 
conduce según la categoría.
"""
def getCategoriaVehiculo():
    vehiculos = ["coche", "moto", "bicicleta"]
    vehiculoSeleccionado =  r.choice(vehiculos)
    print(f"RANDOM: {vehiculoSeleccionado}")
    if (vehiculoSeleccionado == "coche"):
        print("CATEGORIA COCHE")
    elif ( vehiculoSeleccionado == "moto"):
        print("CATEGORIA MOTO")
    elif ( vehiculoSeleccionado == "bicicleta"):
        print("CATEGORIA BICICLETA")
    return vehiculoSeleccionado

getCategoriaVehiculo()