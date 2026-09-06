from productos import *


def main_productos():
    while True:
        print("Seleccione una opción:")
        print("1. Crear producto")
        print("2. Consultar productos disponibles")
        print("3. Consultar productos por categoría")
        print("4. Consultar productos por usuario")
        print("5. Consultar productos por precio")
        print("6. Consultar cantidad de productos por categoría")
        print("7. Consultar promedio de precio por categoría")
        print("8. Consultar productos ordenados por stock")
        print("9. Consultar productos por categoría y precio")
        print("10. Salir")

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
            cantidad_productos_por_categoria()
        elif opcion == "7":
            promedio_precio_por_categoria()

        elif opcion == "8":
            ordenar_productos_por_stock()
            
        elif opcion == "9":
            productos_categoria_precio()
        elif opcion == "10":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

main_productos()