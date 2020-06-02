from sys import argv
import os
 
def ping(net,start=80,end=85,n=1,w=3):
    for i in range(start,end+1):
        ip=net+"."+str(i)
        command="ping %s -n %d -w %d"%(ip,n,w)
        print(ip,("通","不通")[os.system(command)])
 
if len(argv) not in [2,4,6]:
    print("参数输入错误！")
    print("运行示例：")
    print("demo1.py  125.89.69")
    print("demo1.py  125.89.69 80 90")
    print("demo1.py  125.89.69 80 90 3 1")
    print("语法：demo1.py net startip endip count timeout")
 
elif len(argv)==2:
    net=argv[1]
    ping(net)
elif len(argv)==4:
    net=argv[1]
    ping(net,start=int(argv[2]),end=int(argv[3]))
else:
    net=argv[1]
    ping(net,start=int(argv[2]),end=int(argv[3]),n=int(argv[4]),w=int(argv[5]))
