import json
import logging
import os

from kafka import KafkaConsumer
from sqlalchemy import create_engine
from message_repository import LocationRepository

# Get initial configuration fields from environment variables
DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]
KAFKA_TOPIC_NAME = os.environ["KAFKA_TOPIC_NAME"]
KAFKA_SERVER = os.environ["KAFKA_SERVER"]

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("udaconnect-location-service")

# Set up Kafka Consumer
consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=[KAFKA_SERVER])

# Set up MessageRepository
engine = create_engine(f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
location_repository = LocationRepository(engine)

for message in consumer:
    logger.info("Received Incoming Message: %s", message)
    decoded_message = json.loads(message.value.decode("utf-8"))
    location_repository.save_location_message(decoded_message)