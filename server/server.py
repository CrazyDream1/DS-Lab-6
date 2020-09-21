import socket
import sys
import os

# Create socket
host = ''
port = 8888
addr = (host, port)
server = socket.socket(socket.AF_INET)
server.bind(addr)
server.listen(10)

# For each connection
while True:
    sc, address = server.accept() # Connect to client
    filename = sc.recv(1024).decode("utf-8") # Get name of file
    
    ls = os.listdir('.') # get list of files in the directory
    if filename in ls: # if file is already exists set name as "namecopy_1.extension"
        dot_split = filename.split('.')
        name = dot_split[0]
        extension = ".".join(dot_split[1:])
        i = 1
        while(filename in ls):
            filename = name + "copy_" + str(i) + "." + extension # change filename
            i += 1    
	
    f = open(filename,'wb') #open in binary
    # receive data and write it to file
    l = sc.recv(1024)
    while (l):
        f.write(l)
        l = sc.recv(1024)

    f.close()
    sc.close()

server.close()