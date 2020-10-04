"""
Входный файл для демонизации парсеров
Получение данных из мастер очереди создание задач
И отправка обратно в очередь
"""

import json
import daemon
from shop.zara import Zara
from shop.shop_enum import ShopEnum
import settings
import custom_queue.consume as queue


def task_handle():
    """Callback consumer"""
    def callback(msg: str):
        data = json.loads(msg)
        item_data = data['clothes']

        if item_data['shop'] == ShopEnum.ZARA.value:
            print('Zara process starting')
            zara_clothes = Zara(item_data['code'])
            detail_zara = zara_clothes.run()
            print(detail_zara)
            print('Zara process stoping')
    return callback


print('Start proccessing')
consumer = queue.Consume(settings.CLOUDAMQP_URL, 'parcerProcess')
channel = consumer.channel(task_handle())
print('Start start_consuming')

with daemon.DaemonContext():
    channel.start_consuming()
