import random as r 

class Personaje:

    def __init__(self, nombre, ciudadOrigen):
        self.nombre = nombre
        self.ciudadOrigen = ciudadOrigen

    def saludar(self):
        print(f"hola soy {self.nombre}")


class Guerrero(Personaje):

    def fundirArma(self): # metodo propio de la clase hija Guerrero. 
        print(f" hello my name is {self.nombre} and soy de {self.ciudadOrigen} y a make a")
        armas = ["🪓 ", "🍠" , "🏎️"] 
        return r.choice(armas)

    def saludar(self): # aca estamos redefiniendo el metodo. 
        print("Soy un guerrero ⚔️ 🪂")


def main():
    guerrero = Guerrero("anthony gonzalo", "rep dominicana")
    guerrero.saludar()
    print(f" {guerrero.fundirArma()}")


main()

