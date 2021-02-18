import socket
import ssl

a = socket.getaddrinfo('192.168.43.87', 8012)[0][-1]
print(a)
s = socket.socket()
s.setblocking(False)
s = ssl.wrap_socket(s)
s.connect(a)