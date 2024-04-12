import pika
import json
import pymysql

# Conecta ao servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declara a fila da loja online
channel.queue_declare(queue='pedidos')

# Conecta ao banco de dados
db = pymysql.connect("localhost", "usuario", "senha", "loja")
cursor = db.cursor()

# Função para processar e registrar os pedidos
def callback(ch, method, properties, body):
    pedido = json.loads(body)
    print("Pedido recebido:", pedido)
    # Processa o pedido e registra no banco de dados
    sql = "INSERT INTO pedidos (cliente, produto) VALUES (%s, %s)"
    cursor.execute(sql, (pedido['cliente'], pedido['produto']))
    db.commit()
    print("Pedido registrado no banco de dados")

# Registra o consumidor na fila
channel.basic_consume(queue='pedidos', on_message_callback=callback, auto_ack=True)

print("Aguardando pedidos...")

# Começa a consumir mensagens
channel.start_consuming()
