import socket, os

client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
client.connect("/tmp/python_unix_sockets_example", )

client.send("kakağu".encode("utf-8"))

client.close()