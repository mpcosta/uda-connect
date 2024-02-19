class LocationRepository:
    def __init__(self, engine):
        self.engine = engine

    def save_location_message(self, message):
        with self.engine.connect() as connection:
            connection.execute(
                f"""
                INSERT INTO location (person_id, latitude, longitude)
                VALUES ({message['person_id']}, {message['latitude']}, {message['longitude']})
                """
            )