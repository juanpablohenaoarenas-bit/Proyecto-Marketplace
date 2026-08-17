from usuarios import *

while True:
    print("Seleccione una opción:")
    print("1. Crear un nuevo usuario")
    print("2. Consultar usuarios")
    print("3. Consultar un usuario por nombre")
    print("4. Eliminar un usuario")
    print("5. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        crear_usuario()
    elif opcion == "2":
        consultar_usuarios()
    elif opcion == "3":
        consultar_usuario_nombre()
    elif opcion == "4":
        eliminar_usuario()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, intente nuevamente.")