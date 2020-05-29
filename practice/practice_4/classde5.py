class Singleton(type):
    def __call__(cls, *args,**kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__call__(*args,**kwargs)
        return cls._instance


class Foo(metaclass = Singleton):
    pass


f1 = Foo()

f2 = Foo()

print(f1)
print(f2)
