import os
import logging
import json

from kafka import KafkaProducer

TOPIC_NAME = os.environ['KAFKA_TOPIC_NAME']
KAFKA_SERVER = os.environ['KAFKA_SERVER']

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("udaconnect-location-ingester-service")

producer = KafkaProducer(bootstrap_servers=[KAFKA_SERVER])

def send_location_message(location_message):
    logger.info("Received Location Data for publishing to Kafka: %s", location_message)
    kafka_data = json.dumps(location_message).encode('utf-8')
    producer.send(TOPIC_NAME, kafka_data)
    producer.flush()
    logger.info("Location Data successfully published to Kafka: %s", location_message)
