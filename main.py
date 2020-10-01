import pika
import os
import time
import json
import zara
import daemon

def task_handle(msg: str):
    data = json.loads(msg)
    item_data = data['clothes']
    if item_data['shop'] == zara.Zara.parcer_code:
        print('Zara process starting')
        zara = zara.Zara(item_data['code'])
        detail_zara = zara.run()
        print(detail_zara)
        print('Zara process stoping')
    return

def callback(ch, method, properties, body: str):
    task_handle(body)

def consume():
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

with daemon.DaemonContext():
    consume()
