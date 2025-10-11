import redis
import socket

TCP_IP = "127.0.0.1"
TCP_PORT = 6379

r = redis.Redis(host="localhost", port=6379, db=0)
pubsub = r.pubsub()
pubsub.subscribe("teensy_channel")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))

print("TCP bridge running...")

for item in pubsub.listen():
    if item['type'] == 'message':
        payload = item['data']
        sock.sendall(payload)  # TCP send
        print("Sent", len(payload), "bytes over TCP")
