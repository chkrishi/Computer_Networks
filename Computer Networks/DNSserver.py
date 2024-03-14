import socket
dns_table={
    "www.google.com":"192.165.1.1",
    "www.youtbe.com":"192.165.2.2",
    "www.python.org":"192.165.3.3",
    "www.gmail.com":"192.165.4.4",
    "www.amazon.com":"192.165.5.5"
    }
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("Server Starting ...")
s.bind(("127.0.0.1",1234))
while True:
    data,address=s.recvfrom(1024)
    print(f"{address} wants to fetch data !")
    data=data.decode()
    ip=dns_table.get(data,"Not Found !").encode()
    send=s.sendto(ip,address)
s.close()
