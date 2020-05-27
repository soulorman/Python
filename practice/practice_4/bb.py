def foo1():
    a = [1]
    def bar():
       a[0] = a[0] + 1 
       print(bar.__closure__) 
       return a[0]
    return bar


c = foo1()
print(c())
print(c())
