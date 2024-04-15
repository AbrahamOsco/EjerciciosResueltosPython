def ejemploDiccionario():
    unDic = {"Lunes": [100, 101]}
    unDic["Martes"] = "Anthony"  # agregando un elemento 
    unDic["Miercoles"] = (3, 30)
    unValor = unDic.get("Miercoles", "FIORELLA")
    for dia,valor in unDic.items():
        print(f" la clave es {dia} y el valor es {valor}")
    unasKeys = unDic.keys() # escupe encapsulado una lista con todas las claves
    
    for unaClave in unDic.keys():
        print(unaClave)
    
    for unValue in unDic.values():
        print(unValue)




def tuplas_a_diccionario(listaTuplas):
    unDic = {}
    for unaClave, unValor in listaTuplas:
        if (unaClave in unDic):
            unDic[unaClave].append(unValor)
        else: 
            unDic[unaClave] = [ unValor]
    return unDic     

def main():
    #ejemploDiccionario()
    listTuplas = [ ("hola", "don pepito"), ("hola", "don Jose"), ("Buenos", "dias")] 
    resultado = tuplas_a_diccionario(listTuplas)
    print(resultado)
main()
