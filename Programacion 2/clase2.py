
#  (Pre) Precondiciones: Recibe el numerador y el denominador como argumentos en ese orden,
#                        el denominador no debe ser cero. 
# (Post) Postcondiciones: Retorna la division, en caso de que el denominador sea cero retornamos 0. 
def divisionSegura(numerador, denominador):
    if denominador == 0:
        raise Exception("Error el denominador no puede ser cero ")
    return numerador/denominador

def elevarCuadrado(unNumero):
    return unNumero**2


def catcheandoExcepciones():
    try:
        print(f"{divisionSegura(3, 0)}") # SE EJECUTO 
        print(f"{divisionSegura(3, 1)}")  # Nunca se ejecuto
        print(f"{divisionSegura(3, 2)}")  # Nunca se ejecuto
        print(f"{divisionSegura(3, 3)}")  # Nunca se ejecuto
    except Exception:
        print(f"LANZO Excepcion Estoy capturandolo :")

def sumarResultadosAlCubo(num1, num2):
    return (num1**3 + num2**3)

def calcular(unaFuncion):
    def restarNumeros(unNumero):
        return unNumero - 40
    unResultado = unaFuncion(3, 4)
    return restarNumeros, unResultado

# Pre: Recibe un diccionario cuya clave es el mail y el valor es la contraseña. 
# Post: Printea cada mail asociado a su clave. 
def printCuentas(cuentasUsuarios: dict):
    for mail, contraseña in cuentasUsuarios.items():
        print(f"El mail es : {mail} y la contraseña es: {contraseña}" )

def depositar(saldoCuenta, saldoDepositar):
    if saldoDepositar < 0:
        raise Exception("Error saldo negativo ")
    saldoCuenta += saldoDepositar
    return saldoCuenta    

""" 
Dado una lista de número y una función getCuadrado, crear una función que
recibe ambos elementos  y retorna una lista con los cuadrados de los números
"""
def getCuadrado(unNumero):
    return unNumero**2

def calcularCuadradosConFOS(unaLista, getCuadrado):
    cuadrados = []
    for elemento in unaLista:
        cuadrados.append(getCuadrado(elemento))
    return cuadrados 

def filterName7(unString):
    return (len(unString) < 7)

def filtrarNombres(nombres, filterName7):
    nombresFiltrados = []
    for unNombre in nombres:
        if filterName7(unNombre):
            nombresFiltrados.append(unNombre)
    return nombresFiltrados

def probando():
    unaFuncion, unNumero = calcular(sumarResultadosAlCubo)
    print(f" unaFuncion(unNumero):  {unaFuncion(unNumero)}")
    users = {"darko@gmail.com" : "1234567", "athony@gmail.com" : "queso1234", "mercy@gmail.com" : "codeando123"   } 
    printCuentas(users)
    #print(f"depositar(100, -40) {depositar(100, -40)}") 
    listaLoca = [3, 4.5, 8, 9, 10, 2.5, 7]
    print(calcularCuadradosConFOS(listaLoca, getCuadrado))

def combinarFunciones(funcion1, funcion2, unNumero):
    resultadoParcial = funcion1(unNumero)
    return funcion2(resultadoParcial)

def getCubo(unNumero):
    return unNumero**3    

def main():
    listaLocaNombres= ["Anthony", "Gonzalo", "Matias", "Fiorella", "Sol", "Ricardo" ]
    print(f" nombres filtadros {filtrarNombres(listaLocaNombres, filterName7)}")
    print(combinarFunciones(getCuadrado, getCubo, 5))
    
    
main()