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

def consultar_usuarios():
    filtro = coleccion_usuario.find()
    total_usuarios = coleccion_usuario.count_documents({})
    print(f"Total de usuarios: {total_usuarios}")
    for usuario in filtro:
        print(usuario)

def consultar_usuario_nombre():
    nombre = input("Ingrese el nombre del usuario a consultar: ")
    usuario = coleccion_usuario.find_one({"nombre": nombre})
    if usuario:
        print(usuario)
    else:
        print("Usuario no encontrado.")

def eliminar_usuario():
    nombre = input("Ingrese el nombre del usuario a eliminar: ")
    seguridad = input("¿Está seguro de que desea eliminar este usuario? (s/n): ")
    if seguridad == "s":
        coleccion_usuario.delete_one({"nombre": nombre})
        print("Usuario eliminado correctamente.")
    elif seguridad == "n":
        print("Operación cancelada.")
    else:
        print("Operación no válida.")

