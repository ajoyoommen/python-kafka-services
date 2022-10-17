import json
import logging
from time import sleep

import config
from kafka import KafkaConsumer, KafkaProducer

logger = logging.getLogger("orders_service")
logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
logger.addHandler(stream_handler)


sleep(20)

# KAFKA CONSUMER SETUP
consumer = KafkaConsumer(
    config.KAFKA_TOPIC_NEW_ORDERS,
    bootstrap_servers=[config.KAFKA_SERVER],
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)

producer = KafkaProducer(
    bootstrap_servers=[config.KAFKA_SERVER],
    value_serializer=lambda x: json.dumps(x).encode("utf-8"),
)

logger.info("Topics: %s", consumer.topics())

for message in consumer:
    message = message.value
    data = message.get("order")

    order_id = data["order_id"]

    for item, quantity in data["items"].items():
        if quantity < 1:
            continue
        producer.send(
            config.KAFKA_TOPIC_UNPROCESSED_ORDERS,
            value={"order_id": order_id, "item": item, "quantity": quantity},
        )
    logger.info("Received: %s", message)
