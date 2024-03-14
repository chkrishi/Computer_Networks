from socket import*
server=socket(AF_INET,SOCK_STREAM)
server.bind(('localhost',12000))
server.listen()
print('Server listening')
connection,address=server.accept()
print('Connected to Client')
while True:
    data=input('server: ')
    connection.send(bytes(data,'UTF-8'))
    recdata=connection.recv(1024).decode()
    print("client ",recdata)
connection.close()
