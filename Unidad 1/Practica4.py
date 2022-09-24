import os;os.system("cls")
"""
#4 Entrada de datos y estructuración.
Revisar su retícula para escribir un programa que cree un diccionario vacío para que 
el usuario capture las materias y créditos de su semestre preferido (inferior a 8vo)
al final imprimir en el formato “{asignatura}” tiene “{créditos}”
créditos. Y la suma de todos los créditos del semestre
"""

dicc={}
creditosTotales=0
while True:
    try:#try por si se mete algo que no debe
        materia=input("Ingrese la materia:\n")
        creditos=int(input("Ingrese los creditos de la materia:\n"))
    except Exception:
        os.system("cls")
        print("Dato no aceptado\n")
        continue
    dicc.update({materia:creditos})
    if int(input("Ingresar otra materia? 1=si\n "))==1:
        os.system("cls")
        continue
    else: break
os.system("cls")
for i in dicc:
    print(f"La asignatura {i} tiene {dicc[i]} creditos")
    creditosTotales+=dicc[i]
print(f"Creditos totales: {creditosTotales}")

