""" 
Escribe una funcion que solicite al usuario dos
números y luego muestre la suma y resta de esos dos números.
"""

def sumarNumeros():
    numero1 = int(input("Ingrese un numero: "))
    numero2 = int(input("Ingrese otro numero: "))
    suma = numero1 + numero2
    resta = numero1 - numero2
    print(f"La suma es: {suma}")    
    print(f"La resta es: {resta}")    

#sumarNumeros()


from turtle import *
import colorsys

speed(0)
bgcolor("black")
h=0

for i in range(60):
    for j in range(8):
        c=colorsys.hsv_to_rgb(h,0.9,1)
        color(c)
        h+=0.008
        rt(90)
        circle(150-j*6,90)
        lt(90)
        circle(150-j*6,90)
        lt(90)
        circle(150-j*6,90)
        rt(180)
    circle(40,24)

done()
