import os
from tokenize import String

i=0
suma=0.0
os.system("cls")
print("cuantos numeros quiere introducir?")
x = int(input())
while True:
    print("Introduzca un numero:")
    suma +=int(input())
    i=i+1
    if i == x:
        break 
print("La suma es de: "+str(suma))