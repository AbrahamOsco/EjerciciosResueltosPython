""" 
Escribir una función que reciba una tupla de elementos e indique si se encuentran
ordenados de mayor a menor
"""
def ordenarTuplaASC(unaTupla):
    tuplaOrdenada = sorted(unaTupla, reverse=True) # con reverse ordenamos del mas grandote al mas chiquito.
    for i in range(0, len(unaTupla)):
        if unaTupla[i] != tuplaOrdenada[i]:
            print("No esta ordenada la tupla ")
            return False
    print("Esta  ordenada la tupla de ")
    return True  

""" 
Escribir una función que reciba una lista de tuplas, y que devuelve un diccionario en donde
las claves sean los primeros elementos de las tuplas, y los valores 
una lista con los segundos.
"""
def getDicFromTuplas(listaTuplas):
    dicRetonar = {}
    for unaTupla in listaTuplas:
        for elemento in unaTupla:
            unaLista = list(unaTupla)
            ultimoValor = unaLista[len(unaLista)-1]
            unaLista.remove( unaTupla[len(unaTupla)- 1] )
            dicRetonar[ultimoValor] = unaLista 
            break
    return dicRetonar

def main():
    #tupla1 = ("ricardo", "felipe", "ana")
    #ordenarTuplaASC(tupla1)
    listaTuplas = [(1, 2, 3, 4, 5) , ("Ana", "Ric", "Felipe", "Tantrum") ]
    print(getDicFromTuplas(listaTuplas))


main()
