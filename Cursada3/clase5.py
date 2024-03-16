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

def main():
    ejemplListas()

main()
