#!/usr/bin/env python
import pika

# connection with RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# create a hello queue to which the message will be delivered
channel.queue_declare(queue='hello')

# send msg
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")


connection.close()