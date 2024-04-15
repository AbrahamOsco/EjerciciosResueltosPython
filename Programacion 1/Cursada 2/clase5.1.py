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

# Ejercicio 8
def getCategoriaUsuario():
    sueldo = float(input('Ingrese su sueldo: '))
    if (sueldo <= 0 ):
        raise Exception('El sueldo no puede ser negativo')
    elif (sueldo <= 100000.0):
        return 'Cat.Baja'
    elif ( sueldo > 100000.0 and sueldo <= 300000.0):
        return 'Cat.Media'
    elif (sueldo > 300000 ):
        return 'Cat.Alta'
    

print(getCategoriaUsuario())

#Ejercicio 9
def getMayor(num1, num2):
    mayor = num1
    if (num2 > num1):
        mayor = num2
    return mayor


def getMayor3NumIngresados():
    num1 = int(input('Ingrese un numero: '))
    num2 = int(input('Ingrese un numero: '))
    num3 = int(input('Ingrese un numero: '))
    mayorUno = getMayor(num1, num2)
    mayorTotal = getMayor(mayorUno, num3)
    return mayorTotal

print(getMayor3NumIngresados())

#Ejercicio 11:
def getCategoriaVehiculo():
    categoria = input('Ingrese su categoria: ').lower()
    categRetornada = ''
    if (categoria != 'coche' and categoria !='moto' and categoria != 'bicicleta'):
        raise Exception('Error: Ingrese un vehiculo que sea coche, moto o bicicleta ')
    elif (categoria == 'coche'):
        categRetornada = 'Categoria es Coche'
    elif (categoria == 'moto'):
        categRetornada = 'Categoria es Moto'
    elif (categoria == 'bicicleta'):
        categRetornada = 'Categoria es Bicicleta'
    
    return categRetornada


print(getCategoriaVehiculo())


#Ejercicio 12
def mostrarPromedio():
    num1 = float(input('Ingrese un numero: '))
    num2 = float(input('Ingrese un numero: '))
    num3 = float(input('Ingrese un numero: '))
    promedio = (num1 + num2 +num3)/3
    print(f'Promedio float: {promedio} , Promedio entero: { int(promedio) }' )

mostrarPromedio()

# ejercicio 13

def getSumaConRestric():
    acumulador = 0 
    num1 = int(input('Ingrese un numero entero: '))
    if (num1 == 0 ):
        return num1 
    acumulador += num1

    num2 = int(input('Ingrese un numero entero: '))
    if (num2 == 0):
        return acumulador
    acumulador += num2
    
    num3 = int(input('Ingrese un numero entero: '))
    if (num3 == 0):
        return acumulador    
    acumulador += num3

    return acumulador

print(getSumaConRestric())

#ejercicio 14
def getCantidadDigNum():
    num1 = input('Ingrese un numero: ')
    return len(num1)

print(getCantidadDigNum())

#Ejercicio 15: 
def mostrarEscalaSegunPuntj():
    num1 = int(input('Ingrese un numero: '))
    if ( num1 < 0 or num1 >100):
        print('Error: numero ingresado debe ser entre 0 y 100')
    elif ( num1 >= 90 and num1 <= 100):
        print('A')
    elif (num1 >= 80 and num1 <= 89):
        print('B')        
    elif (num1 >= 70 and num1 <= 79):
        print('C')        
    elif (num1 >= 60 and num1 <= 69):
        print('D')        
    elif (num1 < 60):
        print('F')        

mostrarEscalaSegunPuntj()

