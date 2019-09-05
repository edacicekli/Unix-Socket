import socket
import struct
import os

if os.path.exists("/tmp/python_unix_sockets_example"):
       os.remove("/tmp/python_unix_sockets_example")
s = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)


s.bind("/tmp/python_unix_sockets_example")


while True:
    message = s.recv(1024)
    print(message.decode("utf-8"))
    break
