from conexion import coleccion_usuario

def crear_usuario():
    nombre = input("Ingrese el nombre: ")
    tipo_usuario = input("Seleccione el tipo de usuario (V o C): ")
    correo = input("Ingrese su correo: ")
    contraseña = input("Ingrese su contraseña: ")
    telefono = input("Ingrese su numero de telefono: ")
    imagen_perfil = input("Añade una imagen: ")

    if nombre == "" or tipo_usuario == "" or correo == "" or contraseña == "" or telefono == "" or imagen_perfil == "":
        print("Error: todos los campos deben ser obligatorios y validos")
        return

    if tipo_usuario == "V":
        print("Perfil vendedor")
        tipo_usuario = "Vendedor"
        descripcion = input("Ingrese una descripcion de su perfil: ")
        if descripcion == "":
            print("Error: la descripcion es obligatoria")

    elif tipo_usuario == "C":
        tipo_usuario = "Comprador"
        print("Perfil comprador")
        descripcion = ""
    else:
        print("Seleccione un tipo de usuario valido")

    usuario = {
        "nombre": nombre,
        "tipo_usuario": tipo_usuario,
        "correo": correo,
        "contraseña": contraseña,
        "telefono": telefono,
        "imagen_perfil": imagen_perfil,
        "descripcion": descripcion
    }

    coleccion_usuario.insert_one(usuario)
    print("Usuario insertado correctamente")

def iniciar_sesion():
    correo = input("Ingrese su correo: ")
    contraseña = input("Ingrese su contraseña: ")

    if correo == "" or contraseña == "":
        print("Error: todos los campos deben ser obligatorios")

    usuario = coleccion_usuario.find_one({"correo": correo, "contraseña": contraseña})

    if usuario:
        print("Inicio de sesión exitoso")
        print(f"Bienvenido, {usuario['nombre']}!")
    else:
        print("Correo o contraseña incorrectos. Intente nuevamente.")
        return iniciar_sesion()


def cerrar_sesion():
    opcion = input("Desea cerrar sesión? s/n: ")
    if opcion == "s":
        print("Cerrando sesión...")
        print("Sesión cerrada correctamente.")
    elif opcion == "n":
        print("Operación cancelada.")
    else:
        print("Opción no válida. Por favor, intente nuevamente.")

def consultar_usuarios():
    filtro = coleccion_usuario.find()
    total_usuarios = coleccion_usuario.count_documents({})
    print(f"Total de usuarios: {total_usuarios}")
    for usuario in filtro:
        print(usuario)

def consultar_usuario_nombre():
    nombre = input("Ingrese el nombre del usuario a consultar: ")
    usuarios = coleccion_usuario.find({"nombre": nombre})
    for usuario in usuarios:
        if usuario:
            print(f"Nombre: {usuario['nombre']}, Tipo de usuario: {usuario['tipo_usuario']}, Correo: {usuario['correo']}, Telefono: {usuario['telefono']}, Imagen de perfil: {usuario['imagen_perfil']}, Descripcion: {usuario['descripcion']}")
        else:
            print("Usuario no encontrado.")

def eliminar_usuario():
    nombre_usuario = coleccion_usuario.find_one({"nombre": nombre})
    tipo_usuario = coleccion_usuario.find_one({"tipo_usuario": "tipo_usuario"})

    if tipo_usuario == "administrador":

        nombre = input("Ingrese el nombre del usuario a eliminar: ")
        seguridad = input("¿Está seguro de que desea eliminar este usuario? (s/n): ")
        if seguridad == "s":
            coleccion_usuario.delete_one({"nombre": nombre})
            print("Usuario eliminado correctamente.")
        elif seguridad == "n":
            print("Operación cancelada.")
        else:
            print("Operación no válida.")


    elif tipo_usuario != "administrador" and nombre_usuario == nombre_usuario:
        coleccion_usuario.delete_one({"nombre": nombre})
        print("Cuenta eliminada correctamente.")
    elif nombre_usuario != nombre_usuario:
        print("No puede eliminar cuenta de otro usuario.")

# consultas por indice
def consultar_usuario_combinacion():
    nombre = input("Ingrese el nombre del usuario a consultar: ")
    correo = input("Ingrese el correo del usuario a consultar: ")
    usuarios = coleccion_usuario.find({"nombre": nombre, "correo": correo})
    for usuario in usuarios:
        if usuario:
            print(f"Nombre: {usuario['nombre']}, Tipo de usuario: {usuario['tipo_usuario']}, Correo: {usuario['correo']}, Telefono: {usuario['telefono']}, Imagen de perfil: {usuario['imagen_perfil']}, Descripcion: {usuario['descripcion']}")
        else:
            print("Usuario no encontrado.")

