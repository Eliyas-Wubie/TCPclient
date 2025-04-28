import socket

IP="127.0.0.1"
PORT=2020
s=socket.socket()
s.connect((IP,PORT))

while True:
    m=input("you> ")
    s.send(m.encode())
    res=s.recv(4000)
    print(res)



s.close()