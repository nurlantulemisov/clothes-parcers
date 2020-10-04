"""
Входный файл для демонизации парсеров
Получение данных из мастер очереди создание задач
И отправка обратно в очередь
"""

import json
import daemon
from shop.shop_factory import ShopFactory
import settings
import custom_queue.consume as queue


def decode_message(msg: str) -> list:
    """ Parce message and get playload"""
    data = json.loads(msg)
    return data['clothes']


def task_handle():
    """Callback consumer"""
    def callback(msg: str):
        item_data = decode_message(msg)
        print('Zara process starting')
        factory = ShopFactory()
        shop = factory.shop(int(item_data['shop']), item_data['code'])
        detail_zara = shop.run()
        print(detail_zara)
        print('Zara process stoping')
    return callback


print('Start proccessing')
consumer = queue.Consume(settings.CLOUDAMQP_URL, 'parcerProcess')
channel = consumer.channel(task_handle())
print('Start start_consuming')

with daemon.DaemonContext():
    channel.start_consuming()
