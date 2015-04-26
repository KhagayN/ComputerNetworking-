# We will need the following module to generate randomized lost packets

import random
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('',12000)) # '' means all available interfaces

while True:
    # Generate random numbers in the range of 0 to 10
    rand = random.randint(0,10)
    # Receive client packet along with address it is coming from
    message, address = serverSocket.recvfrom(1024)
    # capitalize the message
    message = message.upper()
    print (message)
    # If rand is less than 4, we consider the packet lost and do not respond
    if rand < 4:
        continue
    # Otherwise, the server responds
    serverSocket.sendto(message, address)
    


