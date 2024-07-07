import random as r 

class Arma:
    def __init__(self, danioBase):
        self.danioBase = danioBase
        self.critico = 1
    
    def getDanio(self):
        pass

class Cuchillo(Arma):

      def getDanio(self):
        self.critico = r.randint(1, 4)
        return ("🔪", self.critico * self.danioBase)

class Axe(Arma):

      def getDanio(self):
        self.critico = r.randint(2, 5)
        return ("🪓", self.critico * self.danioBase)

class Guerrero:

    def __init__(self, nombre, ciudadOrigen, arma):
        self.nombre = nombre
        self.ciudadOrigen = ciudadOrigen
        self.arma = arma

    def saludar(self):
        print(f"hola soy {self.nombre}")

    def atacar(self):
        simbolo, danio = self.arma.getDanio()
        print(f"Haciendo {danio} danio con {simbolo}")


def main():
    knife = Cuchillo(10)
    hachaLoca = Axe(30)
    guerrero = Guerrero("gonzalo anthony", "nuevo mundo ", hachaLoca)
    guerrero.atacar()

main()

