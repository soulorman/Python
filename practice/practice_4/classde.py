def deco(obj):
    obj.x = 1 
    return obj

@deco
class test:
    def __init__(self,name):
        self.name = name
print(test.__dict__)
