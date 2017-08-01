import socket 
import sys
from thread import *
def ServerSocket(host,port,listenport):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print 'Socket created'
    try:
        s.bind((host,port))
    except socket.error ,msg:
        print 'Bind faild Error Code:'+str(msg[0])+'Message'+msg[1]
        sys.exit()
    print 'Socket bind complete'
    s.listen(listenport)
    print 'Socket is now listening'
    while 1:
        conn,addr=s.accept()
        print 'Connected with'+addr[0]+':'+str(addr[1])
        start_new_thread(clientthread, (conn,))
    s.close()
        
def clientthread(conn):
    conn.send('Welcome to the server.Enter your message\n')
    while True:
        data=conn.recv(10)
        replay=data
        if not data:
            break
        conn.sendall(replay)
        print(data)
    conn.close()
if __name__=="__main__":
    ServerSocket('localhost', 8833, 14)




     