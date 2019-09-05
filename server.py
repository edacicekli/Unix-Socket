import socket
import struct
import os # OS tarafından sağlanan bir çok hizmeti Python içerisinde kolay bir şekilde kullanmamızı sağlayacak nesneleri barındırır.

if os.path.exists("/tmp/python_unix_sockets_example"): # path.exists ile bir dosya ve klasörün var olup olmadığını kontrol edersiniz.
       os.remove("/tmp/python_unix_sockets_example") 
s = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM) 


s.bind("/tmp/python_unix_sockets_example")


while True:
    message = s.recv(1024)
    print(message.decode("utf-8"))
    break
