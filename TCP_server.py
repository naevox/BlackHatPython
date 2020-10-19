import socket
import threading

#0.0.0.0 specifies all non local IP addresses
bind_ip = "0.0.0.0"
bind_port = 9999

#AF_INET specfies IPv4 and hostname, SOCK_STREAM specifies TCP connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to ip and port
server.bind((bind_ip,bind_port))

#listen with maximum backlog of 5
server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip,bind_port)

#this thread handles the client handling
def handle_client(client_socket):

    #print out what the client sends
    requests = client_socket.recv(1024)

    print "[*] Received: %s" % requests

    #reply with packet
    client_socket.send("ACK!")

    client_socket.close()

while True:
    client,addr = server.accept()

    print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])

    #handle incoming data
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start() 