import pika

# CONNECT TO RABBITMQ SERVER
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672, virtual_host='/', credentials=pika.PlainCredentials('guest', 'guest')))
channel = connection.channel()

# DECLARE A QUEUE
channel.queue_declare(queue="hello")

# ------------------------------------------------------------------------------ PRODUCER (PUBLISHING MESSAGES)
# PUBLISH A MESSAGE TO THE QUEUE
channel.basic_publish(exchange='', routing_key='hello', body='hello, rabbitmq!')

print("[x] sent 'hello, rabbitmq'")

# close the connection
# connection.close()


# ------------------------------------------------------------------------------ CONSUMER (CONSUMING MESSAGES)
# define callback function for consuming messages
def callback(ch, method, properties, body):
    print("[x] RECEIVED %r" % body)


# consume messages from the queue
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print('[*] waiting for messages. to exit press ctrl+c')

# start consuming
channel.start_consuming()
connection.close()
