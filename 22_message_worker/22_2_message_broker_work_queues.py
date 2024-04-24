"""
send and receive messages from a named queue. In this one we'll create a Work Queue that will be used to distribute
time-consuming tasks among multiple workers.
The main idea behind Work Queues (aka: Task Queues) is to avoid doing a resource-intensive task immediately and
having to wait for it to complete. Instead we schedule the task to be done later.
We encapsulate a task as a message and send it to the queue.
A worker process running in the background will pop the tasks and
eventually execute the job. When you run many workers the tasks will be shared between them.
This concept is especially useful in web applications where it's impossible to handle a complex task during a short
HTTP request window.

buka 2 terminal
run
python 22_message_worker/22_2_message_broker_work_queue.py

run python 22_2_new_task.py
"""
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672, virtual_host='/', credentials=pika.PlainCredentials('guest', 'guest')))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)  # optional create queue to control
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
# Sends the AMQP command Basic.Consume to the broker and binds messages
#         for the consumer_tag to the consumer callback
channel.basic_consume(queue='task_queue', on_message_callback=callback)
channel.start_consuming()
