import random as r 
ATAQUE_SALTO = 1 
ATAQUE_BOLA_DE_FUEGO = 2
ATAQUE_GOLPE_DE_MARTILLO = 3
#self.dicAtaques= {ATAQUE_SALTO: AtaqueSalto(), }
#import Ataque
# refactor: pasar cada clase a un .py distinto. 
class Ataque():
    def __init__(self):
        self.danio = 0
        self.simbolo = "X"
    
    def getAtaque(self):
        mensaje = f" ha atacado con {self.simbolo} e hizo {self.danio} de danio"
        return (self.danio, self.simbolo, mensaje)


class Salto(Ataque):

    def __init__(self):
        self.danio = 10
        self.simbolo = "🦘"
    
class BolaDeFuego(Ataque):

    def __init__(self):
        self.danio = 15
        self.simbolo = "🔥"
    
class Martillo(Ataque):

    def __init__(self):
        self.danio = 20
        self.simbolo = "🔨"


class Personaje():
    
    def __init__(self):
        self.simbolo = "X"
        self.hp = 0
    
    def recibirDanio(self, simboloAtaque, danio):
        print(f"{self.simbolo} ha recibido el ataque {simboloAtaque} que le hizo {danio} de danio")
        self.hp -= danio
    
    def sigueVivo(self):
        return self.hp > 0
    
    def getEstado(self):
        return f"{self.simbolo} Tiene {self.hp}"


class Mario(Personaje):
    def __init__(self):
        self.simbolo = "🍄"
        self.hp = 150
        # patron de command. 
        self.dicAtaques = {ATAQUE_SALTO: Salto(), ATAQUE_BOLA_DE_FUEGO: BolaDeFuego(), ATAQUE_GOLPE_DE_MARTILLO: Martillo()}
        self.ataqueActual = Salto()

    def atacar(self, numeroDeAtaque):
        self.ataqueActual = self.dicAtaques.get(numeroDeAtaque)
        return self.ataqueActual.getAtaque()

# Ataques de bowser y bowser
    
class LanzaLlamas(Ataque):

    def __init__(self):
        self.danio = 20
        self.simbolo = "🔥"
    
class Pisoton(Ataque):

    def __init__(self):
        self.danio = 25
        self.simbolo = "🦶"
    
class GarraSombria(Ataque):

    def __init__(self):
        self.danio = 30
        self.simbolo = "🔱"

class Bowser(Personaje):
    def __init__(self):
        self.simbolo = "🐲"
        self.hp = 80
        self.ataquesDisponibles = [Pisoton(), LanzaLlamas()]
        self.ataqueActual = Pisoton()
        self.contadorAtaques = 0

    def atacar(self, numeroDeAtaque: int):
        if (self.contadorAtaques >= 3):
            self.ataqueActual = GarraSombria()
        else: 
            self.ataqueActual = r.choice(self.ataquesDisponibles)
        self.contadorAtaques +=1
        return self.ataqueActual.getAtaque()


class Juego:
    def __init__(self):
        self.inputUsuario = ""
        self.juegoTerminado = False

    def seguirJugando(self, mario: Mario, boswer: Bowser):
        if (not mario.sigueVivo()):
            print("El ganador de la batalla es Boswer 🐲!!")
            return False
        elif(not boswer.sigueVivo()):
            print("El ganador de la batalla es Mario 🍄!!")
            return False
        return True


    def iniciarJuego(self):
        mario = Mario()
        boswer = Bowser()
        while self.seguirJugando(mario, boswer):
            print(f"{mario.getEstado()} {boswer.getEstado()}", end="")
            numeroDeAtaque = int(input("\n1: Salto 🦘\n2: Bola de fuego 🔥 \n3: Golpe con martillo 🔨\n Ingrese el nro: "))
            danio, simbolo, mensaje = mario.atacar(numeroDeAtaque)
            print(f"Mario {mensaje} | ", end="")
            boswer.recibirDanio(simbolo, danio)
            danio, simbolo, mensaje = boswer.atacar(numeroDeAtaque)
            print(f"Boswer {mensaje} | ", end="")
            mario.recibirDanio(simbolo, danio)
        print(f"{mario.getEstado()} {boswer.getEstado()}")

def main():
    marioRPG = Juego()
    marioRPG.iniciarJuego()


main()