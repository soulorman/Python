# 核心思想就是判断左边的数是否小于右边的数
def test(s):
    d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    sum = 0
    # 预值
    pre = d.get(s[0])

    for i in range(1, len(s)):
        num = d.get(s[i])

        if pre < num:
            sum -= pre
        else:
            # 如果加pre + num 那么三个数 必然会多加一次，上面一样
            sum += pre

        pre = num

    #少加了一个预值
    sum += pre

    return sum

s = 'MCMXCIV'
print(test(s))
