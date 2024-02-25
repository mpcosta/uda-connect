import grpc
import location_pb2
import location_pb2_grpc
import random

"""
Sample implementation of a writer that sends a payload to the gRPC server in order to demonstrate 
the communication between a mobile device and the gRPC server.
"""

channel = grpc.insecure_channel('localhost:5005')
stub = location_pb2_grpc.LocationServiceStub(channel)

print("Sending sample location payload to gRPC server")

# Generate random person_id, latitude, and longitude
person_id = random.randint(5, 6)
latitude = str(random.uniform(-90, 90))
longitude = str(random.uniform(-180, 180))

# Create the payload with the random data
location_payload = location_pb2.LocationMessage(
    person_id=person_id,
    latitude=latitude,
    longitude=longitude
)

# Print the generated payload
print(f"Generated payload to be sent: Person ID: {person_id}, Latitude: {latitude}, Longitude: {longitude}")

# Send the payload to the gRPC server
response = stub.CreateLocation(location_payload)