class Materia:
    instancias = 0
    MAX_ALUMNOS = 100

    def __init__(self, nombre, nota):
        Materia.instancias += 1
        self.nota = nota
        self.nombre = nombre
    
    def cantidadInstancias(self):
        print(f"cantidad de instancias es : {Materia.instancias}")
        Materia.otroMetodoDeClase()
    
    def printSinAtributos(self):
        print("printSinAtributos")

    def printMateria(self):
        print(f"materia: {self.nombre} nota: {self.nota} 💯")

    @classmethod
    def otroMetodoDeClase(cls):
        cls.printSinAtributos(cls)
        print("hello soy otro metodo de clase")

    @classmethod
    def cuposDisponibles(cls, alumnosActuales):
        print(f"Cupos disponibles son:  {cls.MAX_ALUMNOS - alumnosActuales}")
        cls.otroMetodoDeClase()
        cls.printMateria(cls)



def main():
    print("hello")
    nota1 = Materia("mate", 10)
    nota2 = Materia("chemistry", 7)
    nota2.cantidadInstancias()
    Materia.cuposDisponibles(10)

main()

