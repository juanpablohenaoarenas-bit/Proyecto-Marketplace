from pedidos import *

def main_pedidos():
    while True:
        print("Seleccione una opción:")
        print("1. Crear pedido")
        print("2. Consultar pedidos")
        print("3. Consultar pedidos por comprador")
        print("4. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            crear_pedido()
        elif opcion == "2":
            consultar_pedidos()
        elif opcion == "3":
            pedidos_comprador()
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

main_pedidos()