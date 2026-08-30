from conexion import coleccion_categoria

def crear_categoria():
    nombre = input("Ingrese el nombre de la categoria: ")
    descripcion = input("Ingrese la descripcion de la categoria: ")

    if nombre == "" or descripcion == "":
        print("Error: todos los campos deben ser obligatorios y validos")
        return

    categoria = {
        "nombre": nombre,
        "descripcion": descripcion
    }

    coleccion_categoria.insert_one(categoria)
    print("Categoria insertada correctamente")

def consultar_categorias():
    filtro = coleccion_categoria.find()
    total_categorias = coleccion_categoria.count_documents({})
    print(f"Total de categorias: {total_categorias}")
    for categoria in filtro:
        print(categoria)

def consultar_categoria_nombre():
    nombre = input("Ingrese el nombre de la categoria a consultar: ")
    categoria = coleccion_categoria.find_one({"nombre": nombre})
    if categoria:
        print(categoria)
    else:
        print("Categoria no encontrada.")