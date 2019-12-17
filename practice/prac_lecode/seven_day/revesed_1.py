# C语言做法
def test(x):
    if x // 10 == 0:
        return x

    y = 0
    while x:
        y *= 10
        print(y)
        if ( y > 2**31-1 or y < -2**31):
            return 0
        y += x % 10
        print(y)
        x //= 10
        print(x)

    return y

x = -123
print(test(x))
