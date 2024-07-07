class Perro():
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print("Metodo que sera pisado por las hijas! invocamos a las hijas")

    def dormir(self):
        print(f"{self.nombre} está durmiendo.")

class PastorAleman(Perro):
    def ladrar(self):
        print(f"{self.nombre} (Pastor Alemán) dice: ¡Guau, guau!")

    def acrobacia(self):
        print("salto de 2m ⛵")

class Pitbull(Perro):
    def ladrar(self):
        print(f"{self.nombre} (Pitbull) dice: ¡Woof, woof!")

    def mordedura(self):
        print("te mordi 🐕")

def main():
    unPerro = PastorAleman("Max")
    otroPerro = Pitbull("Rocky")
    unPerro.acrobacia()
    unPerro.ladrar()
    unPerro.dormir()
    otroPerro.ladrar()

main()