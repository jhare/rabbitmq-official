#!/usr/bin/env python

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

result = channel.queue_declare(exclusive=True)  # let rmq pick name
queue_name = result.method.queue

channel.queue_bind(exchange='logs',
                   queue=queue_name)

print(' [*] Waiting for logs.')


def logCallback(ch, method, properties, body):
    print(" [x] got log %r" % body)


channel.basic_consume(logCallback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
