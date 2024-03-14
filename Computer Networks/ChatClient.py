from socket import*

client=socket()
client.connect(('localhost',12000))
print('Connected to Server')

while True:
    recdata=client.recv(1024).decode()
    print('server: ',recdata)
    data=input('Client :')
    client.send(bytes(data,'utf-8'))
client.close()
