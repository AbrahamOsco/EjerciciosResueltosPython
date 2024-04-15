""" Crear un tablero(matriz) de 4 filas y 3 columnas y llenalas con el  numero '1'
    Luego imprimirlas en forma de tablero e imprimir el tablero """
def getTablero():
    filas = 4
    columnas = 3
    tablero = []
    for i in range(0, filas):
        filaTablero = []    # Creamos una lista que modelara cada fila del tablero"
        for j in range(0, columnas):
            filaTablero.append('1') # A cada fila del tablero le agregamos un '1' string.
        tablero.append(filaTablero)
    return tablero,filas,columnas   # retornamos 3 cosas de golpe tablero filas y columnas (una Tupla)

def printearTablero(unTablero, filas, columnas):
    for i in range(0, filas):
        print("--"*filas + 'T') # Hago el techo de cada fila
        for j in range(0, columnas):
            print(f'|{unTablero[i][j]}', end='|')
        print('')
    print("--"*filas + "Piso") #hago el piso final

def main():
    tablero, filas, columnas = getTablero()     # desempaquetamos
    print(tablero)
    printearTablero(tablero, filas, columnas)

main()
