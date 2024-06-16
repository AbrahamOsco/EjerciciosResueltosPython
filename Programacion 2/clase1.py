SIMBOLO_JUGADOR = {1:"🪓", 2: "🪵"}

def crearTablero():
    tablero = []
    for i in range(0, 3):
        unaFila = []
        for j in range(0, 3):
            unaFila.append(" ")
        tablero.append(unaFila)
    return tablero

def printTablero(unTablero):
    print("--------------------")
    for i in range(0, 3):
        for j in range(0, 3):
            if (unTablero[i][j] == SIMBOLO_JUGADOR[1]):
                print(f"|  {unTablero[i][j]} |", end="")
            else: 
                print(f"|  {unTablero[i][j]}  |", end="")
        print("")
    print("--------------------")

def validarInputUsuario(datosIngresados):
    unaFila, unaColumna, unSimbolo, unTablero = datosIngresados
    if (unaFila < 1 or unaFila > 3 or unaColumna < 1 or unaColumna > 3 ):
        print("[ERROR] Debe ingresar un numero entre 1 y 3")
        return "ERROR"
    if (unTablero[unaFila-1][unaColumna-1]) != " ":
        print(f"[ERROR] Debe no puede ingresar un {unSimbolo} en un casillero ocupado")
        return "ERROR"
    return "OK"

def ingresarJugada(tablero, jugadorAct):
    ingresoJugada = False
    while not ingresoJugada:
        try:
            unaFila = int(input("Ingresa una fila ( 1 a 3): "))
            unaColumna = int(input("Ingresa una columna ( 1 a 3): "))
        except(ValueError):
            print("[ERROR] Debe ingresar un numero y no una letra en fila o columna")
            continue
        if ( validarInputUsuario((unaFila, unaColumna, SIMBOLO_JUGADOR[jugadorAct], tablero)) == "OK" ):
            tablero[unaFila-1][unaColumna -1] = SIMBOLO_JUGADOR[jugadorAct]
            ingresoJugada = True

def obtenerJugadorActual(jugador):
    if jugador == 1: 
        jugador = 2
    elif jugador == 2 or jugador == 0:
        jugador = 1
    return jugador

def chequearGanador(tablero):
    if tablero[0][0] != " " and tablero[0][0] == tablero[0][1] and tablero[0][1] == tablero[0][2]:
        print(f"Ganador es {tablero[0][0]}")
        return "HAY_GANADOR"
    
    elif tablero[1][0] != " " and tablero[1][0] == tablero[1][1] and tablero[1][1] == tablero[1][2]:
        print(f"Ganador es {tablero[1][1]}")
        return "HAY_GANADOR"
    
    elif tablero[2][0] != " " and tablero[2][0] == tablero[2][1] and tablero[2][1] == tablero[2][2]:
        print(f"Ganador es {tablero[2][0]}")
        return "HAY_GANADOR"
    
    elif tablero[0][0] != " " and tablero[0][0] == tablero[1][0] and tablero[1][0] == tablero[2][0]:
        print(f"Ganador es {tablero[0][0]}")
        return "HAY_GANADOR"
    
    elif tablero[0][1] != " " and tablero[0][1] == tablero[1][1] and tablero[1][1] == tablero[2][1]:
        print(f"Ganador es {tablero[0][1]}")
        return "HAY_GANADOR"
    
    elif tablero[0][2] != " " and tablero[0][2] == tablero[1][2] and tablero[1][2] == tablero[2][2]:
        print(f"Ganador es {tablero[0][2]}")
        return "HAY_GANADOR"
    
    elif tablero[0][0] != " " and tablero[0][0] == tablero[1][1] and tablero[1][1] == tablero[2][2]:
        print(f"Ganador es {tablero[0][0]}")
        return "HAY_GANADOR"
    
    elif tablero[0][2] != " " and tablero[0][2] == tablero[1][1] and tablero[1][1] == tablero[2][0]:
        print(f"Ganador es {tablero[0][2]}")
        return "HAY_GANADOR"

    return "NO_HAY_GANADOOR"

def chequearEmpate(tablero):
    for i in range(0, 3):
        for j in range(0, 3):
            if (tablero[i][j] == " "):
                return "NO_EMPATE"
    return "EMPATE"

    
def jugarJuego():
    tablero = crearTablero()
    hayGanador = False
    hayEmpate = False
    jugador = 0
    printTablero(tablero)
    while(not hayGanador and not hayEmpate):
        jugador = obtenerJugadorActual(jugador)
        print(f"Ingrese jugada del jugador {jugador} que juega CON: {SIMBOLO_JUGADOR[jugador]} : ")
        ingresarJugada(tablero, jugador)
        printTablero(tablero)
        unResultado = chequearGanador(tablero)
        if (unResultado == "HAY_GANADOR"):
            hayGanador = True
        unEmpate = chequearEmpate(tablero)
        if (unEmpate == "EMPATE"):
            hayEmpate = True
    if(hayEmpate):
        print("Hubo empate nadie gano")
    elif (hayGanador): 
        print(f"Muchas gracias por jugar {SIMBOLO_JUGADOR[1]} {SIMBOLO_JUGADOR[2]}. El ganador es {jugador} (tres en rayas)")

def main():
    jugarJuego()

main()
