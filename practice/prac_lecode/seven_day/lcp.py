# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。

# 示例 1:
# 输入: ["flower","flow","flight"]
# 输出: "fl"

# 示例 2:
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。

# 说明:
# 所有输入只包含小写字母 a-z 。

# 注意看题  前缀!!!,随便比两个就行

# 利用python的max()和min()，在Python里字符串是可以比较的，按照ascII值排，举例abb， aba，abac，最大为abb，最小为aba。所以只需要比较最大最小的公共前缀就是整个数组的公共前缀

def longestCommonPrefix(strs):
    if not strs:
        return ""

    str_min = min(strs)
    str_max = max(strs)

    for idx,val in enumerate(str_min):
        print(idx,val)
        if val != str_max[idx]:
            return str_max[:idx]        

    return str_min

strs = ["fl","fl","fl"]
print(longestCommonPrefix(strs))
