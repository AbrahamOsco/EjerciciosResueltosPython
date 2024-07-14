class Nota:
    cantNotasCreadas:int = 0 #Esto es un atributo de clase

    def __init__(self, unNombreMateria:str, unaNota:int):
        self.nombreMateria = unNombreMateria #Esto es un atributo de instancia. 
        self.nota = unaNota
        Nota.cantNotasCreadas +=1 #aumento en 1 al atributo de clase. 

def f(x,y ):
    return x +y 

def main():
    unObjetoNota = Nota("matematicas", 10)
    unObjetoNota2 = Nota("ciencia", 8)
    unObjetoNota3 = Nota("programacion", 7)
    print(f"value1:  {unObjetoNota.cantNotasCreadas}")
    print(f"value2:  {unObjetoNota3.cantNotasCreadas}")


main()