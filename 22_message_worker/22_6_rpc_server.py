"""
REMOTE PROCUDURAL CALL (RPC)
need to run a function on a remote computer and wait for the result? Well, that's a different story. This pattern is commonly known as Remote Procedure Call or RPC.
"""
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672, virtual_host='/',
                                                               credentials=pika.PlainCredentials('guest', 'guest')))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def on_request(ch, method, props, body):
    n = int(body)

    print(f" [.] fib({n})")
    response = fib(n)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()

"""

    As usual we start by establishing the connection and declaring the queue rpc_queue.
    We declare our fibonacci function. It assumes only valid positive integer input. (Don't expect this one to work for big numbers, it's probably the slowest recursive implementation possible).
    We declare a callback on_request for basic_consume, the core of the RPC server. It's executed when the request is received. It does the work and sends the response back.
    We might want to run more than one server process. In order to spread the load equally over multiple servers we need to set the prefetch_count setting.

"""