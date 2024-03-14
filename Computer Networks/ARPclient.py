import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('localhost',1234))
a=input("Select ARP or RARP ")
if(a=="ARP"):
    x=input('Enter IP Address: ')
elif(a=="RARP"):
    x=input('Enter MAC Address: ')
s.send(x.encode())
mac=s.recv(1024)
mac=mac.decode("utf-8")
if(a=="ARP"):
    print('MAC Address of ',x,' is ',mac)
else:
    print('IP Address of ',x,' is ',mac)
