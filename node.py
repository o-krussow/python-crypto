import socket
import json






#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket()
port = 12345

s.bind(('', port))

s.listen()

c, addr = s.accept()

print("Got connection from",addr)

c.send("what is up".encode())



c.close()
