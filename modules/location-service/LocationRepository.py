import logging
from sqlalchemy.exc import ProgrammingError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("udaconnect-location-service")

class LocationRepository:
    def __init__(self, engine):
        self.engine = engine

    def save_location_message(self, message):
        try:
            with self.engine.connect() as connection:
                query = f"""
                INSERT INTO location (person_id, coordinate)
                VALUES ({message['person_id']}, ST_Point({message['longitude']}, {message['latitude']}))
                """
                connection.execute(query)
        except ProgrammingError as e:
            logger.error("An error occurred while saving the location message: %s", e)