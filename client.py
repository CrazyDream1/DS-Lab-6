import socket
import sys
from pathlib import Path

# Get parameters from console
filename = sys.argv[1]
host = sys.argv[2]
port = int(sys.argv[3])

# Get size of file in bytes
filesize = Path(filename).stat().st_size
currentfilesize = 0

# Create socket
s = socket.socket(socket.AF_INET)
# Connect to server
s.connect((host,port))

# Send name of file
s.send(bytes(filename, 'utf-8'))
# Send file data
f = open (filename, "rb")
l = f.read(1024)

while (l):
    currentfilesize = currentfilesize + 1024
    # Each 100Kb write progress
    if (currentfilesize % (1024 * 100) == 0):
        print(str(currentfilesize / filesize * 100) + "%")
    s.send(l)
    l = f.read(1024)
    
s.close()

# python client.py car.png "18.188.141.97" 8888