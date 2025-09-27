import redis
import control_pb2


r = redis.Redis(host="localhost", port=6379, db=0)

msg = control_pb2.controlMsg()
msg.id = 1
msg.command = "LED_ON"
msg.value = 42.0

payload = msg.SerializeToString()

r.publish("teensy_channel", payload)

print("Sent:", msg)
