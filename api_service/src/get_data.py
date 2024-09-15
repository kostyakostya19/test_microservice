import pika
import os
from dotenv import load_dotenv

load_dotenv()

def get_data_from_rabbitmq():
    RABBITMQ_HOST = os.getenv('RABBITMQ_HOST')
    RABBITMQ_QUEUE = os.getenv('RABBITMQ_QUEUE')
    RABBITMQ_USER = os.getenv('RABBITMQ_USER')
    RABBITMQ_PASS = os.getenv('RABBITMQ_PASS')

    credentials = pika.PlainCredentials(
        RABBITMQ_USER,
        RABBITMQ_PASS
        )

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=RABBITMQ_HOST,
            credentials=credentials
            )
        )

    channel = connection.channel()

    method_frame, header_frame, body = channel.basic_get(
        queue=RABBITMQ_QUEUE
        )

    if method_frame:
        print(f"Received message: {body}")
        channel.basic_ack(method_frame.delivery_tag)
        return body
    else:
        print("No message received")
        return None
