import socket


#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket()
port = 12345

s.bind(('', port))

s.listen()

c, addr = s.accept()

print("Got connection from",addr)

print (s.recv(1024).decode())

c.send("what is up".encode())



c.close()
