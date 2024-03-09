""" 
Crear una función que pregunte la edad del usuario y muestre qué categorías
de peliculas puede ver: peliculas para todas las edades (1 a 100),
mayores de 12 o mayores de 18. 
"""

def mostrarCategDisponible():
    edad = int(input("Ingrese su edad: "))
    if ( edad <=0 or edad >100 ):
        print("ERROR: Ingrese una edad entre 1 y 100 ")
        return
    if (edad >=1 and edad <= 100 ):
        print("Peliculas para todas las edades")
    if ( edad >=12 ):
        print("Peliculas para adolescentes ")
    if ( edad >= 18 ):
        print("Peliculas para adultos ")

""" 
Crear una función que solicite al usuario el precio de 
un producto (ej: $550.50) y su descuento (ej: 30.5%), calcule y muestre el
precio final (el producto entre el precio y el descuento)
"""
def calcularPrecioFinal():
    precioIngresado = input("Ingrese un precio del producto: ")
    precioNumString = precioIngresado.replace('$','')
    precio = float(precioNumString)
    
    descuento = float( input("Ingrese un descuento: ").replace('%','') )  
    precioFinal = precio - precio*descuento/100
    print(f"El precio final es ${precioFinal}")
    return precioFinal


#precioFinal  = calcularPrecioFinal()
#print(f"EL resultado de la funcion es: {precioFinal} ")
# mostrarCategDisponible()


""" 
Crear una función que pide al usuario un número y verifica en qué rango se encuentra: 
0-10, 11-20, 21-30, o "fuera de rango", debe mostrar el rango en donde esta.
ej: si ingreso 4 debe printear Rango entre (0-10).
"""

def mostrarRango():
    try:    
        numero = int( input("Ingrese un numero: ") )
    except ValueError : # pongo aca el tipo error de error que me sale: 
        print("ERROR: Ingrese un numero y no un texto no numerico")
        return
        
    if (numero >=0 and numero <= 10):
        print("Rango entre (0-10)")
    elif (numero >=11 and numero <=20):    
        print("Rango entre (11-20)")
    elif ( numero >=21 and numero <=30 ):
        print("Rango entre (21-30)")
    elif ( numero < 0 or numero >= 31):
        print("Fuera de rango")

#mostrarRango()
""" 
Crear una función que pide al usuario el mes y determina en qué estación 
del año se encuentra. (Verano, Otoño, Invierno, Primavera). (Cada 3 meses 
calendario corresponde al orden de la estación anterior), debe mostrar 
la estación calculada.
"""
def getEstacionActual():
    dicAntony = { "enero":1, "febrero":2, "marzo":3, "abril":4, "mayo":5, "junio":6, 
                   "julio":7, "agosto":8 , "septiembre":9, "octubre":10, "noviembre":11, "diciembre":12}
    estacionIng = input("Ingrese una estacion: ").lower() # enero, febrero
    if ( not estacionIng in dicAntony.keys() ):
        print("ERROR: ingrese una mes valida")
        return
    valorMes = dicAntony[estacionIng]
    if (valorMes <= 3):
        print("Verano")
    elif (valorMes > 3 and valorMes <= 6):
        print("Otoño")
    elif (valorMes > 6 and valorMes <= 9):
        print("Invierno")
    elif (valorMes > 9 and valorMes <= 12):
        print("Primavera")
  
    return estacionIng

getEstacionActual()
