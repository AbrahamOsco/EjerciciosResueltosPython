""" 
Crear una función que solicite 3 números al usuario, luego muestra la suma acumulativa de
todos los números ingresados. si uno de los números ingresado es cero, muestra la suma actual
y retorna la suma actual.
"""
def getSumaAcumulativa():
    sumaTotal = 0
    num1 = int(input("Ingrese un numero: "))
    if (num1 == 0):
        print(f"Suma Actual : {sumaTotal}")
        return sumaTotal
    sumaTotal += num1
    num2 = int(input("Ingrese un numero: "))
    if (num2 == 0):
        print(f"Suma Actual : {sumaTotal}")
        return sumaTotal
    sumaTotal += num2
    num3 = int(input("Ingrese un numero: "))
    if (num3 == 0):
        print(f"Suma Actual : {sumaTotal}")
        return sumaTotal
    sumaTotal += num3
    print(f"Suma Actual : {sumaTotal}")
    return sumaTotal

def main():
    getSumaAcumulativa()

main()