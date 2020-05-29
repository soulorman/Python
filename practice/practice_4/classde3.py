class Singleton(object):
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print('调用__init__， 实例未创建')
        else:
            print('调用__init__，实例已经创建过了')

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

a = Singleton()
b = Singleton()
print(id(a))
print(id(b))
