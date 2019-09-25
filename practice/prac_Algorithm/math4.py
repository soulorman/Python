# encoding: utf-8

s =''
n = 10

while n>0:
    s = str(n % 2) + s
    n //= 2
print(s)
