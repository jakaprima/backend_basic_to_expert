"""
add feature:
membuat posible to subscribe only to a subset dari messages.
contoh: kita bisa direct hanya critical error messages ke log file (to save disk space),
ketika sedang print semua log messages di console.
"""

#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672, virtual_host='/',
                                                               credentials=pika.PlainCredentials('guest', 'guest')))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(
    exchange='direct_logs', routing_key=severity, body=message)
print(f" [x] Sent {severity}:{message}")
connection.close()
