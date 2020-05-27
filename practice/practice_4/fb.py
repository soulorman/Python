def fb(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b,a+b
        yield a


for j in fb(10):
    print(j)
