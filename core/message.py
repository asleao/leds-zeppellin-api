"""
    Class responsable for passing information to the Cloud AMQ.
"""
import pika
from django.conf import settings


class Message:
    def __init__(self, queue, exchange, routing_key, body):
        self.queue = queue
        self.exchange = exchange
        self.routing_key = routing_key
        self.body = body

    def send_message(self):
        """
            Function responsible to send data to a queue on Cloud AMQ.
        """
        connection = pika.BlockingConnection(
            settings.PARAMS_AMQ)  # Connect to CloudAMQP
        channel = connection.channel()  # start a channel
        channel.queue_declare(queue=self.queue)  # Declare a queue

        channel.basic_publish(exchange=self.exchange,
                              routing_key=self.routing_key, body=self.body) # Send message
        # print("[x] Message sent to consumer")
        connection.close()
