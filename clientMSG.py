import socket

IP="192.168.1.104"
PORT=27441
s=socket.socket()
s.connect((IP,PORT))

while True:
    m=input("you> ")
    s.send(m.encode())
    res=s.recv(4000)
    print(res)



s.close()