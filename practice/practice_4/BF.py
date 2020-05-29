def find_chuan(s1,s2):
    length1 = len(s1)
    length2 = len(s2)
    index = 0
    for i in range(length1):
        if length1 - i < length2:
            break
        index = i
        for j in range(length2):
            if s1[index] == s2[j]:
                index+=1
            elif s1[index] != s2[j]:
                break
 
            if index == i+length2:
                lis = i

    return lis

s1 = 'aaaabcddd'
s2 = 'bcd'
print(find_chuan(s1,s2))



