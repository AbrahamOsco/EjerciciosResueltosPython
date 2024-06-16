

class Nota:
    cantNotasCreadas:int = 0 #Esto es un atributo de clase

    def __init__(self, unNombreMateria:str, unaNota:int):
        self.nombreMateria = unNombreMateria #Esto es un atributo de instancia. 
        self.nota = unaNota
        self.cantNotasCreadas +=1


def main():
    unObjetoNota = Nota("matematicas", 10)
    unObjetoNota2 = Nota("ciencia", 8)
    unObjetoNota3 = Nota("programacion", 7)
    print(f" {unObjetoNota.nombreMateria}  {unObjetoNota.nota} ")
    print(f" {unObjetoNota3.cantNotasCreadas}")



main()