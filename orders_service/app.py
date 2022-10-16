import json
import logging

import config
from kafka import KafkaConsumer

logger = logging.getLogger("orders_service")
logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
logger.addHandler(stream_handler)

# KAFKA CONSUMER SETUP
consumer = KafkaConsumer(
    config.KAFKA_TOPIC,
    bootstrap_servers=[config.KAFKA_SERVER],
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)

logger.info("Topics: %s", consumer.topics())

counter = 0
for message in consumer:
    message = message.value
    data = message.get("order")
    logger.info("Received: %s", data)
    counter += 1
    if counter % 5000 == 0:
        logger.info("Indexed %s logs", counter)
