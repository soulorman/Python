import socket

# socket(套接字,类型,协议)
# 套接字: AF_UNIX  AF_INET
# 类型: SOCK_STREAM SOCK_DGRAM
# 协议: tcp udp 

# 创建
tcps = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定
#host = 127.0.0.1
host = socket.gethostname()
port = 9999
tcps.bind((host,port))

# 监听
tcps.listen(5)

# 开始读数据

while True:
    print('服务器已启动')
    conn, addr = tcps.accept()
    print('地址是{}'.format(addr))
    msg = 'test'
    conn.send(msg.encode('utf-8'))
    conn.close()
    
tcps.close() 
