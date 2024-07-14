import random as r

class Guerrero:

    def __init__(self, nombre, arma):
        self.nombre = nombre
        self.hp = 100
        self.arma = arma

    def getNombre(self):
        return self.nombre    

    def atacar(self, otroGuerrero : Guerrero):
        simbolo,danio = self.arma.getAtaque()
        otroGuerrero.recibirDanio(danio)
        print(f" {otroGuerrero.getNombre()} recibio {danio} de danio !! con {simbolo} hecho por {self.nombre} ")
    
    def recibirDanio(self, danio):
        self.hp -= danio

class Arma: 
    def __init__(self, danioBase):
        self.critico = 1
        self.danioBase = danioBase
    
    def getAtaque(self):
        pass 


class Espada(Arma):
        
    def getAtaque(self):
        self.critico = r.uniform(1, 1.5)
        danioFinal = round(self.danioBase * self.critico, 2)
        return ("🗡️", danioFinal)
    
class Cuchillo(Arma):
    def getAtaque(self):
        self.critico = r.uniform(0.9, 1.7)
        danioFinal = round(self.danioBase * self.critico, 2)
        return ("🔪", danioFinal)
    
class Arco(Arma):
    def getAtaque(self):
        self.critico = r.uniform(1.3, 1.9)
        danioFinal = round(self.danioBase * self.critico, 2)
        return ("🏹", danioFinal)


cuchillo = Cuchillo(20)
unaEspada = Espada(15)
arco = Arco(20)
gonzalo = Guerrero("gonza", arco)
juanPerez = Guerrero("juan perez", unaEspada)
gonzalo.atacar(juanPerez)
