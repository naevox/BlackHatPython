import socket

target_host = "www.google.com"
target_port = 80

#makes a socket object AF_NET specifies IPV4 or hostname, SOCK_STREAM specifies TCP CLIENT
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to the server
client.connect((target_host,target_port))

#send data to server
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#receive responce
responce = client.recv(4096)

print responce