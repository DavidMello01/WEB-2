import pika
import json

# Conecta ao servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declara a fila da loja online
channel.queue_declare(queue='pedidos')

# Simula um pedido
pedido = {'id': 1, 'cliente': 'João', 'produto': 'Notebook'}

# Envia o pedido para a fila
channel.basic_publish(exchange='', routing_key='pedidos', body=json.dumps(pedido))
print("Pedido enviado:", pedido)

# Fecha a conexão
connection.close()
