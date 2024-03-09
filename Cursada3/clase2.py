#nombre =  input("Hola ingresa tu nombre: ")
nombre = "antony"
edad = 10
#print("El nombre ingreasdo es ", nombre, "su edad es: ", 10)
#print(f"El nombre ingresado es {nombre} y su edad {edad} con fStrings")
edadAntony = 30
edadEdgar = 50
comparacion = (edadAntony != edadEdgar) or not (edadAntony >= edadEdgar)

if (edadAntony < 20 ): 
    print("Tu edad es menor que 100")
elif (edadAntony < 80):
    print("Tue edad es menor que 80 ")
elif (edadAntony < 60):
    print("Tue edad es menor que 60")
else:
    print("Tenes mas que 60 ")

if (0):
    print("Hola mundo")
x = "" # cadena vacia
y = " " # cadena con un espacio. 
if (0 or ""):
    print("Entre aca ???")
elif ( (-230.404 or 12.32) and "hola antony" ):
    print("Siempre entrare aca")

def productosLocos(x, y, z):
    aux1 = x * y 
    aux2 = x * z
    return aux1 + aux2

print(productosLocos(3, -4, 5))

def mostrarSumYRestDeNumeros():
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese un numero: "))
    print(f" La resta es :  {num1 - num2}, y la suma es {num1 + num2} ")

# invocar la funcion para poder ejecutarla
mostrarSumYRestDeNumeros()

# ☕  :coffee: 