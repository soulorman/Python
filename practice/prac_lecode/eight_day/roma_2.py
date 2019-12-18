# 核心思想就是 替换字符为数字
def test(s):
    table=[('CM', 900), ('CD', 400), ('XC', 90), ('XL', 40), ('IX', 9), ('IV', 4), ('M', 1000), ('D', 500), ('C', 100), ('L', 50), ('X', 10), ('V', 5), ('I', 1)]
    import re
    res=0

    for cha,val in table:
        s, n = re.subn(cha,'',s)
        res += val * n

    return res

s = "XLIV"
print(test(s))
