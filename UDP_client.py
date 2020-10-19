import socket

th = "127.0.0.1"
tp = 80

#create the socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send data
client.sendto("BOB",(th,tp))

#receive responce
data, addr = client.recvfrom(4096)

print data 