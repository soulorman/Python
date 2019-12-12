# 实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。

# 示例 1：
# 输入: "Hello"
# 输出: "hello"

# 示例 2：
# 输入: "here"
# 输出: "here"

# 示例 3：
# 输入: "LOVELY"
# 输出: "lovely"

#encoding: utf-8

def ToLowerCase(str):
    for i in str:
        if 65 <= ord(i) and ord(i) <= 90:
            str = str.replace(i,chr(ord(i)+32))

    return str

str = "LOVELY"
print(ToLowerCase(str))

