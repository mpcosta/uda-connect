import logging
import grpc
import location_pb2
import location_pb2_grpc

from concurrent import futures
from utils import send_location_message

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("udaconnect-location-ingester-service")

class LocationIngesterService(location_pb2_grpc.LocationServiceServicer):
    def CreateLocation(self, request, context):

        request_data = {
            "person_id": int(request.person_id),
            "latitude": request.latitude,
            "longitude": request.longitude
        }
        logger.info("Received Incoming Payload: %s", request_data)
        # Publish to Kafka Queue
        send_location_message(request_data)
        return location_pb2.LocationMessage(**request_data)

# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationIngesterService(), server)

logger.info('Starting server. Listening on port 5005.')
server.add_insecure_port('[::]:5005')
server.start()
server.wait_for_termination()