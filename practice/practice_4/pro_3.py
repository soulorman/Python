from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename, version='1.0'):
    print('启动下载进程, 进程号[{}]'.format(getpid()))
    print('开始下载%s...' % (filename+version))
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('%s下载完成! 耗费%d秒' % (filename,time_to_download ))

def main():
    start = time()
    p1 = Process(target=download_task, args=('Python从入门到住院.pdf',),kwargs={'version':'v1.0'})
    p1.start()
    p2 = Process(target=download_task, args=('Peking Hot.avi',))
    p2.start()
    p3 = Process(target=download_task, args=('爸爸去哪儿了',))
    p3.start()
    p1.setDaemon(True)
    p2.setDaemon(True)
    p3.setDaemon(True)
    end = time()
    print('{}'.format(end-start))
    

if __name__ == '__main__':
    main()
