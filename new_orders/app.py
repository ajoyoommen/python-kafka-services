import json
import logging
import random
from time import sleep

import config
from kafka import KafkaProducer

logger = logging.getLogger("orders_processing")
logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
logger.addHandler(stream_handler)


sleep(20)

producer = KafkaProducer(
    bootstrap_servers=[config.KAFKA_SERVER],
    value_serializer=lambda x: json.dumps(x).encode("utf-8"),
)

items = ["bread", "cake", "tea", "coffee"]

order_id = 1

while True:
    order = {"order_id": order_id, "items": {}}
    for item in items:
        order["items"][item] = random.choice([0, 1, 2, 3])
    logger.info("Order created: %s", order)
    producer.send(config.KAFKA_TOPIC_NEW_ORDERS, value={"order": order})
    sleep(1)
    order_id += 1
