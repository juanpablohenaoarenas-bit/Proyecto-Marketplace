from categorias import *

def main_categorias():
    while True:
        print("Seleccione una opción:")
        print("1. Crear categoria")
        print("2. Consultar categorias")
        print("3. Consultar categoria por nombre")
        print("4. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            crear_categoria()
        elif opcion == "2":
            consultar_categorias()
        elif opcion == "3":
            consultar_categoria_nombre()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
main_categorias()