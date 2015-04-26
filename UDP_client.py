"""
Khagay Nagdimov
Computer Networking: UDP ping client
Professor Rafail Portnoy 4/25/2015
"""

# UDP client

#useful for later
from socket import *
import time

####################################################### body of code
#create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
#encode the host in bytes
host = '127.0.0.1'
encodedHost = bytes(host,'utf-8')

# address and port number of UDP PING server
port = 12000
address = ((encodedHost,12000))

# the client's socket will assume a packet is lost if no response within 1 second
clientSocket.settimeout(1)

# counts number of pings sent by client to server ( 10 needed)
pingCounter = 0
# initialize sequence number which has a synonymous value to that of pingCounter
sequenceNumber = 0

# please note that the difference in time between when the timer
# starts and when the difference is calculated is a little off because the timer does not start
# immediately when the message is sent. This gap in time is minuscule and if
# this code is used for something that is time sensitive to that extent,
# further changes need to be made.

while(pingCounter < 10):
    # increment the counter. Counter can be synonymous to sequence number
    pingCounter += 1
    # increment the sequence number
    sequenceNumber +=1
    # start the timer ( counter is in milliseconds)
    startTime = time.clock()
    # create the message
    message = []
    message.append(str(pingCounter))
    message.append(" ")
    message.append(str(sequenceNumber))
    message.append(" ")
    message.append(str(startTime))
    message.append(" ")
    # separate items of the value by a space
    message = ''.join(message)
    # encode and message to UDP ping server
    encodedMessage= bytes(message,'utf-8')
    clientSocket.sendto(encodedMessage, address)
    try:
        # accept data from UDP ping server
        dataFromServer, sendingAddress = clientSocket.recvfrom(1024)
        # decode the message
        dataFromServer = dataFromServer.decode('utf-8')
        # calculate difference and multiply because time was recorded in milliseconds
        timeElapsed = ((time.clock()-startTime) *1000)
        #print message from UDP
        print ("Message from UDP ping server is:", dataFromServer,"and the first number refers to the ping number, the second "
                                                                   "to the sequence number and the third to the time when the message was "
                                                                   "sent")
        # print RTT (round trip time)
        print ("Round Trip Time for packet#", pingCounter,"=" , timeElapsed, "seconds")

    except error:
        print ("Request timed out for packet #", pingCounter)