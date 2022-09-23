import os;os.system("cls")

class Usuario:
    def __init__(self,usuario,contrasena,rol,nombre,curp,ciudad) -> None:
         self.Usuario=usuario
         self.Contrasena=contrasena
         self.Rol=rol
         self.Nombre=nombre
         self.CURP=curp
         self.Ciudad=ciudad
    def __str__(self) -> str:
        return(f"""
        Usuario:{self.Usuario} 
        Contraseña:{self.Contrasena}
        Rol:{self.Rol}
        Nombre:{self.Nombre}
        CURP:{self.CURP}
        Ciudad:{self.Ciudad}\n""")

#Usuario Admin
admin=Usuario("mikeangelo1212","1212","Administrador","Miguel Campos","CAXM01212MENPEGA0","Nuevo Laredo")
usuarios=[admin]

while True:
    try:
        opcion= int(input("""Seleccione una opcion:
    1.- Registro
    2.- Inicio de sesión
    3.- Salida\n"""))
    except Exception:
        os.system("cls")
        print("Opcion no valida\n")
        continue
    if opcion==1:
        miUsuario=Usuario(
        input("\nIngrese nombre de usuario:"),
        input("\nIngrese contraseña: "),
        input("\nIngrese su rol: "),
        input("\nIngrese su nombre: "),
        input("\nIngrese su CURP: "),
        input("\nIngrese su ciudad: "))
        for i in usuarios:
            if miUsuario.CURP==i.CURP:
                os.system("cls")
                print("El usuario ya existe")
                break
        else:
            os.system("cls")
            usuarios.append(miUsuario)
            print("==Usuario capturado==\n")
            continue
                
    elif opcion==2:
        x=input("Ingrese su usuario: ")
        y=input("Ingrese su contraseña: ")
        os.system("cls")
        for i in usuarios:
            if i.Usuario==x and i.Contrasena==y and i.Rol=="Administrador":
                print("\nBienvenido administrador")
                for i in usuarios:
                    print(i.__str__())
                    break
            elif i.Usuario==x and i.Contrasena==y:
                print(f"\nHola {i.Rol}\n")
                print(i.__str__())
                break
        else: os.system("cls");print("====Usuario no encontrado====\n")
    else:
        print("Adios")
        break
