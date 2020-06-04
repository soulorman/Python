import time
from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, name):  # 可以通过初始化来传递参数
        super().__init__()
        self.name = name

    def run(self):  # 必须有的函数
        print(f"{self.name}开始")
        time.sleep(0.2)
        print(f"{self.name}结束")


if __name__ == '__main__':
    p1 = MyProcess("进程1")  # 创建第一个进程，并传递参数
    p2 = MyProcess("进程2")  # 创建第二个进程，并传递参数
    p1.start()  # 开启第一个进程
    p2.start()  # 开启第二个进程
    print("主进程执行结束，子进程是依附于主进程存在的，所以，子进程都结束后，主进程才真正的结束。")
