
from socket import *
import time

HOST = '172.26.78.123'
PORT = 9999
ADDR=(HOST,PORT)
SIZE = 5
BUFS = 1024
COD = 'utf-8'

tcps = socket(AF_INET,SOCK_STREAM)
tcps.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
tcps.bind(ADDR)
tcps.listen(SIZE)

while True:
    print('服务器已开启')
    conn, addr = tcps.accept()
    while True:
        try:
            data = conn.recv(BUFS)
        except Exception:
            print('断开客户端')
            break
        print('客户端发送{}'.format(data.decode(COD)))
        if not data:
            break
        msg = time.strftime("%x %X")
        msg1 = '[%s]:%s' %(msg, data.decode(COD))
        conn.send(msg1.encode(COD))
    conn.close()
tcps.close()
