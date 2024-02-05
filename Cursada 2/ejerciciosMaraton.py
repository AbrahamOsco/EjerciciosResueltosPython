"""
1) Crear una función que pregunte la edad del usuario y muestre qué categorías de peliculas puede
ver: peliculas para todas las edades (1 a 100), mayores de 12 o mayores de 18.
"""
def mostrarCategoriasSegunEdad():
     edadUsuario = int(input("Ingrese su edad: "))
     if ( edadUsuario <= 0 or edadUsuario >= 101 ):
        print("Error, ingrese una edad entre 1 y 100 ")
        return "Error" 
     if edadUsuario >= 1 and edadUsuario <= 100:
          print("Puedo ver peliculas infatiles: ")
     if  edadUsuario >= 12: 
          print("Puedo ver peliculas para mayores de 12")
     if edadUsuario >= 18:
          print("Puedo ver peliculas para adultos")
    
# mostrarCategoriasSegunEdad()

""" 
Calculadora de descuento:
Crear una función que solicite al usuario el precio de un producto (ej: $550.50)
y su descuento (ej: 30.5%), calcule y muestre el precio final 
(el producto entre el precio y el descuento). 
"""
def calcularPrecioFinal():
    precio = (input("Ingrese el precio del producto: ")).replace('$','')
    precio = float(precio)
    descuento = (input("Ingrese el descuento del producto: ")).replace('%', '')
    descuento = float(descuento)
    if (precio <= 0 or descuento <= 0):
         print("Error: ingrese un precio y descuento positivos (mayores a 0)")
         return 
    precioFinal = precio - (precio * (descuento/100))
    print(f"Precio final: {round(precioFinal, 2)} ")

#calcularPrecioFinal()

""" 
Rango de números:
Crear una función que pide al usuario un número y verifica en qué rango se encuentra: 0-10,
11-20, 21-30, o "fuera de rango", debe mostrar el rango en donde esta.
"""
def printearRango():
    numero = int(input("Ingrese un numero: "))
    if numero < 0:
        print("ERROR: debe ingresar un numero positivo o cero ")
    elif numero >=0 and numero <= 10:
        print('Esta en el rango entre 0 y 10')
    elif numero >10 and numero <= 20:
        print('Esta en el rango entre 11 y 20')
    elif numero >20 and numero <= 30:
        print('Esta en el rango entre 21 y 30')
    elif numero >30:
        print('Fuera de rango')
    
    
#printearRango()

def mostrarango():
    numero = int(input("Ingresa un numero: "))
    if (numero >= 0 and numero <=10):
        print("Este numero se encuentra en el rango de 0 - 10")
    elif (numero >=11 and numero <=20):
        print("Este numero se encuentra en el rango de 11 - 20")
    elif (numero >=21 and numero <=30):
        print("Este numero se encuentra en el rango de 21-30")
    else:
        print("Este numero no se encuentra en el rango")
#mostrarango()

""" 
Estaciones del año:
Crear una función que pide al usuario el mes y determina en qué estación del 
año se encuentra. (Verano, Otoño, Invierno, Primavera).
(Cada 3 meses calendario corresponde al orden de la estación
anterior), debe mostrar la estación calculada.
"""
def mostrarEstacion():
    unMes = input('Ingrese un mes: ').lower()
    if (unMes == 'enero' or unMes== 'febrero' or unMes == 'marzo'):
        print('Verano')
    elif (unMes == 'abril' or unMes== 'mayo' or unMes == 'junio'):
        print('Otoño')
    elif (unMes == 'julio' or unMes== 'agosto' or unMes == 'septiembre'):
        print('Invierno')
    elif (unMes == 'octubre' or unMes== 'noviembre' or unMes == 'diciembre'):
        print('Primavera')
    else: 
        print('Error: ingrese un mes valido')

mostrarEstacion()
