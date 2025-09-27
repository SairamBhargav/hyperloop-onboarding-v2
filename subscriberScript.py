import redis
import control_pb2

r = redis.Redis(host="localhost", port=6379, db=0)
pubsub = r.pubsub()
pubsub.subscribe("teensy_channel")

print("Listening for messages...")

for message in pubsub.listen():
    if message["type"] == "message":
        data = message["data"]
        msg = control_pb2.controlMsg()
        msg.ParseFromString(data)
        print(f"Got: id={msg.id}, command={msg.command}, value={msg.value}")
