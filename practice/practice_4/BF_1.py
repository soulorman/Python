def bf_1(s1,s2):
    lis = []
    for i in range(len(s1)):
        index = i
        for j in range(len(s2)):
            if s1[index] != s2[j]:
                break
            index += 1
            if index == len(s2) + i:
                lis.append(i)
    return lis

s1 = 'abeabdabe'
s2 = 'abe'

print(bf_1(s1,s2))
