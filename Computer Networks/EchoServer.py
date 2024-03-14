import socket
import sys
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=('localhost',9999)
server.bind(server_address)
server.listen(1)
print('waiting for a connection')
connection,client_address=server.accept()
print("connection established with: ",client_address)
data=connection.recv(1000)
print("recieved: ",data)
connection.sendall(data)
connection.close()
server.close()
