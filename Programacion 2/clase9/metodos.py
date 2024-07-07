import random as r 
class Estudiante:
    cantidad = 0

    def __init__(self, nombre, apellido):
        Estudiante.cantidad += 1
        self.nombre = nombre
        self.apellido = apellido

    def presentarse(self):
        print(f"Hello my name is : {self.nombre} {self.apellido} 💯")

    @classmethod
    def getClima(cls):
        print("Es soleado 🌞")

    @classmethod #decorador para indicarle q es un metodo de clase. 
    def calcularDistancia(cls, distancia):
        print(f" {cls.cantidad} ")
        cls.getClima()
        numero = r.randint(1, 10)
        return distancia * numero
    


def main():
    estudiante1 = Estudiante("juan", "Perez")
    estudiante2 = Estudiante("Gonza", "Anthony")
    estudiante1.presentarse()
    distanciaCalculada = Estudiante.calcularDistancia(10)
    print(f"distanciaCalculada: {distanciaCalculada}")


    print("hello world")


main()