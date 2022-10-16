import json
import logging
import random
from time import sleep

import config
from kafka import KafkaProducer

logger = logging.getLogger("orders_service")
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

while True:
    order = {}
    for item in items:
        order[item] = random.choice([0, 1, 2, 3])
    producer.send(config.KAFKA_TOPIC, value={"order": order})
    sleep(1)
