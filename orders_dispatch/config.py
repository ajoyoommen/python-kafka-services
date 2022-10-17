# Kafka
import os

KAFKA_SERVER = os.environ["KAFKA_SERVER"]  # "localhost:9092"
KAFKA_TOPIC_UNPROCESSED_ORDERS = os.environ.get("KAFKA_TOPIC_UNPROCESSED_ORDERS")
