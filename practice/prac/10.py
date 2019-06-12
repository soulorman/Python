#encoding: utf-8

stats = [('a',10),('b',5),('c',2)]

n = len(stats)
for j in range(n-1):
    for i in range(n-1):
        if stats[i][1] > stats[i+1][1]:
            temp = stats[i]
            stats[i] = stats[i+1]
            stats[i+1] = temp
print(stats)
