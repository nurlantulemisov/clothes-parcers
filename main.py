import pika
import os
import time


def task_handle(msg):
    print("RabbitMq processing")
    print(" [x] Received " + str(msg))

    time.sleep(5)
    print(" RabbitMq processing finished")
    return

def callback(ch, method, properties, body):
    task_handle(body)

url = os.environ.get('CLOUDAMQP_URL', 'amqp://app:qwerty@0.0.0.0:5672/%2f')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()  # start a channel
channel.queue_declare(queue='parcerProcess', durable=True)

channel.basic_consume('parcerProcess',
                      callback,
                      auto_ack=True)

channel.start_consuming()
connection.close()
