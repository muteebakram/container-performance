import argparse
import logging
import os

from pykafka import KafkaClient

logging.basicConfig(level=logging.INFO)

client = KafkaClient(hosts=os.getenv("KAFKA_HOST"))


def publish_message(message, topic):
    topic = client.topics[topic]
    with topic.get_sync_producer() as producer:
        producer.produce(message.encode())
        logging.info(f"Message published to {message} to {topic}.")


if __name__ == "__main__":

    parser = argparse.ArgumentParser("Send a message to a Kafka Topic")
    parser.add_argument("message", help="Kafka message")
    parser.add_argument("topic", help="Kafka topic")
    args = parser.parse_args()

    _message = str(args.message)
    _topic = str(args.topic)

    if _message is None or _topic is None:
        raise Exception("Please make sure to provide message and a topic")

    publish_message(_message, _topic)
