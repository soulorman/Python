def bf_plus(hstring: str, substring: str):
    hlen = len(hstring)
    slen = len(substring)
    if (hlen == 0) or (slen == 0) or (hlen < slen):
        return None
    i = 0
    while i <= hlen - slen:
        is_find = True
        for j in range(slen):  # 循环子串
            ch1 = hstring[i + j]
            ch2 = substring[j]
            if ch1 != ch2:
                is_find = False
                # 当匹配失败时，检查败的字符串是不是与首字母相同，若不同，继续BF算法；若相同，直接将首字母移到当前位置
                if (ch1 == substring[0]) and (j >= 1):
                    ipos = i + j
                    i = ipos - 1
                break
        i += 1
        if is_find:
            return i - 1
    return False
s1 = 'abc'
s2 = 'abc'
print(bf_plus(s1,s2))
