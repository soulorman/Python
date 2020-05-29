def BF_1(s1, s2):
    lis = []
    hlen = len(s1)
    slen = len(s2)
    if hlen == 0 or slen ==0 or hlen < slen:
        return
    for i in range(hlen - slen + 1):
        is_find = True
        for j in range(slen):
            if s1[i + j] != s2[j]:
                is_find = False
                break
        if is_find:
            return i
    return False
s1 = 'abeabf'
s2 = 'abf'
print(BF_1(s1,s2))
