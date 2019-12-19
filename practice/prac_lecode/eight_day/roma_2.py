# 核心思想 使用正则替换单个或者2个字符
# re.subn会返回替换完成的字符以及匹配次数，用val乘以次数，如果有匹配就把当前值加上

import re
def test(s):
    
    table=[('CM', 900), ('CD', 400), ('XC', 90), ('XL', 40), ('IX', 9), ('IV', 4), ('M', 1000), ('D', 500), ('C', 100), ('L', 50), ('X', 10), ('V', 5), ('I', 1)]
    res = 0
    for cha,val in table:
        s, n = re.subn(cha, '', s)
        res += val * n
    return res

s = "XLIV"
print(test(s))

