def create_next(s2):
    i = 0
    j = 1
    next = [0] * len(s2)
    while j < len(s2):
        if s2[i] == s2[j]:
            next[j] = i + 1
            i += 1
            j += 1
        elif i > 0:
            i = next[i - 1]
        else:
            j += 1

    return next


def kmp(s1, s2):
    i = 0
    j = 0
    while i < len(s1) and j <len(s2):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        elif j > 0:
            j = next[j - 1]
        else:
            i += 1

    if j == len(s2):
        return i - j
        
    return -1

