from conexion import coleccion_pedido

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
