import pika
import json
from dotenv import load_dotenv
import os

load_dotenv()

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST')
RABBITMQ_QUEUE = os.getenv('RABBITMQ_QUEUE')
RABBITMQ_USER = os.getenv('RABBITMQ_USER')
RABBITMQ_PASS = os.getenv('RABBITMQ_PASS')

def send_data_to_rabbitmq(data):

    credentials = pika.PlainCredentials(
        RABBITMQ_USER,
        RABBITMQ_PASS
    )

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            RABBITMQ_HOST,
            credentials=credentials
            )
        )

    channel = connection.channel()
    channel.queue_declare(queue=RABBITMQ_QUEUE)

    data_json = json.dumps(data)

    data_bytes = data_json.encode('utf-8')

    channel.basic_publish(
        exchange='',
        routing_key=RABBITMQ_QUEUE,
        body=data_bytes)
    connection.close()