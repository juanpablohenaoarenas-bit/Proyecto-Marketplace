from usuarios import *
from main_usuarios import main_usuarios

def menu_principal():
    while True:
        print("Bienvenido a esta pagina Marketplace")
        print("Seleccione una opción:")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. cerrar programa")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            iniciar_sesion()
            main_usuarios()
            opcion = input("Desea mantener la sesión iniciada? s/n: ")
            if opcion == "s":
                print("ok")
                return main_usuarios()
            elif opcion == "n":
                cerrar_sesion()
                break
        elif opcion == "2":
            crear_usuario()
        elif opcion == "3":
            print("Gracias por usar nuestro programa.")
            break

if __name__ == "__main__":
    menu_principal()

