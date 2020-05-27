import functools
def log(test):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f" {test} ok")
            func(*args, **kwargs)
        return wrapper
    return decorator


@log('i am')
def test():
    print('wo shi test')

@log('i am')
def test2():
    print('wo shi test2')

test()
test2()
print(test2.__name__)
