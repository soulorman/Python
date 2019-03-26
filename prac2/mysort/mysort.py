#enconding: utf-8

DEFAULT_KEY = lambda x : x 

def bubble(l,key):
    length = len(l)
    for j in range(length - 1):
        for i in range(length - 1):
            if key(l[i]) > key(l[i+1]):
                l[i+1],l[i] = l[i],l[i+1]

if __name__ == '__main__':
    print('test')
