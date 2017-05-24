#!/usr/bin/env python
import pika
import time

# Whenever we receive a message, this callback function is called by the Pika library
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)# if worker die, msg will be delivered again


# connection with RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# create a hello queue to which the message will be delivered
# we can run the command as many times as we like, and only one will be created
channel.queue_declare(queue='task_queue')

# receive message
channel.basic_consume(callback,
                      queue='task_queue',
                      no_ack=True)


# finally, we enter a never-ending loop that waits for data and runs callbacks whenever necessary.                    
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
