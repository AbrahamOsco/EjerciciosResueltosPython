numLoco = 0 # variable global
CANT_DIAS_SEMANA = 7 # constante
IMPUESTO_PAIS = 30.4

def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return (num1 - num2)*numLoco

def dividir(num1, num2):
    return (num1 + num2)*numLoco

# PRE: num1 y num2 son numeros positivos. 
# POST: retorna el sueldo

def printearReporte():
    for i in "litaEmpleados":
        print(i, end='')

def calculoSueldo(sueldoBruto, tasaEfectiva):
    printearReporte()            
    return sueldoBruto*tasaEfectiva - IMPUESTO_PAIS/100

def ejemploFor():
    for i in [1, 3, 5, 7]:
        print(f" el valor de i es {i**2}", end="@\n") 

def ejemplListas():
    unaLista = ["ANTONY", "Juan", "Isabela", 40.0, True]
    print(unaLista)
""" 
Escribir una función que pide al usuario una cantidad de numeros a ingresar y
luego que determine para cada numero entero ingresado:
a) Si el número entero 𝑛, indicar si es par o no.
"""

def esPar(unNumero):
    return (unNumero % 2 == 0)


def calcularSiEsPar():
    cantNumeros = int(input("Ingrese la cantidad de numeros que tiene: "))
    for i in range(0, cantNumeros):
        unNumero = int(input("Ingrese un Numero: "))
        if (esPar(unNumero)):
            print("El numero es Par")
        else: 
            print("El numero es impar")
    

def main():
    calcularSiEsPar()

main()
