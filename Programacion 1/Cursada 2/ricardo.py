def Tuplar(tupla):
    diccionario={}

    for i in range(0,len(tupla)):       
        clave =tupla[i][0]
        valores= tupla[i][1:]
        diccionario[clave] = valores
        
    return diccionario
   
def main ():
    tupla =[("JEAN","FRANCO","JACK","MAX"),(24,22,2,2)]
    print(Tuplar(tupla))
main() 

""" 
🤯 😶‍🌫️  🪵 :piple 🔥 📬 :speed 🖌️ 🌟
"""