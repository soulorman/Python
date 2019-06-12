#enconding: utf-8

import hashlib

md5 = hashlib.md5()

md5.update(b'123')
a=md5.hexdigest()
print(a)



class TestUtils(object):
    @staticmethod
    def test():
        print('test')

TestUtils.test()