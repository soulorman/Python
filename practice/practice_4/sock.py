import socket
HostPort = ('127.0.0.1',9999)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(HostPort)
s.listen(1)
conn,addr = s.accept()
#print('Connecting by : %s ' % addr)
while 1:
    data = conn.recv(1024).decode()
    print (data)
    user_input = input('>>>')
    conn.send(user_input.encode('utf8'))
    #conn.close()
s.close()
