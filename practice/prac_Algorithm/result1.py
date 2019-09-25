# encoding: utf-8

def fib(number):

    x,y =0,1
    result = []
    while y<number:
        result.append(y)
        x,y = y,x+y
    return result

print(fib(15))
