
def saludarJhoson():
    def saludarGonzalo():
        print("hola gonza")
    print("hola jhonson")
      
def saludarAbraham(unaFuncion):
    unaFuncion()

def funcionStr(unString):
    return "@@@" + unString + "@@@"

def ejemplosConLambda():
    funcionLoca = lambda x, y ,z : ((x + y) * z**2 ) - x
    x = funcionLoca(3, 4, 5)
    funcion2 = lambda unStr, otroStr: funcionStr(unStr) + funcionStr(otroStr)   
    saludo = funcion2("hola", "mundo")
    print(x)
    print(saludo)

def criterioParaOrdenar(unStr):
    print(len(unStr))
    return len(unStr)

def probarSorted():
    nombres = ["Mathias", "Ana", "Gonzalo a", "Abraham Osco ", "Jhonson lalalala"]
    nombresOrdenados = sorted(nombres, key=criterioParaOrdenar)
    print(nombresOrdenados)
# Hacer una funcion que retone el cubo de un numero y le reste su cuadrado. 
# usando map y una funcion anomima (lambda). y que retorne la lista mapeada.
# funcion_cubo_loco = lambda x : (x ** 3) - (x ** 2)
def calcularCuboLoco(unaLista):
    return list(map(lambda x : (x ** 3) - (x ** 2), unaLista))
    
def filtrarLoco(nombres):
    return  list(filter(lambda unNombre: len(unNombre) < 10, nombres))

# Usando map, filter, y funciones anonimas: 
# Crear una funcion que genera una lista aleatoria de 12 numeros enteros (entre 0 , 25)
# aplicar map  para cuadriplicar el valor, y luego filtrar los numeros menores a 58.
import random as r

def ejemploMapFilterLambda():
    numerosRandom = []
    for i in range(0, 12):
        numerosRandom.append( r.randint(0, 25))
    numerosMapeados = list(map(lambda x: x *4, numerosRandom))
    numerosFiltrados = tuple(filter(lambda x: x < 50, numerosMapeados))
    print(f"numerosRandom : {numerosRandom}")    
    print(f"numerosMapeados : {numerosMapeados}")    
    print(f"numerosFiltrados : {numerosFiltrados}")    

def probarArchivos():
    archivo = open('matheo.txt', 'a')
    print(archivo)
    archivo.close()
    
def main():
    #ejemplosConLambda()
    numeros = [3, 4, 1, 1, 9, 10]
    #probarSorted()
    #print(calcularCuboLoco(numeros))
    nombres = ["Mathias", "Ana", "Gonzalo a", "Abraham Osco ", "Jhonson lalalala"]
    #print(filtrarLoco(nombres))
    ejemploMapFilterLambda()
    probarArchivos()
    
    
main()
