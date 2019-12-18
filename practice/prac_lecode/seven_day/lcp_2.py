#利用python的zip函数，把str看成list然后把输入看成二维数组，左对齐纵向压缩，然后把每项利用集合去重，之后遍历list中找到元素长度大于1之前的就是公共前缀

def longestCommonPrefix(strs):
    if not strs: 
        return ""
    # zip(*) 表示把strs里的字符 变成列表形式，然后一个元素一个元素的向里传
    # map(set, )  表示把返回的对象变成set去重
    ss = list(map(set, zip(*strs)))

    res = ""
    for i, x in enumerate(ss):    
# 这里的x 就是ss列表里，如果一项里有前缀重复的，那么这一项就只有一个元素，因为前面去重了
        x = list(x)
        if len(x) > 1:
            break
        res = res + x[0]
    return res

strs = ["flaar","flaaw","flaaht"]

print(longestCommonPrefix(strs))
