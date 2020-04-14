#!/usr/bin/python3 
def fbnq(num): 
    """斐波那契生成器 

    :param num: 生产数量 
    :return: 斐波那契迭代器 
    """ 
    a, b = 1, 1 
    for _ in range(num): 
        a, b = b, a+b 
        yield a 

if __name__ == '__main__': 
    gener = fbnq(20) 
    print(dir(gener))

