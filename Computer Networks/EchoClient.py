import socket
import sys
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=('localhost',9999)
client.connect(server_address)
message=input()
print("Sending ",message)
client.sendall(message.encode())
print("Original: ",message)

data=client.recv(1000).decode()
print("Echo: ",data)
client.close()
