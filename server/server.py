import socket
import sys

host = 'localhost'
port = 8888
addr = (host, port)
server = socket.socket(socket.AF_INET)
server.bind(addr)
server.listen(10)

while True:
    sc, address = server.accept()
	
    filename = sc.recv(1024).decode("utf-8")
    f = open(filename,'wb') #open in binary  
    
    # receive data and write it to file
    l = sc.recv(1024)
    while (l):
        f.write(l)
        l = sc.recv(1024)

    f.close()
    sc.close()

s.close()