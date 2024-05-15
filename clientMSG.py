import socket

IP=str(input("insert IP: "))
PORT=int(input("insert PORT: "))
s=socket.socket()
s.connect((IP,PORT))

while True:
    res=s.recv(4000)
    print(res)
    m=input("you> ")
    s.send(m.encode())

s.close()