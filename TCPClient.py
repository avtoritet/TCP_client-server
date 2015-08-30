# TCPClient.py - Simple TCP Client
import socket

target_host = "192.168.5.134"
target_port = 8888

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
client.send("Whats up!")#("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n\r\n")

# receive some data
response = client.recv(4096)

print response