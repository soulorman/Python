import os
def ping(net, start=80,end=90,number=1,timeout=3):
    for i in range(start,end+1):
        ip = net + '.' + str(i)
        command = "ping {} -c {} -W {}".format(ip,number,timeout)
        print(ip,"不通" if os.system(command) else '通')
ping('127.0.0',1,2,3,1)
