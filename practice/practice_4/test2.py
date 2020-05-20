class B(object):
    def __next__(self):
        raise StopIteration

class A(object):
    def __iter__(self):
        return B()


from collections.abc import *

a = A()
b = B()
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))

print(isinstance(b, Iterable))
print(isinstance(b, Iterator))
