#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Create exchange: On one side it receives messages from producers and the other side it pushes them to queues
channel.exchange_declare(exchange='logs',
                         type='fanout')# fanout: broadcasts all the messages it receives to all the queues it knows

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()