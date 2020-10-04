"""
Consume class
"""

import pika
from pika.adapters.blocking_connection import BlockingChannel


class Consume:
    """Consume class"""

    def __init__(self, url: str, name_queue: str):
        self.name_queue = name_queue
        self.connection = pika.BlockingConnection(pika.URLParameters(url))

    def channel(self, message_callback: callable) -> BlockingChannel:
        """create channel and sets callback"""
        channel = self.connection.channel()
        channel.queue_declare(queue=self.name_queue, durable=True)

        def callback(channel, method, properties, body):
            # pylint: disable=unused-argument
            message_callback(body)

        channel.basic_consume(self.name_queue,
                              on_message_callback=callback,
                              auto_ack=True)
        return channel

    def close(self) -> None:
        """close"""
        self.connection.close()
