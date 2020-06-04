
def counting_sort(a, k):  # k = max(a)
    n = len(a)  # 计算a序列的长度
    b = [0 for i in range(n)]  # 设置输出序列并初始化为0
    c = [0 for i in range(k + 1)]  # 设置计数序列并初始化为0，
    for j in a:
        c[j] = c[j] + 1
    for i in range(1, len(c)):
        c[i] = c[i] + c[i-1]
    for j in a:
        b[c[j] - 1] = j
        c[j] = c[j] - 1
    return b

a = [3,5,6,7,8,2,3,232,4,235]
print(counting_sort(a, max(a)))
