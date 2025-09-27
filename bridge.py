import redis
import socket

UDP_IP = "192.168.1.50"   
UDP_PORT = 5005

r = redis.Redis(host="localhost", port=6379, db=0)
pubsub = r.pubsub()
pubsub.subscribe("teensy_channel")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Bridge running...")

for item in pubsub.listen():
    if item['type'] == 'message':
        payload = item['data']
        sock.sendto(payload, (UDP_IP, UDP_PORT))
        print("Forwarded", len(payload), "bytes")
