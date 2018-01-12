#!/usr/bin/env python

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='i am jhare\'s test')

print(" [x] Sent the message")

connection.close()
