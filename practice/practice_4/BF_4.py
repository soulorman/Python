def bf_plus(s1,s2):
    len1 = len(s1)
    len2 = len(s2)

    i = 0
    while i <= len1 - len2:
        is_find = True
        for j in range(len2):
            if s1[i + j] != s2[j]:
                is_find = False
                if s1[i + j] == s2[0]:
                    i = i + j - 1
                break
        i += 1
        if is_find:
            return i - 1
    return False

s1 = 'abe'
s2 = 'abe'
print(bf_plus(s1,s2))
