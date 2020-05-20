L = [89,67,56,45,34,23,1]
for i in range(1,len(L)):
    j = i
    while j >= 0 and L[j] < L[j-1]:
        L[j], L[j-1] = L[j-1],L[j-1]
        j -= 1
print(L)
