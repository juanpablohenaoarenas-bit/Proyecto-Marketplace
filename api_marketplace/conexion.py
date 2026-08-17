from pymongo import MongoClient

try:
    cliente = MongoClient("mongodb://localhost:27017/")
    cliente.admin.command('ping')
    print("Conexion exitosa con MongoDB")
except Exception as e:
    print("Error al conectar con MongoDB:", e)
    print("Asegurate que MongoDB este instalado y en ejecucion en tu sistema.")

db = cliente["marketplace"]
coleccion_usuario = db["usuarios"]

coleccion_categoria = db["categorias"]

coleccion_producto = db["productos"]

coleccion_carrito = db["carrito"]

coleccion_pedido = db["pedidos"]

coleccion_pago = db["pagos"]

coleccion_envio = db["envios"]