#!/usr/bin/env python

import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)


def callback(ch, method, properties, body):
    print(" [x] Received message %r" % body)
    print("Working...")
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='task_queue')

print(' [*] Waiting for messages on durable queue')

channel.start_consuming()
