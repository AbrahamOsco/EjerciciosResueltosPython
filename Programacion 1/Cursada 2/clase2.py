""" 
Escribe una funcion que solicite al usuario dos
números y luego muestre la suma y resta de esos dos números.
"""

def sumarNumeros():
    numero1 = int(input("Ingrese un numero: "))
    numero2 = int(input("Ingrese otro numero: "))
    suma = numero1 + numero2
    resta = numero1 - numero2
    print(f"La suma es: {suma}")    
    print(f"La resta es: {resta}")    

