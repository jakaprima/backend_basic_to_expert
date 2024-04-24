#!/usr/bin/env python
import pika
import sys

# open connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672, virtual_host='/',
                                                               credentials=pika.PlainCredentials('guest', 'guest')))
channel = connection.channel()  # create channel

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.DeliveryMode.Persistent
    ))
print(f" [x] Sent {message}")
connection.close()
