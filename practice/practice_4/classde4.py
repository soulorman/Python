class Sing(object):
    def __new__(cls, name, age):
        if not hasattr(cls, '_flag'):
            cls._flag = object.__new__(cls)
        return cls._flag


a = Sing('test1',16)
b = Sing('test2',17)

print(id(a))
print(id(b))

a.age = 2000

print(b.age)
