from usuarios import *


def main_usuarios():
    while True:
        print("Bienvenido a la sección de usuarios")
        print("Seleccione una opción:")
        print("1. Consultar un usuario por nombre")
        print("2. Eliminar mi cuenta")
        print("3. Volver al menú principal")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            consultar_usuario_nombre()
        elif opcion == "2":
            confirmacion = input("Esta seguro de eliminar su cuenta? s/n: ")
            if confirmacion == "s":
                eliminar_usuario()
            elif confirmacion == "n":
                print("No se eliminó la cuenta, aún puedes usarla.")
        elif opcion == "3":
            print("Volviendo al menú principal...")
            return
        else:
            print("Opción no válida. Por favor, intente nuevamente.")