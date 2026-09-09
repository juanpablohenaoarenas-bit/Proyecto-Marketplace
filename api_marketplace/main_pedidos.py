from pedidos import *

def main_pedidos():
    while True:
        print("Seleccione una opción:")
        print("1. Crear pedido")
        print("2. Consultar pedidos")
        print("3. Consultar pedidos por comprador")
        print("4. Consultar pedidos con comprador y su información")
        print("5. Consultar usuarios con pedidos")
        print("6. Consultar pedidos con detalle")
        print("7. Consultar pedidos con información completa")
        print("8. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            crear_pedido()
        elif opcion == "2":
            consultar_pedidos()
        elif opcion == "3":
            pedidos_comprador()
        elif opcion == "4":
            pedidos_con_comprador()
        elif opcion == "5":
            usuarios_con_pedidos()
        elif opcion == "6":
            pedidos_con_detalle()
        elif opcion == "7":
            pedidos_con_informacion_completa()
        elif opcion == "8":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

main_pedidos()