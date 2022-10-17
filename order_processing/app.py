import json
import logging
from datetime import datetime
from time import sleep

import config
from kafka import KafkaConsumer

logger = logging.getLogger("order_processing")
logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
logger.addHandler(stream_handler)


sleep(20)

# KAFKA CONSUMER SETUP
consumer = KafkaConsumer(
    config.KAFKA_TOPIC_UNPROCESSED_ORDERS,
    bootstrap_servers=[config.KAFKA_SERVER],
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)

logger.info("Topics: %s", consumer.topics())

counter = 0
for message in consumer:
    data = message.value
    logger.info("Dispatched: %s", datetime.now(), message)
