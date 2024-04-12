import pika
import json
import requests

# Conecta ao servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declara a fila de pedidos processados
channel.queue_declare(queue='pedidos_processados')

# Função para enviar os pedidos processados para o sistema de envio
def callback(ch, method, properties, body):
    pedido = json.loads(body)
    print("Pedido processado recebido:", pedido)
    # Simula o envio do pedido processado para o sistema de envio/logística
    requests.post('http://localhost:8000/enviar_pedido', json=pedido)
    print("Pedido processado enviado para o sistema de envio")

# Registra o consumidor na fila de pedidos processados
channel.basic_consume(queue='pedidos_processados', on_message_callback=callback, auto_ack=True)

print("Aguardando pedidos processados...")

# Começa a consumir mensagens
channel.start_consuming()
