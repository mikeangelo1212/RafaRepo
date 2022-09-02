import os
from datetime import date

os.system("cls")
print("""Seleccione una opcion: 
1.- Imprimir YYYY/MM/DD
2.- Imprimir  MM/DD/YYYY""")
tecla=int(input())
x = date(date.today().year, date.today().month, date.today().day)
if tecla == 1:
    print(x.strftime("%Y-%m-%d"))    
elif tecla == 2:#elif es else if
    print(x.strftime("%m-%d-%Y"))
else:
    print("No existe esa opcion, byeeeeeeeeeeee")
