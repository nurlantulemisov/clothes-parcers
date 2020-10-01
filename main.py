"""
Входный файл для демонизации парсеров
Получение данных из мастер очереди создание задач
И отправка обратно в очередь
"""

import os
import json
import pika
import daemon
import zara


def task_handle(msg: str):
    """Callback consumer"""
    data = json.loads(msg)
    item_data = data['clothes']
    if item_data['shop'] == zara.Zara.parcer_code:
        print('Zara process starting')
        zara_clothes = zara.Zara(item_data['code'])
        detail_zara = zara_clothes.run()
        print(detail_zara)
        print('Zara process stoping')


def callback(channel, method, properties, body: str):
    #pylint: disable=unused-argument
    """Callback consumer"""
    task_handle(body)


def consume():
    """daemon consumer"""
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
