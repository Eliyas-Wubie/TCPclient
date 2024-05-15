import socket

#creating socket and connectin
IP=str(input("insert IP: "))
PORT=int(input("port: "))
s=socket.socket()
s.connect((IP, PORT))

#reciving response i.e banner
res=s.recv(4000)
print ("BANNER: ",res)

#closeing the socket
s.close()