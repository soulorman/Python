#encoding: utf-8


def fact(n):
    if n<0:
        return None
    mul = 1
    for i in range(1,n+1):
        mul *= i
    return mul
print(fact(-1))
print(fact(100))
print(fact(1))
