#!/usr/bin/env python
import pika
import uuid


class FibonacciRpcClient(object):

    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

        self.response = None
        self.corr_id = None

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(n))
        while self.response is None:
            self.connection.process_data_events(time_limit=None)
        return int(self.response)


fibonacci_rpc = FibonacciRpcClient()

print(" [x] Requesting fib(30)")
response = fibonacci_rpc.call(30)
print(f" [.] Got {response}")

"""

    We establish a connection, channel and declare an exclusive callback_queue for replies.
    We subscribe to the callback_queue, so that we can receive RPC responses.
    The on_response callback that gets executed on every response is doing a very simple job, for every response message it checks if the correlation_id is the one we're looking for. If so, it saves the response in self.response and breaks the consuming loop.
    Next, we define our main call method - it does the actual RPC request.
    In call method, we generate a unique correlation_id number and save it - the on_response callback function will use this value to catch the appropriate response.
    Also in call method, we publish the request message, with two properties: reply_to and correlation_id.
    At the end we wait until the proper response arrives and return the response back to the user.

"""