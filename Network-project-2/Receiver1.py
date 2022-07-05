
import socket
import socket
import sys
import os
import math

# specify localhost
IP_UDP = "127.0.0.1"
#speecify port
PORT_UDP = int(sys.argv[1])
#specify filename to be created
filename = sys.argv[2]
#start a socket
s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Use this socket for specified port number
s.bind((IP_UDP, PORT_UDP))
#create a bytearray
image = bytearray()

while True:
    # set buffer size to 1027 and receive data
    data, addr = s.recvfrom(1027)
    #add to image bytearray
    image.extend(data[2:])
    #if it is last packet break
    if(data[2] == 1):
        break

#write image
with open(filename, 'wb') as f:
    f.write(image)

#close socket
s.close()
