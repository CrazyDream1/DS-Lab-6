import socket
import sys
from pathlib import Path

filename = sys.argv[1]
host = sys.argv[2]
port = int(sys.argv[3])

filesize = Path(filename).stat().st_size
currentfilesize = 0
s = socket.socket(socket.AF_INET)
s.connect((host,port))
s.send(bytes(filename, 'utf-8'))
f = open (filename, "rb")
l = f.read(1024)
while (l):
    currentfilesize = currentfilesize + 1024
    if (currentfilesize % (1024 * 100) == 0):
        print(str(currentfilesize / filesize * 100) + "%")
    s.send(l)
    l = f.read(1024)
s.close()

# python client.py car.png localhost 8888