#enconding: utf-8

def fact(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    return n * fact(n -1)
'''
n-1! = 1*2*3*4...*n-2*n-1
n-2!=1*2*3*4...*n-3*n-2

n! = (n-1)! * n

'''
print(fact(-1))
print(fact(0))
print(fact(5))