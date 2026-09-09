from conexion import coleccion_pedido, coleccion_usuario

def crear_pedido():
    detalle = input("Ingrese el detalle del pedido: ")
    pago = float(input("Ingrese el monto del pago: "))
    comprador = input("Ingrese el nombre del comprador: ")

    pedido = {
        "detalle": detalle,
        "pago": pago,
        "comprador": comprador
    }

    coleccion_pedido.insert_one(pedido)
    print("Pedido creado exitosamente.")

def consultar_pedidos():
    pedidos = coleccion_pedido.find()
    for pedido in pedidos:
        print(f"ID: {pedido['_id']}, Detalle: {pedido['detalle']}, Pago: {pedido['pago']}, Comprador: {pedido['comprador']}")

def pedidos_comprador():
    comprador = input("Ingrese el nombre del comprador: ")
    pedidos = coleccion_pedido.find({"comprador": comprador})
    for pedido in pedidos:
        print(f"ID: {pedido['_id']}, Detalle: {pedido['detalle']}, Pago: {pedido['pago']}, Comprador: {pedido['comprador']}")

# consultas por indice

def pedidos_existencia():
    comprador = input("Ingrese el nombre del comprador: ")
    pedidos = coleccion_pedido.find({"comprador": {"$exists": True}})
    for pedido in pedidos:
        if pedido['comprador'] == comprador:
            print(f"ID: {pedido['_id']}, Detalle: {pedido['detalle']}, Pago: {pedido['pago']}, Comprador: {pedido['comprador']}")
        else:
            print("No se encontraron pedidos para el comprador especificado.")
        
def pedidos_texto():
    detalle = input("Ingrese el detalle del pedido: ")
    pedidos = coleccion_pedido.find({"detalle": {"$regex": detalle}})
    for pedido in pedidos:
        print(f"ID: {pedido['_id']}, Detalle: {pedido['detalle']}, Pago: {pedido['pago']}, Comprador: {pedido['comprador']}")   

# pipeline con $lookup
def pedidos_con_comprador():
    pipeline = [
        {
            "$lookup": {
                "from": "usuarios",
                "localField": "comprador",
                "foreignField": "nombre",
                "as": "informacion_comprador"
            }
        }
    ]
    pedidos = coleccion_pedido.aggregate(pipeline)
    for pedido in pedidos:
        print(f"ID: {pedido['_id']}, Detalle: {pedido['detalle']}, Pago: {pedido['pago']}, Comprador: {pedido['comprador']}")
        if pedido['informacion_comprador']:
            comprador_info = pedido['informacion_comprador'][0]
            print(f"Información del comprador - Nombre: {comprador_info['nombre']}, Correo: {comprador_info['correo']}, Tipo de usuario: {comprador_info['tipo_usuario']}")
        else:
            print("No se encontró información del comprador.")


# pipeline con $unwind
def usuarios_con_pedidos():
    pipeline = [
        {
            "$lookup": {
                "from": "pedidos",
                "localField": "nombre",
                "foreignField": "comprador",
                "as": "pedidos_usuario"
            }
        },
        {
            "$unwind": "$pedidos_usuario"
        }
    ]
    usuarios = coleccion_usuario.aggregate(pipeline)
    for usuario in usuarios:
        print(f"Nombre: {usuario['nombre']}, Correo: {usuario['correo']}, Tipo de usuario: {usuario['tipo_usuario']}")
        print(f"Pedido - Detalle: {usuario['pedidos_usuario']['detalle']}, Pago: {usuario['pedidos_usuario']['pago']}")

# pipeline con $project

def pedidos_con_detalle():
    pipeline = [
        {
            "$project": {
                "_id": 0,
                "detalle": 1,
                "pago": 1,
                "comprador": 1
            }
        }
    ]
    pedidos = coleccion_pedido.aggregate(pipeline)
    for pedido in pedidos:
        print(f"Detalle: {pedido['detalle']}, Pago: {pedido['pago']}, Comprador: {pedido['comprador']}")

# pipeline con $lookup, $unwind y $project
def pedidos_con_informacion_completa():
    pipeline = [
        {
            "$lookup": {
                "from": "usuarios",
                "localField": "comprador",
                "foreignField": "nombre",
                "as": "informacion_comprador"
            }
        },
        {
            "$unwind": "$informacion_comprador"
        },
        {
            "$project": {
                "_id": 0,
                "detalle": 1,
                "pago": 1,
                "comprador": 1,
                "correo_comprador": "$informacion_comprador.correo",
                "tipo_usuario_comprador": "$informacion_comprador.tipo_usuario"
            }
        }
    ]
    pedidos = coleccion_pedido.aggregate(pipeline)
    for pedido in pedidos:
        print(f"Detalle: {pedido['detalle']}, Pago: {pedido['pago']}, Comprador: {pedido['comprador']}, Correo del comprador: {pedido['correo_comprador']}, Tipo de usuario del comprador: {pedido['tipo_usuario_comprador']}")