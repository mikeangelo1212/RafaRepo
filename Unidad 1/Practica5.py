def ForVal(kwargs):
    for key, value in kwargs.items():
        print(key, value)
Flag = True
Completa = {}

while Flag:
    Llave = input("Ingrese dato X: \n")
    Valor = input("Ingrese dato Y: \n")
    
    Completa[Llave] = Valor
    Res = input("¿Otro Dato?: ")
    if Res == "Si" or Res == "SI" or Res == "si" or Res == "y" or Res == "Y" or Res =="Yes" or Res == "yes":
        continue
    else:
        Flag = False
        ForVal(Completa)