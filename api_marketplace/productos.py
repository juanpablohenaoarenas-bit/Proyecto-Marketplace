from conexion import coleccion_producto



def crear_producto():
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripcion del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese la cantidad de stock disponible: "))
    imagen_producto = input("Añade una imagen del producto: ")
    categoria = input("Ingrese la categoria del producto: ")
    usuario = input("Ingrese el usuario que crea el producto: ")

    if nombre == "" or descripcion == "" or precio == "" or stock == "" or imagen_producto == "":
        print("Error: todos los campos deben ser obligatorios y validos")
        return

    producto = {
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio,
        "stock": stock,
        "imagen_producto": imagen_producto,
        "categoria":categoria,
        "usuario": usuario
    }

    coleccion_producto.insert_one(producto)
    print("Producto insertado correctamente")

def productos_disponibles():
    stock = coleccion_producto.find({"stock": {"$gt": 0}})
    for producto in stock:
        print(f"ID: {producto['_id']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Stock: {producto['stock']}")

def productos_categoria():
    categoria = input("Ingrese la categoria del producto: ")
    productos = coleccion_producto.find({"categoria": categoria})
    for producto in productos:
        print(f"ID: {producto['_id']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Stock: {producto['stock']}")

def productos_usuario():
    usuario = input("Ingrese el usuario del producto: ")
    productos = coleccion_producto.find({"usuario": usuario})
    for producto in productos:
        print(f"ID: {producto['_id']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Stock: {producto['stock']}")

def productos_precio():
    precio = float(input("Ingrese el precio del producto: "))
    productos = coleccion_producto.find({"precio": precio})
    for producto in productos:
        print(f"ID: {producto['_id']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Stock: {producto['stock']}")