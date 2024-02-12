
# Gracias @zulema por el ejemplo
def pruebaListas():
    datosJuan = ['Juan', 'Perez', 30, True]
    for i in datosJuan:
      print(i)
    
    for i in range(0, len(datosJuan)):
       print(datosJuan[i])


""" 
Escribir una función que pide al usuario una cantidad de numeros a
ingresar y luego que determine para cada numero entero ingresado: 
    a) Si el número entero n, indicar si es par o no.
    b) Si el número entero n, indicar si es primo o no.
"""


def esPar(x):
   return (x % 2 == 0)
"""   if ( x % 2 == 0):
      return True
   else:
      return False
"""

def sonNumerosPares():
    cantIngresos = int(input('Ingrese la cantidad de numeros a ingresar: '))
    for i in range(0, cantIngresos):
       unNumero = int(input('Ingrese un numero: '))
       print(f"Con {unNumero} el resultado de si es par es {esPar(unNumero)} ")

def esPrimo(num):
   for i in range(2, num):
      if(num % i == 0):
         return False
   return True


def serieParPrimo():
  cantidad = int(input("Ingrese la cantidad de numeros a ingresar:"))
  for i in range(0, cantidad):
     num = int(input(f"Ingrese el {i+1}  numero: "))
     if(esPar(num)):
        print(f"en numero: {num}   es Par ")

     if(esPrimo(num)):
        print(f"en numero: {num}   es Primo ")


def main():
    #sonNumerosPares()
    serieParPrimo()
main()

