def ejemploWhile():
    i = 0        
    while ( i < 15):
        if ( i == 7):
            print("Entro al if ")
            return i   
        print(f"Dentro del while i es {i} ")
        i += 1
    print(f"Sali del while i vale: {i}")
    print("TERMINO la funcion")

def calcularNumeros(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    producto = num1 * num2
    return suma, resta, producto #empaquetamiento

def aplicarTuplas():
    result1, result2, result3 = calcularNumeros(3, 4) # desempaquetando
    tuplaCompleta = calcularNumeros(3, 4) 
    print(f" re1 {result1} re2: {result2} re3: {result3} ")    
    print(tuplaCompleta)

""" 
Crea un programa que calcule la suma de los números 
pares del 1 al 10 usando un bucle.
"""
def getSumaNum1Al10():
    cantNumeros = int(input("Ingrese la cantidad de numeros que tiene: "))
    while ( i <= cantNumeros):
         if ( i % 2 == 0):
            acumulador += i
         i += 1
    return acumulador




