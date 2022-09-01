import os
from datetime import date
import datetime

os.system("cls")
print("""Seleccione una opcion: 
1.- Imprimir YYYY/MM/DD
2.- Imprimir  MM/DD/YYYY""")
tecla=input()
if tecla == 1:
    x = datetime.date(date.today().year, date.today().month, date.today().day)
else:
    x = datetime.date(date.today().month, date.today().day, date.today().year)
print(x)