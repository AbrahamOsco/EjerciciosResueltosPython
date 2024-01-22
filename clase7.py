""" 
Ejercicio 1
Preguntar la edad del usuario y muestre qué categorías de peliculas puede ver:
peliculas para todas las edades (1 a 100), mayores de 12 o mayores de 18
def mostrarCategoriaPelicula():
    edad = int (input('Che decime tu edad: '))
    if (edad > 1 and edad < 100):
        print('Peliculas para todas las edades')
    if (edad > 12 ):
        print('Peliculas para mayores de 12')
    if ( edad > 18):
        print('Peliculas para mayores de 18 para adultos')

mostrarCategoriaPelicula()
"""

"""
Ejercicio 2
Solicita al usuario el precio de un producto (ej: $550.50) y
su descuento (ej: 30.5%), y calcula el precio final (el producto entre el precio y el descuento). 
def obtenerPrecioFinal():
    precio = float(input('Ingrese el precio del producto: ').replace('$',''))
    descuento = float(input('Ingrese el descuento: ').replace('%', ''))
    precioFinal = precio*descuento/100
    print(precio, descuento, precioFinal)
    return precioFinal
obtenerPrecioFinal()
"""
"""
Ejercicio 3: 
def reportaRango():
    unNumero = int(input('Ingresar un numero: '))
    if ( unNumero >= 0 and unNumero <= 10):
        print('Estoy en el rango de 0 a 10')
    elif ( unNumero >= 11 and unNumero <=20):
        print('Estoy en el rango de 11 a 20')
    elif ( unNumero >=21 and unNumero <= 30):
        print('Estoy en el rango de 21 a 30')
    else:
        print('Fuera de rango')

reportaRango()
"""

"""
Ejercicio 4
Pide al usuario el mes y determina en qué estación del año
se encuentra. (Verano, Otoño, Invierno, Primavera). 
(Cada 3 meses calendario corresponde al orden de la estación anterior).
def reportarEstacion(unMes):
    if (unMes == 'Enero' or unMes == 'Febrero' or unMes == 'Marzo'):
        print('Verano')
    elif (unMes == 'Abril' or unMes == 'Mayo' or unMes == 'Junio'):
        print('Otoño')
    elif (unMes == 'Julio' or unMes == 'Agosto' or unMes == 'Septiembre'):
        print('Invierno')
    elif (unMes == 'Octubre' or unMes == 'Noviembre' or unMes == 'Diciembre'):
        print('Primavera')
    else: 
        print('Error ingrese un mes !!')

reportarEstacion(input('Ingrese un mes: '))
"""

"""
Pregunta al usuario un número del 1 al 7 y retorne el nombre del dia asociado.
(ej: 1- Lunes, 2-Martes, … 7-Domingo).
def obtenerDia():
    unNumero = int(input('Ingrese un numero del 1 al 7: '))
    if (unNumero == 1):
        return 'Lunes'
    elif (unNumero == 2):
        return 'Martes'
    elif (unNumero == 3):
        return 'Miercoles'
    elif (unNumero == 4):
        return 'Jueves'
    elif (unNumero == 5 ):
        return 'Viernes'
    elif (unNumero == 6):
        return 'Sabado'
    elif (unNumero == 7):
        return 'Domingo'
    else:
        return 'Error! Ingrese un numero entre 1 y 7'
"""
""" 
Ejercicio 6:
Pide al usuario su edad y clasificarla en categorías como niño (<12),
adolescente ( <18), adulto (<=60), o anciano (>60) y retornarla.

def getCategoriaEdad():
    edad = int(input('Ingrese su edad: '))
    if (edad < 0 or edad >= 150): 
        raise Exception('Error edad no puede ser negativa debe ser >0')
    elif ( edad >= 0 and edad <= 12 ):
        return 'Niño'
    elif (edad >12 and edad < 18):
        return 'Adolescente'
    elif (edad >=18 and edad < 60):
        return 'Adulto'
    elif (edad >= 60):
        return 'Ancino'

print(getCategoriaEdad())
"""

"""
Ejercicio 7:
Pide al usuario la hora del día (en formato 24 horas ej: 22)
y muestra si es mañana (6 a 12) , tarde (12 a 19),  
noche (19 a 0) o madrugada (0 a 6), debe retornar el mensaje
def getEstadoDia():
    hora = int(input('Ingrese un hora valida: '))
    if (hora < 0 or hora >= 24 ):
        raise Exception('Error, ingrese una hora entre 0 y 23.')
    elif ( hora >= 6 and hora <12):
        return 'Mañana'
    elif ( hora >=12 and hora < 19):
        return 'Tarde'
    elif ( hora >= 19 and hora <= 23):
        return 'Noche'
    elif (hora >= 0 and hora < 6):
        return 'Madrugada'

print(getEstadoDia())
"""
