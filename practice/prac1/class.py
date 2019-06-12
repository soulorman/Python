#enconding: utf-8

class Person(object):
    id = 0
    @classmethod
    def gen_id(cls):
        return cls.id

a = Person.gen_id()
print(a)

kk = Person()
b = kk.gen_id()

print(b)





