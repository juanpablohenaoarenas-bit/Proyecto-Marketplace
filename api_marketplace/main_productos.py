from productos import *


def main_productos():
    while True:
        print("Seleccione una opción:")
        print("1. Crear producto")
        print("2. Consultar productos disponibles")
        print("3. Consultar productos por categoría")
        print("4. Consultar productos por usuario")
        print("5. Consultar productos por precio")
        print("6. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            crear_producto()
        elif opcion == "2":
            productos_disponibles()
        elif opcion == "3":
            productos_categoria()
        elif opcion == "4":
            productos_usuario()
        elif opcion == "5":
            productos_precio()
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

main_productos()