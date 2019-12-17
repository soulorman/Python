#利用python的zip函数，把str看成list然后把输入看成二维数组，左对齐纵向压缩，然后把每项利用集合去重，之后遍历list中找到元素长度大于1之前的就是公共前缀

def longestCommonPrefix(strs):
    if not strs: 
        return ""
    ss = list(map(set, zip(*strs)))
    res = ""
    for i, x in enumerate(ss):
        x = list(x)
        if len(x) > 1:
            break
        res = res + x[0]
    return res

strs = ["oweflaar","oflaaw","igflaaht"]

print(longestCommonPrefix(strs))
